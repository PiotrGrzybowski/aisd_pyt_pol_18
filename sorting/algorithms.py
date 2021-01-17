from typing import List


def generate_random_list(length: int, start: int, end: int) -> List[int]:
    """Zwraca listę liczb losowo uporządkowanych o długości len z zakresu
    9,4,3,111,24346,...
    """
    pass


def generate_ordered_list(length: int) -> List[int]:
    """Zwraca listę wartości uporządkowanych od 0 do lenght
    0,1,2,3,4,5...,length-1
    """
    pass


def generate_reversed_list(length: int) -> List[int]:
    """Zwraca listę wartości odwrotnie uporządkowanych od 0 do lenght
    length-1,length-2,length-3,length,...,0
    """
    pass


def bubble_sort(values: List) -> None:
    pass


if __name__ == '__main__':
    values = [8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(values)
    print(values)
