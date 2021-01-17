from abc import ABC, abstractmethod
from typing import List


class SoringAlgorithm(ABC):
    def __init__(self):
        self.comparisons = 0

    @abstractmethod
    def sort(self, values: List) -> None:
        pass

    def gt(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 > value_2


class BubbleSort(SoringAlgorithm):
    def sort(self, values: List) -> None:
        for n in range(len(values)):
            for i in range(len(values) - 1 - n):
                if self.gt(values[i], values[i + 1]):
                    values[i], values[i + 1] = values[i + 1], values[i]


class BubbleSortSmart(SoringAlgorithm):
    def sort(self, values: List) -> None:
        n = 0
        swap_occurred = True

        while n < len(values) and swap_occurred:
            swap_occurred = False
            for i in range(len(values) - 1 - n):
                if self.gt(values[i], values[i + 1]):
                    values[i], values[i + 1] = values[i + 1], values[i]
                    swap_occurred = True


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    algorithm = BubbleSortSmart()
    algorithm.sort(values)
    print(values)
    print(algorithm.comparisons)
