import json

from abc import ABC, abstractmethod
from typing import List

from sorting.algorithms import generate_ordered_list, generate_reversed_list, generate_random_list

ORDERED = 'ordered'
REVERSED = 'reversed'
RANDOM = 'random'


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
        self.comparisons = 0
        for n in range(len(values)):
            for i in range(len(values) - 1 - n):
                if self.gt(values[i], values[i + 1]):
                    values[i], values[i + 1] = values[i + 1], values[i]


class BubbleSortSmart(SoringAlgorithm):
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


def simulate(algorithm: SoringAlgorithm, max_length: int):
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

    for length in range(1, max_length + 1):
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
    algorithm = BubbleSortSmart()
    simulate(algorithm, 100)
