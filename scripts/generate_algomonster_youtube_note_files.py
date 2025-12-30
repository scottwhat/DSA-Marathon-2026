"""Generate one Python note file per AlgoMonster YouTube video.

This script tries to fetch *all* videos from the channel handle by:
- Downloading the /videos page and extracting ytInitialData + INNERTUBE key/context
- Following continuation tokens via YouTube's internal browse endpoint

If YouTube changes its page structure, this may need adjustments.

Usage:
  C:/.../.venv/Scripts/python.exe scripts/generate_algomonster_youtube_note_files.py

Optional:
  --out "algomap/youtube videos summaries"   Output dir (default set)
  --handle "algo.monster"                   Channel handle
  --max 9999                                 Max videos to fetch (safety)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


def _http_get(url: str, *, headers: dict[str, str] | None = None, timeout: float = 30.0) -> str:
    req = urllib.request.Request(
        url,
        headers=headers
        or {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _http_post_json(url: str, payload: dict, *, headers: dict[str, str] | None = None, timeout: float = 30.0) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers=headers
        or {
            "Content-Type": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    return json.loads(text)


def _extract_json_object(text: str, marker: str) -> dict:
    """Extract a JSON object assigned after `marker` by bracket matching."""
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError(f"Could not find marker: {marker}")

    # Find first '{' after marker
    brace = text.find("{", idx)
    if brace < 0:
        raise RuntimeError(f"Could not find opening '{{' after marker: {marker}")

    depth = 0
    for end in range(brace, len(text)):
        ch = text[end]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                raw = text[brace : end + 1]
                return json.loads(raw)

    raise RuntimeError(f"Unbalanced JSON braces after marker: {marker}")


def _slugify_filename(title: str, *, max_len: int = 120) -> str:
    title = title.strip().lower()
    # Replace separators with spaces
    title = re.sub(r"[\s\-_/]+", " ", title)
    # Keep alnum, spaces
    title = re.sub(r"[^a-z0-9 ]+", "", title)
    title = re.sub(r"\s+", "_", title).strip("_")
    if not title:
        title = "untitled"
    if len(title) > max_len:
        title = title[:max_len].rstrip("_")
    return title


def _find_video_renderers(obj) -> list[dict]:
    """Walk JSON and collect videoRenderer dicts."""
    found: list[dict] = []

    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            if "videoRenderer" in cur and isinstance(cur["videoRenderer"], dict):
                found.append(cur["videoRenderer"])
            for v in cur.values():
                stack.append(v)
        elif isinstance(cur, list):
            stack.extend(cur)

    return found


def _extract_title(renderer: dict) -> str | None:
    title = renderer.get("title")
    if isinstance(title, dict):
        # Most common: { runs: [ { text: "..." } ] }
        runs = title.get("runs")
        if isinstance(runs, list) and runs:
            text = runs[0].get("text")
            if isinstance(text, str) and text.strip():
                return text.strip()
        simple = title.get("simpleText")
        if isinstance(simple, str) and simple.strip():
            return simple.strip()
    return None


def _extract_video_id(renderer: dict) -> str | None:
    vid = renderer.get("videoId")
    if isinstance(vid, str) and vid:
        return vid
    return None


def _extract_continuation_tokens(obj) -> list[str]:
    tokens: list[str] = []

    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            # Typical shape: { continuationCommand: { token: "..." } }
            cc = cur.get("continuationCommand")
            if isinstance(cc, dict):
                tok = cc.get("token")
                if isinstance(tok, str) and tok:
                    tokens.append(tok)
            for v in cur.values():
                stack.append(v)
        elif isinstance(cur, list):
            stack.extend(cur)

    # De-dup while preserving order
    seen = set()
    ordered = []
    for t in tokens:
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    return ordered


def _write_note_file(out_dir: str, *, title: str, video_id: str, url: str) -> str:
    safe = _slugify_filename(title)
    filename = f"{safe}__{video_id}.py"
    path = os.path.join(out_dir, filename)

    if os.path.exists(path):
        return path

    content = f'''"""Video: {title}
URL: {url}

Summary
- 

Key Ideas
- 

Patterns / Templates
- 

Pitfalls
- 

Related Problems
- 

