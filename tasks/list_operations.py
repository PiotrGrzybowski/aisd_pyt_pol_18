from typing import List


def maximum(values: List[int]) -> int:
    result = values[0]
    for value in values:
        if value > result:
            result = value

    return result


if __name__ == '__main__':
    print(maximum([8, 2, 1, 9]))
    