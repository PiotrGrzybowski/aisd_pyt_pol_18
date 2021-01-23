import json

from abc import ABC, abstractmethod
from typing import List
from tqdm import tqdm

from sorting.algorithms import generate_reversed_list, generate_ordered_list, generate_random_list

ORDERED = 'ordered'
REVERSED = 'reversed'
RANDOM = 'random'


class SortingAlgorithm(ABC):
    def __init__(self):
        self.comparisons = 0

    @abstractmethod
    def sort(self, values: List) -> None:
        pass

    def gt(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 > value_2


class BubbleSort(SortingAlgorithm):
    def sort(self, values: List) -> None:
        self.comparisons = 0
        for n in range(len(values)):
            for i in range(len(values) - 1 - n):
                if self.gt(values[i], values[i + 1]):
                    values[i], values[i + 1] = values[i + 1], values[i]


class BubbleSortSmart(SortingAlgorithm):
    def sort(self, values: List) -> None:
        self.comparisons = 0
        n = 0
        swap_occurred = True

        while n < len(values) and swap_occurred:
            swap_occurred = False
            for i in range(len(values) - 1 - n):
                if self.gt(values[i], values[i + 1]):
                    values[i], values[i + 1] = values[i + 1], values[i]
                    swap_occurred = True

            n += 1


class InsertionSort(SortingAlgorithm):
    def sort(self, values: List) -> None:
        self.comparisons = 0
        for i in range(1, len(values)):
            current_value = values[i]
            current_position = i
            while current_position > 0 and self.gt(values[current_position - 1], current_value):
                values[current_position] = values[current_position - 1]
                current_position -= 1
            values[current_position] = current_value


class QuickSort(SortingAlgorithm):
    def partition(self, values: List, low: int, high: int) -> int:
        pivot = values[high]
        j = low - 1

        for i in range(low, high):
            if values[i] < pivot:
                self.comparisons += 1
                j += 1
                values[i], values[j] = values[j], values[i]
        j += 1
        values[j], values[high] = values[high], values[j]
        return j

    def sort(self, values: List) -> None:
        self.comparisons = 0

        def sort_help(low: int, high: int) -> None:
            if low < high:
                index = self.partition(values, low, high)
                sort_help(low, index - 1)
                sort_help(index + 1, high)

        sort_help(0, len(values) - 1)


def simulate(algorithm: SortingAlgorithm, max_length: int):
    """
    Przyjmuje algorytm, za pomocą którego zostanie wykonane sortowanie list:
    - Uporządkowanej,
    - Odwrotnie uporządkowanej
    - Losowo uporządkowanej
     O długościach od 1 do max_length.

     {
        'ordered': {1: x, 2: y, ..., 1000: z},
        'reversed': {1: x, 2: y, ..., 1000: z},
        'random': {1: x, 2: y, ..., 1000: z}
     }
     
     Kroki do wykonania:
     - Utwórz słownik o wyżej napisanym formacie
     - Pętla for lenght in range(1, max_length + 1)
        * wygenerować trzy listy, za pomocą pomocniczych funkcji (random, ordered, reversed) dla atualnie rozważanej długości listy
        * dla każdej z nich wykonaj sortowanie algorytmem przekazanym jako argument funkcji
        * do słownika wynikowego dodaj w odpowienim miejscu wynik będący liczbą porównań wykonanych podczas sortowania
    
     - Zapisz słownikik wynikowy do pliku json o nazwie: f'{algorithm.__class__.__name__}_{max_length}.json'
    """
    result = {
        ORDERED: {},
        REVERSED: {},
        RANDOM: {}
    }

    for length in tqdm(range(1, max_length + 1)):
        ordered_list = generate_ordered_list(length)
        algorithm.sort(ordered_list)
        result[ORDERED][length] = algorithm.comparisons

        reversed_list = generate_reversed_list(length)
        algorithm.sort(reversed_list)
        result[REVERSED][length] = algorithm.comparisons

        random_list = generate_random_list(length, 0, max_length)
        algorithm.sort(random_list)
        result[RANDOM][length] = algorithm.comparisons

    filename = f'{algorithm.__class__.__name__}_{max_length}.json'
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    algorithm = QuickSort()
    # simulate(algorithm, 1000)

    values = [8, 6, 7, 0, 2, 4, 1, 5]
    algorithm.sort(values)
    print(values)
    # values = generate_reversed_list(10)
    # print(values)
    # InsertionSort().sort(values)
    # print(values)
