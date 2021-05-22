import tqdm
import os
import random
import timeit
import cProfile, pstats
from enum import Enum
import json
import numpy as np
import sys

sys.setrecursionlimit(2000)

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
from typing import Any, List, Callable, Union, Dict
import abc


class SeriesGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self, length: int) -> List[int]:
        raise NotImplementedError


class RandomSeriesGenerator(SeriesGenerator):
    def generate(self, length: int) -> List[int]:
        return [randint(0, int(1e6)) for _ in range(length)]


class OrderedSeriesGenerator(SeriesGenerator):
    def generate(self, length: int) -> List[int]:
        return list(range(length))


class ReversedSeriesGenerator(SeriesGenerator):
    def generate(self, length: int) -> List[int]:
        return list(reversed(range(length)))


class LengthsSeriesGenerator(SeriesGenerator):
    def generate(self, length: int) -> List[int]:
        if length < 1:
            raise ValueError("Lengths of series must be positive.")
        values = [10]
        base = 10
        while values[-1] < length:
            values.append(values[-1] + base)
            if values[-1] == base * 10:
                base *= 10

        if values[-1] > length:
            values[-1] = length
        return values


def generate_random_list(length: int) -> List[int]:
    return [randint(0, int(1e6)) for _ in range(length)]


def generate_ordered_list(length: int) -> List[int]:
    return list(range(length))


def generate_reversed_list(length: int) -> List[int]:
    return list(reversed(range(length)))


def bubble_sort(values: List[Any]) -> None:
    length = len(values)
    for _ in range(length):
        for index in range(length - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


def partition(values: List[Any], low: int, high: int) -> int:
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


def quick_sort(values: List[Any]) -> None:
    def quick_sort_help(left: int, right: int) -> None:
        if left < right:
            index = partition(values, left, right)
            quick_sort_help(left, index - 1)
            quick_sort_help(index + 1, right)

    quick_sort_help(0, len(values) - 1)


def extract_function_duration(stats: pstats.Stats, function: Callable):
    for key, value in stats.stats.items():
        if function.__name__ in key:
            return value[3] / value[0]


def sorting_duration(algorithm: Callable[[List[Any]], None], values: List[Any]) -> float:
    profiler = cProfile.Profile()
    profiler.enable()
    algorithm(values)
    profiler.disable()
    stats = pstats.Stats(profiler)
    return extract_function_duration(stats, algorithm)


def generate_lengths(max_length: int) -> List[int]:
    if max_length < 100:
        raise ValueError("Lengths of series must be positive.")
    values = [100]
    base = 100
    while values[-1] < max_length:
        values.append(values[-1] + base)
        if values[-1] == base * 10:
            base *= 10

    if values[-1] > max_length:
        values[-1] = max_length
    return values


ORDERED = 'ordered'
RANDOM = 'random'
REVERSED = 'reversed'


def save_durations(algorithm: Callable[[List[Any]], None], durations: Dict[str, Dict[int, float]]):
    filename = f'{algorithm.__name__}.json'
    if not os.path.exists('results'):
        os.mkdir('results')
    with open(os.path.join('results', filename), 'w') as f:
        json.dump(durations, f, indent=4, sort_keys=True)


def simulate_sorting(algorithm: Callable[[List[Any]], None], max_length) -> Dict[str, Dict[int, float]]:
    lengths = generate_lengths(max_length)
    durations = {ORDERED: {}, RANDOM: {}, REVERSED: {}}

    for length in lengths:
        durations[ORDERED][length] = sorting_duration(algorithm, generate_ordered_list(length))
        durations[RANDOM][length] = sorting_duration(algorithm, generate_ordered_list(length))
        durations[REVERSED][length] = sorting_duration(algorithm, generate_ordered_list(length))
    save_durations(algorithm, durations)

    return durations


if __name__ == '__main__':
    algorithm = bubble_sort
    # print(simulate_sorting(algorithm, 4000))
    print(generate_lengths(1700))
