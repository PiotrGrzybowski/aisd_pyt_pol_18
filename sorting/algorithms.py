import random
from typing import List


def generate_random_list(length: int, start: int, end: int) -> List[int]:
    return [random.randint(start, end) for _ in range(length)]


def generate_ordered_list(length: int) -> List[int]:
    return list(range(length))


def generate_reversed_list(length: int) -> List[int]:
    return list(reversed(range(length)))


def bubble_sort(values: List) -> None:
    for n in range(len(values)):
        for i in range(len(values) - 1 - n):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]


def bubble_sort_smart(values: List) -> None:
    n = 0
    swap_occurred = True

    while n < len(values) and swap_occurred:
        swap_occurred = False
        for i in range(len(values) - 1 - n):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swap_occurred = True


if __name__ == '__main__':
    values = [8, 7, 6, 5, 4, 3, 2, 1]
    values = [1, 2, 3, 4, 5, 6, 7, 8]

    values = ['S', 'A', 'C', 'G', 'a']
    bubble_sort_smart(values)
    print(values)
