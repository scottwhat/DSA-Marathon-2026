"""Hash map using separate chaining (educational, not production).

Run:
    python baseimplementations/hash_map.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar


K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Entry(Generic[K, V]):
    key: K
    value: V


class HashMap(Generic[K, V]):
    def __init__(self, *, initial_capacity: int = 8, max_load_factor: float = 0.75):
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be >= 1")
        self._buckets: list[list[_Entry[K, V]]] = [[] for _ in range(initial_capacity)]
        self._size = 0
        self._max_load_factor = max_load_factor

    def __len__(self) -> int:
        return self._size

    def _bucket_index(self, key: K) -> int:
        return hash(key) % len(self._buckets)

    def _rehash(self, new_capacity: int) -> None:
        old_items = list(self.items())
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0
        for k, v in old_items:
            self[k] = v

    def _maybe_grow(self) -> None:
        if self._size / len(self._buckets) > self._max_load_factor:
            self._rehash(len(self._buckets) * 2)

    def __setitem__(self, key: K, value: V) -> None:
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        bucket.append(_Entry(key, value))
        self._size += 1
        self._maybe_grow()

    def __getitem__(self, key: K) -> V:
        idx = self._bucket_index(key)
        for entry in self._buckets[idx]:
            if entry.key == key:
                return entry.value
        raise KeyError(key)

    def __delitem__(self, key: K) -> None:
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, entry in enumerate(bucket):
            if entry.key == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key: object) -> bool:
        try:
            self[key]  # type: ignore[index]
            return True
        except KeyError:
            return False

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self) -> Iterator[K]:
        for bucket in self._buckets:
            for entry in bucket:
                yield entry.key

    def values(self) -> Iterator[V]:
        for bucket in self._buckets:
            for entry in bucket:
                yield entry.value

    def items(self) -> Iterator[tuple[K, V]]:
        for bucket in self._buckets:
            for entry in bucket:
                yield entry.key, entry.value


def _test_hash_map() -> None:
    m = HashMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["a"] = 3
    assert len(m) == 2
    assert m["a"] == 3
    assert m.get("missing") is None
    assert "b" in m
    del m["b"]
    assert "b" not in m

    # Basic resize path
    m2 = HashMap[int, int](initial_capacity=2)
    for i in range(50):
        m2[i] = i * i
    for i in range(50):
        assert m2[i] == i * i


if __name__ == "__main__":
    _test_hash_map()
    print("hash_map.py: OK")
