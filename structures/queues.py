from __future__ import annotations

from abc import ABC, abstractmethod

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


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
        pass

    def pop(self) -> T:
        pass

    def front(self) -> T:
        pass
