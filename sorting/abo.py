import abc
import random
import time
from typing import Callable


def bubble_sort(values: list) -> None:
    for _ in range(len(values)):
        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


class DataMaker(abc.ABC):
    @abc.abstractmethod
    def make(self, *args, **kwargs):
        pass


class RandomListMaker(DataMaker):
    def make(self, size: int) -> list[int]:
        return [random.randint(0, int(1e6)) for _ in range(size)]


class OrderedListMaker(DataMaker):
    def make(self, size: int) -> list[int]:
        return list(range(size))


class ReversedListMaker(DataMaker):
    def make(self, size: int) -> list[int]:
        return list(reversed(range(size)))


class Timer:
    def __init__(self) -> None:
        self.times = []

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, value: float) -> None:
        self.times.append(value)

    def compute(self):
        return sum(self.times) / len(self.times) / 1e9

    def reset(self):
        self.times = []


class SortingExperiment:
    def __init__(self, algorithm: Callable[[list], None], input_generator: DataMaker, max_size: int):
        self.algorithm = algorithm
        self.input_generator = input_generator
        self.max_size = max_size
        self.result = {}

    def run(self, times: int = 1):
        metric = Timer()

        for size in range(100, self.max_size, 100):
            for _ in range(times):
                data = self.input_generator.make(size)
                start = time.perf_counter_ns()
                self.algorithm(data)
                metric.update(time.perf_counter_ns() - start)
            self.result[size] = metric.compute()
            metric.reset()

import os
import json
def save_durations(algorithm: Callable[[list], None], durations):
    filename = f'{algorithm.__name__}.json'
    if not os.path.exists('results'):
        os.mkdir('results')
    with open(os.path.join('results', filename), 'w') as f:
        json.dump(durations, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    maker = ReversedListMaker()
    e = SortingExperiment(bubble_sort, maker, 2000)
    m = e.run(5)
    save_durations(bubble_sort, e.result)
    import numpy as np
