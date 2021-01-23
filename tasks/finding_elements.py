from typing import List


def find_largest_element(values: List[int]) -> int:
    largest = 0
    for elem in values:
        if elem > largest:
            largest = elem
    return largest


# def find_largest_element(values: List[int]) -> int:
#     return sorted(values)[-2]


def find_second_largest_element(values: List[int]) -> int:
    largest = 0
    second_largest = 0
    for elem in values:
        if elem > largest:
            second_largest = largest
            largest = elem
        elif second_largest < elem < largest:
            second_largest = elem
    return second_largest


def find_ten_largest_element(values: List[int]) -> int:
    pass


def find_kth_largest_element(values: List[int]) -> int:
    pass


if __name__ == '__main__':
    values = [9, 2, 1, 100, 4, 12, 32]
    print(f'largest in {values} -> {find_largest_element(values)}')
    print(f'second largest in {values} -> {find_second_largest_element(values)}')
