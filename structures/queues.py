from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None


class EmptyQueueError(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


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

    # def __bool__(self) -> bool:
    #     pass


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
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1

            if self.head is None:
                self.tail = None
            return value
        else:
            raise EmptyQueueError('Can not pop from empty queue.')

    def front(self) -> T:
        if self.head:
            return self.head.value
        else:
            raise EmptyQueueError('Can not read from empty queue.')


class Stack(AbstractQueue[T]):
    def __init__(self):
        super().__init__()
        self.head = None

    def push(self, element: T) -> None:
        node = Node[T](element)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self) -> T:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        else:
            raise EmptyQueueError('Cannot pop from empty stack.')

    def front(self) -> T:
        if self.head:
            return self.head.value
        else:
            raise EmptyQueueError('Cannot read from empty stack.')