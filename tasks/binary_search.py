def binary_search_rec(values, target, low, high):
    if high >= low:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        elif values[middle] > target:
            return binary_search_rec(values, target, low, middle - 1)
        else:
            return binary_search_rec(values, target, middle + 1, high)
    else:
        return -1


def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        middle = (low + high) // 2
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return -1


if __name__ == '__main__':
    values = [5, 12, 32, 41, 75, 88, 99, 112, 256]
    print(binary_search(values, 5))
    print(binary_search_rec(values, 5, 0, len(values)))
