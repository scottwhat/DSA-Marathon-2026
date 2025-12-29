"""Stack, Queue, and Deque.

Run:
    python baseimplementations/stack_queue_deque.py
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Generic, Iterable, Optional, TypeVar


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, values: Optional[Iterable[T]] = None):
        self._data: list[T] = []
        if values is not None:
            for v in values:
                self.push(v)

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def push(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]


class Queue(Generic[T]):
    """FIFO queue backed by collections.deque."""

    def __init__(self, values: Optional[Iterable[T]] = None):
        self._data: Deque[T] = deque()
        if values is not None:
            for v in values:
                self.enqueue(v)

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def enqueue(self, value: T) -> None:
        self._data.append(value)

    def dequeue(self) -> T:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]


class SimpleDeque(Generic[T]):
    def __init__(self, values: Optional[Iterable[T]] = None):
        self._data: Deque[T] = deque()
        if values is not None:
            self._data.extend(values)

    def __len__(self) -> int:
        return len(self._data)

    def append_left(self, value: T) -> None:
        self._data.appendleft(value)

    def append_right(self, value: T) -> None:
        self._data.append(value)

    def pop_left(self) -> T:
        if not self._data:
            raise IndexError("pop_left from empty deque")
        return self._data.popleft()

    def pop_right(self) -> T:
        if not self._data:
            raise IndexError("pop_right from empty deque")
        return self._data.pop()

    def peek_left(self) -> T:
        if not self._data:
            raise IndexError("peek_left from empty deque")
        return self._data[0]

    def peek_right(self) -> T:
        if not self._data:
            raise IndexError("peek_right from empty deque")
        return self._data[-1]


def _test_stack_queue_deque() -> None:
    s = Stack[int]()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1

    q = Queue[str](["a", "b"]) 
    q.enqueue("c")
    assert q.dequeue() == "a"
    assert q.peek() == "b"
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"

    d = SimpleDeque[int]([2, 3])
    d.append_left(1)
    d.append_right(4)
    assert d.peek_left() == 1
    assert d.peek_right() == 4
    assert d.pop_left() == 1
    assert d.pop_right() == 4
    assert d.pop_left() == 2
    assert d.pop_right() == 3


if __name__ == "__main__":
    _test_stack_queue_deque()
    print("stack_queue_deque.py: OK")
