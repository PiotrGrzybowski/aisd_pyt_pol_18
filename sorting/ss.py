from typing import List


def bubble_sort(values: List) -> None:
    for n in range(len(values)):
        for i in range(len(values) - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]


if __name__ == '__main__':
    values = [9, 22, 1, 0, 54, 212]
    bubble_sort(values)
    print(values)
