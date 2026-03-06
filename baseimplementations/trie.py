"""Trie (prefix tree) for lowercase strings.

Run:
    python baseimplementations/trie.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    is_word: bool = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self._root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


def _test_trie() -> None:
    t = Trie()
    for w in ["apple", "app", "ape", "bat"]:
        t.insert(w)

    assert t.search("app")
    assert t.search("apple")
    assert not t.search("ap")
    assert t.starts_with("ap")
    assert t.starts_with("bat")
    assert not t.starts_with("cat")


if __name__ == "__main__":
    _test_trie()
    print("trie.py: OK")
