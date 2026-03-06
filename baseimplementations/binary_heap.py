"""Binary Heap (min-heap and max-heap) with basic operations.

Run:
    python baseimplementations/binary_heap.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Optional, TypeVar


T = TypeVar("T")


@dataclass
class _HeapItem(Generic[T]):
    priority: int
    value: T


class BinaryHeap(Generic[T]):
    """A simple binary heap with integer priorities.

    - min_heap=True: smaller priority pops first
    - min_heap=False: larger priority pops first (max-heap)
    """

    def __init__(self, items: Optional[Iterable[tuple[int, T]]] = None, *, min_heap: bool = True):
        self._data: list[_HeapItem[T]] = []
        self._min = min_heap
        if items is not None:
            for p, v in items:
                self.push(p, v)

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def _better(self, a: _HeapItem[T], b: _HeapItem[T]) -> bool:
        return a.priority < b.priority if self._min else a.priority > b.priority

    def push(self, priority: int, value: T) -> None:
        self._data.append(_HeapItem(priority, value))
        self._sift_up(len(self._data) - 1)

    def peek(self) -> tuple[int, T]:
        if not self._data:
            raise IndexError("peek from empty heap")
        top = self._data[0]
        return top.priority, top.value

    def pop(self) -> tuple[int, T]:
        if not self._data:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        if self._data:
            self._sift_down(0)
        return item.priority, item.value

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self._better(self._data[i], self._data[p]):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            l = self._left(i)
            r = self._right(i)
            best = i

            if l < n and self._better(self._data[l], self._data[best]):
                best = l
            if r < n and self._better(self._data[r], self._data[best]):
                best = r

            if best == i:
                break
            self._swap(i, best)
            i = best


def _test_binary_heap() -> None:
    h = BinaryHeap[str](min_heap=True)
    h.push(5, "e")
    h.push(1, "a")
    h.push(3, "c")
    assert h.peek() == (1, "a")
    assert h.pop() == (1, "a")
    assert h.pop() == (3, "c")
    assert h.pop() == (5, "e")

    h2 = BinaryHeap[str]([(2, "b"), (9, "i"), (4, "d")], min_heap=False)
    assert h2.pop() == (9, "i")
    assert h2.pop() == (4, "d")
    assert h2.pop() == (2, "b")


if __name__ == "__main__":
    _test_binary_heap()
    print("binary_heap.py: OK")
