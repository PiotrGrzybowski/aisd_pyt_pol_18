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


def simulate(algorithm: SoringAlgorithm, max_length: int):
    f"""
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
    pass

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    algorithm = BubbleSortSmart()
    algorithm.sort(values)
    print(values)
    print(algorithm.comparisons)
