import abc
import random
import time
import tqdm
from typing import Callable, Union
import numpy as np
import os
import pathlib
import logging

LOGGER = logging.getLogger('Experiment')
logging.basicConfig(level=logging.INFO)


def bubble_sort(values: list) -> None:
    for _ in range(len(values)):
        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


def quick_sort(values: list) -> None:
    def partition(values: list, low: int, high: int) -> int:
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

    def quick_sort_help(left: int, right: int) -> None:
        if left < right:
            index = partition(values, left, right)
            quick_sort_help(left, index - 1)
            quick_sort_help(index + 1, right)

    quick_sort_help(0, len(values) - 1)


class InputMaker(abc.ABC):
    @abc.abstractmethod
    def make(self, *args, **kwargs):
        pass

    @property
    def name(self) -> str:
        return self.__class__.__name__


class RandomListMaker(InputMaker):
    def make(self, size: int) -> list[int]:
        return [random.randint(0, int(1e6)) for _ in range(size)]


class OrderedListMaker(InputMaker):
    def make(self, size: int) -> list[int]:
        return list(range(size))


class ReversedListMaker(InputMaker):
    def make(self, size: int) -> list[int]:
        return list(reversed(range(size)))


class Timer:
    def __init__(self) -> None:
        self.times = []
        self.begin = None
        self.end = None

    def start(self):
        self.begin = time.perf_counter_ns()

    def stop(self):
        self.update(time.perf_counter_ns() - self.begin)

    def update(self, value: float) -> None:
        self.times.append(value)

    def time(self):
        return sum(self.times) / len(self.times) / 1e9

    def status(self):
        if len(self.times) < 2:
            print('ko')
        else:
            delta = abs(sum(self.times[:-1]) / len(self.times[:-1]) / 1e9 - sum(self.times) / len(self.times) / 1e9)
            print(delta, self.time(), delta / self.time())

    def is_stable(self):
        if len(self.times) < 3:
            return False
        else:
            delta = abs(sum(self.times[:-1]) / len(self.times[:-1]) / 1e9 - sum(self.times) / len(self.times) / 1e9)
            return delta / self.time() < 0.01

    def reset(self):
        self.times = []


class SortingExperiment:
    def __init__(self, algorithm: Callable[[list], None], input_maker: InputMaker, timer: Timer):
        self.algorithm = algorithm
        self.input_maker = input_maker
        self.timer = timer
        self.durations = {}

    def run(self, max_size: int):
        for size in tqdm.tqdm(range(100, max_size, 100)):
            while not self.timer.is_stable():
                data = self.input_maker.make(size)
                self.timer.start()
                self.algorithm(data)
                self.timer.stop()
            self.durations[size] = self.timer.time()
            self.timer.reset()


class SortingExperimentSerializer:
    def __init__(self, path: pathlib.Path):
        self.path = path

    def load(self, algorithm, input_maker):
        filename = f'{self.algorithm_name(algorithm)}_{input_maker.name}.json'
        with open(self.path.joinpath(filename)) as f:
            data = json.load(f)
        result = {int(size): duration for size, duration in data.items()}
        return list(result.keys()), list(result.values())

    def dump(self, experiment):
        filename = f'{self.algorithm_name(experiment.algorithm)}_{experiment.input_maker.name}.json'
        if not self.path.exists():
            os.makedirs(self.path)
        with open(self.path.joinpath(filename), 'w') as f:
            json.dump(experiment.durations, f, indent=4, sort_keys=True)

    @staticmethod
    def algorithm_name(algorithm) -> str:
        return ''.join([part.capitalize() for part in algorithm.__name__.split('_')])


def run_experiments(algorithm: Callable[[list], None], input_makers: list[InputMaker], max_size: int):
    timer = Timer()
    serializer = SortingExperimentSerializer(pathlib.Path('results'))
    for input_maker in input_makers:
        LOGGER.info(f"{algorithm.__name__} {input_maker.name}")
        experiment = SortingExperiment(algorithm, input_maker, timer)
        experiment.run(max_size)
        serializer.dump(experiment)


def visualize(algorithms, input_makers):
    figure = go.Figure()
    for algorithm in algorithms:
        for input_maker in input_makers:
            sizes, durations = serializer.load(algorithm, input_maker)
            name = f'{SortingExperimentSerializer.algorithm_name(algorithm)} {input_maker.name}'
            figure.add_trace(go.Scatter(x=sizes, y=durations, mode='lines+markers', name=name))

    figure.show()
import os
import json

import plotly.graph_objects as go

if __name__ == '__main__':
    ordered_list_maker = OrderedListMaker()
    reversed_list_maker = ReversedListMaker()
    random_list_maker = RandomListMaker()

    serializer = SortingExperimentSerializer(pathlib.Path('results'))
    data_makers = [RandomListMaker(), OrderedListMaker(), ReversedListMaker()]
    # run_experiments(quick_sort, data_makers, 10001)
    visualize([bubble_sort, quick_sort], [reversed_list_maker])
