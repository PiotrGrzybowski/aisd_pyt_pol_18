import random
from typing import List


def partition(values: List, low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    values[pivot_index], values[high] = values[high], values[pivot_index]
    pivot = values[high]
    j = low - 1

    for i in range(low, high):
        if values[i] < pivot:
            j += 1
            values[i], values[j] = values[j], values[i]
    j += 1
    values[j], values[high] = values[high], values[j]
    return j


def quick_select(values: List[int], k: int) -> int:
    def quick_select_help(low: int, high: int) -> int:
        pass

    return quick_select_help(0, len(values) - 1)