My Notes
- 
"""
'''

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return path


def _try_rss_fallback(handle: str) -> list[tuple[str, str]]:
    """Fallback to RSS (usually only most recent ~15). Returns (title, video_id)."""
    # Best-effort: fetch handle page and extract channel ID
    html = _http_get(f"https://www.youtube.com/@{handle}")
    m = re.search(r'"channelId"\s*:\s*"(UC[^"]+)"', html)
    if not m:
        m = re.search(r'"browseId"\s*:\s*"(UC[^"]+)"', html)
    if not m:
        return []

    channel_id = m.group(1)
    feed = _http_get(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")

    # Parse XML
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
    }
    root = ET.fromstring(feed)
    pairs: list[tuple[str, str]] = []
    for entry in root.findall("atom:entry", ns):
        t = entry.findtext("atom:title", default="", namespaces=ns).strip()
        vid = entry.findtext("yt:videoId", default="", namespaces=ns).strip()
        if t and vid:
            pairs.append((t, vid))
    return pairs


def fetch_all_videos_from_handle(handle: str, *, max_videos: int = 10000) -> list[tuple[str, str]]:
    """Return list of (title, video_id)."""

    videos_url = f"https://www.youtube.com/@{handle}/videos"
    html = _http_get(videos_url)

    # Extract required pieces to call continuation endpoint.
    # ytInitialData contains the first page of videos.
    try:
        initial_data = _extract_json_object(html, "var ytInitialData =")
    except Exception:
        # Sometimes it's `ytInitialData =` without `var`.
        initial_data = _extract_json_object(html, "ytInitialData =")

    # INNERTUBE context / key live in ytInitialPlayerResponse / ytcfg.
    # Grab API key
    api_key_match = re.search(r'"INNERTUBE_API_KEY"\s*:\s*"([^"]+)"', html)
    api_key = api_key_match.group(1) if api_key_match else None

    # Grab client context
    # ytcfg.set({ ... }) is common
    context: dict | None = None
    try:
        cfg = _extract_json_object(html, "ytcfg.set(")
        innertube_ctx = cfg.get("INNERTUBE_CONTEXT")
        if isinstance(innertube_ctx, dict):
            context = innertube_ctx
    except Exception:
        context = None

    # Parse initial batch
    renderers = _find_video_renderers(initial_data)
    results: list[tuple[str, str]] = []
    seen_vids: set[str] = set()

    for r in renderers:
        vid = _extract_video_id(r)
        title = _extract_title(r)
        if vid and title and vid not in seen_vids:
            seen_vids.add(vid)
            results.append((title, vid))
            if len(results) >= max_videos:
                return results

    if not api_key or not context:
        # Fallback to RSS if we can't continue.
        rss = _try_rss_fallback(handle)
        for title, vid in rss:
            if vid not in seen_vids:
                seen_vids.add(vid)
                results.append((title, vid))
                if len(results) >= max_videos:
                    break
        return results

    # Continuations
    tokens = _extract_continuation_tokens(initial_data)
    # Usually the first continuation token is enough; keep a queue for safety.
    queue = list(tokens)

    browse_url = f"https://www.youtube.com/youtubei/v1/browse?key={urllib.parse.quote(api_key)}"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    while queue and len(results) < max_videos:
        token = queue.pop(0)
        payload = {
            "context": context,
            "continuation": token,
        }

        try:
            data = _http_post_json(browse_url, payload, headers=headers)
        except Exception:
            break

        # Extract videos
        renderers = _find_video_renderers(data)
        for r in renderers:
            vid = _extract_video_id(r)
            title = _extract_title(r)
            if vid and title and vid not in seen_vids:
                seen_vids.add(vid)
                results.append((title, vid))
                if len(results) >= max_videos:
                    return results

        # Extract next continuation tokens
        new_tokens = _extract_continuation_tokens(data)
        for t in new_tokens:
            if t not in queue:
                queue.append(t)

        # Be gentle
        time.sleep(0.15)

    # If we got nothing at all, at least try RSS
    if not results:
        return _try_rss_fallback(handle)

    return results


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        default=os.path.join("algomap", "youtube videos summaries"),
        help="Output directory (relative to repo root).",
    )
    parser.add_argument("--handle", default="algo.monster", help="YouTube channel handle")
    parser.add_argument(
        "--max",
        type=int,
        default=10000,
        help="Max videos to fetch (safety limit).",
    )
    args = parser.parse_args(argv)

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    out_dir = os.path.abspath(os.path.join(repo_root, args.out))
    os.makedirs(out_dir, exist_ok=True)

    videos = fetch_all_videos_from_handle(args.handle, max_videos=args.max)
    if not videos:
        print("No videos found. YouTube may have changed markup, or network blocked.")
        return 2

    created = 0
    skipped = 0
    for title, vid in videos:
        url = f"https://www.youtube.com/watch?v={vid}"
        path = _write_note_file(out_dir, title=title, video_id=vid, url=url)
        if os.path.getsize(path) > 0:
            # If it already existed we still return the same path; detect existence by counting.
            # Cheap check: if file existed, we didn't create now.
            # We'll treat "exists" as skipped by checking for creation timestamp is not reliable cross-platform.
            pass

    # Recount created by scanning which filenames exist for fetched set.
    expected = {f"{_slugify_filename(t)}__{vid}.py" for t, vid in videos}
    existing = set(os.listdir(out_dir))
    present = expected & existing
    created = len(present)

    print(f"Fetched videos: {len(videos)}")
    print(f"Note files present for fetched set: {created}")
    print(f"Output dir: {out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
