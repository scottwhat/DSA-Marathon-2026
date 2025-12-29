"""LRU Cache using doubly linked list + dict.

Run:
    python baseimplementations/lru_cache.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Node(Generic[K, V]):
    key: K
    val: V
    prev: Optional["_Node[K, V]"] = None
    next: Optional["_Node[K, V]"] = None


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self._map: dict[K, _Node[K, V]] = {}

        # sentinels
        self._head = _Node(key=None, val=None)  # type: ignore[arg-type]
        self._tail = _Node(key=None, val=None)  # type: ignore[arg-type]
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node[K, V]) -> None:
        p, n = node.prev, node.next
        assert p is not None and n is not None
        p.next = n
        n.prev = p

    def _insert_front(self, node: _Node[K, V]) -> None:
        first = self._head.next
        assert first is not None
        node.prev = self._head
        node.next = first
        self._head.next = node
        first.prev = node

    def get(self, key: K) -> Optional[V]:
        if key not in self._map:
            return None
        node = self._map[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: K, value: V) -> None:
        if key in self._map:
            node = self._map[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)
            return

        node = _Node(key=key, val=value)
        self._map[key] = node
        self._insert_front(node)

        if len(self._map) > self.capacity:
            # evict LRU = node just before tail
            lru = self._tail.prev
            assert lru is not None and lru is not self._head
            self._remove(lru)
            self._map.pop(lru.key)


def _test_lru_cache() -> None:
    c = LRUCache[int, str](capacity=2)
    c.put(1, "one")
    c.put(2, "two")
    assert c.get(1) == "one"  # now 2 is LRU
    c.put(3, "three")
    assert c.get(2) is None
    assert c.get(3) == "three"
    c.put(1, "ONE")
    assert c.get(1) == "ONE"


if __name__ == "__main__":
    _test_lru_cache()
    print("lru_cache.py: OK")
