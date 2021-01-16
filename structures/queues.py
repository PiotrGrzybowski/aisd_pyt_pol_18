from __future__ import annotations

from abc import ABC, abstractmethod

from typing import TypeVar, Generic, Optional

from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None


class AbstractQueue(ABC, Generic[T]):
    def __init__(self) -> None:
        self.size = 0

    @abstractmethod
    def push(self, element: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def front(self) -> T:
        pass

    def __len__(self) -> int:
        return self.size


class Queue(AbstractQueue[T]):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def push(self, element: T) -> None:
        node = Node[T](element)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def pop(self) -> T:
        pass

    def front(self) -> T:
        pass
