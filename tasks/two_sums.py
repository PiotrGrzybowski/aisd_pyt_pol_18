from typing import List, Tuple

from sorting.algorithms import generate_random_list


def suma_dwoch_liczb(values: List[int], target: int) -> Tuple[int, int]:
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                return i, j


def two_sum(values: List[int], target: int) -> Tuple[int, int]:
    complements = {}
    for i in range(len(values)):
        complements[values[i]] = i

    for i in range(len(values)):
        complement = target - values[i]
        if complement in complements and complements[complement] != i:
            return complements[complement], i


def two_sum_one_pass(values: List[int], target: int) -> Tuple[int, int]:
    complements = {}

    for i in range(len(values)):
        complement = target - values[i]
        if complement in complements:
            return complements[complement], i
        complements[values[i]] = i


if __name__ == '__main__':
    values = [2, 3, 5, 7, 324, 22, 14]
    values = generate_random_list(1000000, 0, 10)
    target = 338
    values.append(324)
    values.append(14)
    print(two_sum(values, target))
