from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None

    def append(self, element: T) -> None:
        node = Node[T](element)
        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next

            pointer.next = node

    def __len__(self) -> int:
        length = 0
        pointer = self.head
        while pointer is not None:
            length += 1
            pointer = pointer.next
        return length


if __name__ == '__main__':
    values = LinkedList[str]()
    values.append('apple')
    values.append('orange')
    values.append('strawberry')

    print(values.head)
    print(values.head.next)
    print(values.head.next.next)

    print(len(values))