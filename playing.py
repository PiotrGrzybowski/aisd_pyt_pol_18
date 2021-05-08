# import timeit
# from sorting.algorithms import bubble_sort, generate_random_list, generate_reversed_list
#
#
#
# def time_function(function, *args) -> float:
#     return timeit.Timer(lambda: function(*args)).timeit(1)
#
#
# def foo(num1, num2):
#     pass
#     # do something to num1 and num2
#
# def
# A = 1
# B = 2
#
# values = generate_reversed_list(1000)
#
# # bubble_sort(values)
# # t = time_function(bubble_sort, values)
# # print(t)
# n = 10
# t = timeit.Timer(lambda: bubble_sort(values))
# print(t.repeat(5, 5))
# How to use Profile class of cProfile
from random import randint
from typing import Any, List


def generate_random_list(length, start=0, end=100000):
    return [randint(start, end) for _ in range(length)]


def generate_ordered_list(length):
    return list(range(length))


def generate_reversed_list(length):
    return list(reversed(range(length)))


def bubble_sort(values: List[Any]) -> None:
    length = len(values)
    for n in range(length):
        for index in range(length - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


def partition(values: List[Any], left: int, right: int) -> int:
    pivot = values[right]
    j = left - 1

    for i in range(left, right):
        if values[i] < pivot:
            j += 1
            values[i], values[j] = values[j], values[i]
    j += 1
    values[j], values[right] = values[right], values[j]
    return j


def quick_sort(values: List[Any]) -> None:
    def quick_sort_help(left: int, right: int) -> None:
        if left < right:
            index = partition(values, left, right)
            quick_sort_help(left, index - 1)
            quick_sort_help(index + 1, right)

    quick_sort_help(0, len(values) - 1)


if __name__ == '__main__':
    import cProfile, pstats
    import numpy as np
    import sys
    sys.setrecursionlimit(2000)


    profiler = cProfile.Profile()

    profiler.enable()
    for _ in range(100):
        values = generate_random_list(1000)
        quick_sort(values)
    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats('cumtime')

    print(stats.total_tt/10)
    stats.print_stats()
