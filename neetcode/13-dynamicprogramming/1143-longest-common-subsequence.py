# https://leetcode.com/problems/longest-common-subsequence/description/

# Time: O(n * m), Space: O(n * m)
def memoization(s1, s2):
    rows, cols = len(s1), len(s2)
    cache = [[0] * cols for _ in range(rows)]
    return memoHelper(s1, s2, 0, 0, cache)

def memoHelper(s1, s2, i1, i2, cache):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if cache[i1][i2] != 0:
        return cache[i1][i2]

    if s1[i1] == s2[i2]:
        cache[i1][i2] = 1 + memoHelper(s1, s2, i1 + 1, i2 + 1, cache)
    else:
        cache[i1][i2] = max(memoHelper(s1, s2, i1 + 1, i2, cache),
                memoHelper(s1, s2, i1, i2 + 1, cache))
    return cache[i1][i2]


def _get_empty_symbol():
    import sys

    symbol = "∅"
    encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        symbol.encode(encoding)
        return symbol
    except Exception:
        return "."


def _format_dp_table(dp, s1, s2, highlight=None):
    """Pretty-print a (len(s1)+1) x (len(s2)+1) DP table.

    highlight: optional (i, j) to visually mark the cell just updated.
    """
    rows, cols = len(s1), len(s2)

    def cell_str(i, j):
        value = dp[i][j]
        if highlight == (i, j):
            return f"[{value:2d}]"
        return f" {value:2d} "

    empty = _get_empty_symbol()
    header = "      " + "  ".join([f" {ch} " for ch in s2] + [f"  {empty} "])
    lines = [header]
    for i in range(rows + 1):
        row_label = s1[i] if i < rows else empty
        row_cells = " ".join(cell_str(i, j) for j in range(cols + 1))
        lines.append(f" {row_label} | {row_cells}")
    return "\n".join(lines)


def lcs_bottom_up_with_trace(s1, s2):
    """Bottom-up LCS with verbose tracing.

    Prints, for each DP cell update:
    - what characters are compared
    - what subproblems are referenced
    - the chosen value
    - the full DP table after the update
    """
    rows, cols = len(s1), len(s2)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    print(f"s1={s1!r}, s2={s2!r}")
    print("DP meaning: dp[i][j] = LCS length of s1[i:] and s2[j:]")
    print("Filling from bottom-right to top-left.\n")

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            c1, c2 = s1[i], s2[j]
            if c1 == c2:
                dp[i][j] = 1 + dp[i + 1][j + 1]
                print(
                    f"Compare s1[{i}]='{c1}' vs s2[{j}]='{c2}' => MATCH; "
                    f"dp[{i}][{j}] = 1 + dp[{i+1}][{j+1}] ({dp[i+1][j+1]}) = {dp[i][j]}"
                )
            else:
                down = dp[i + 1][j]
                right = dp[i][j + 1]
                dp[i][j] = max(down, right)
                chosen = "down" if down >= right else "right"
                print(
                    f"Compare s1[{i}]='{c1}' vs s2[{j}]='{c2}' => NO MATCH; "
                    f"dp[{i}][{j}] = max(dp[{i+1}][{j}]={down}, dp[{i}][{j+1}]={right}) = {dp[i][j]} "
                    f"(chose {chosen})"
                )

            print(_format_dp_table(dp, s1, s2, highlight=(i, j)))
            print("-" * 80)

    print(f"Final answer: LCS length = dp[0][0] = {dp[0][0]}")
    return dp[0][0]


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    # Usage:
    #   python 1143-longest-common-subsequence.py
    #   python 1143-longest-common-subsequence.py abcde ace
    s1 = sys.argv[1] if len(sys.argv) > 1 else "abcde"
    s2 = sys.argv[2] if len(sys.argv) > 2 else "ace"

    lcs_len = lcs_bottom_up_with_trace(s1, s2)
    print(f"\n(memoization check) LCS length = {memoization(s1, s2)}")