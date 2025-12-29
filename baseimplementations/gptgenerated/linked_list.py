"""Singly Linked List (basic implementation).

Run:
    python baseimplementations/linked_list.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar


T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self, values: Optional[Iterable[T]] = None):
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size = 0
        if values is not None:
            for v in values:
                self.append(v)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        curr = self._head
        while curr is not None:
            yield curr.value
            curr = curr.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(map(repr, self))}])"

    def is_empty(self) -> bool:
        return self._size == 0

    def prepend(self, value: T) -> None:
        node = Node(value=value, next=self._head)
        self._head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def append(self, value: T) -> None:
        node = Node(value=value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("pop_front from empty list")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        if self._head is None:
            self._tail = None
        return value

    def find(self, value: T) -> Optional[Node[T]]:
        curr = self._head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def to_list(self) -> list[T]:
        return list(self)


def _test_linked_list() -> None:
    ll = SinglyLinkedList([2, 3])
    assert ll.to_list() == [2, 3]
    ll.prepend(1)
    assert ll.to_list() == [1, 2, 3]
    ll.append(4)
    assert ll.to_list() == [1, 2, 3, 4]
    assert len(ll) == 4
    assert ll.find(3) is not None
    assert ll.find(999) is None
    assert ll.pop_front() == 1
    assert ll.to_list() == [2, 3, 4]

    ll2 = SinglyLinkedList[int]()
    try:
        ll2.pop_front()
        raise AssertionError("Expected IndexError")
    except IndexError:
        pass


if __name__ == "__main__":
    _test_linked_list()
    print("linked_list.py: OK")
