import abc
import random


class InputMaker(abc.ABC):
    @abc.abstractmethod
    def make(self, *args, **kwargs):
        pass


class RandomListMaker(InputMaker):
    def make(self, size: int) -> list[int]:
        return [random.randint(0, int(1e6)) for _ in range(size)]


class OrderedListMaker(InputMaker):
    def make(self, size: int) -> list[int]:
        return list(range(size))


class ReversedListMaker(InputMaker):
    def make(self, size: int) -> list[int]:
        return list(reversed(range(size)))