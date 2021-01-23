def sort(values):
    def sort_help(low, high):
        print(f'sorting here from {low} to {high}')

    sort_help(0, len(values) - 1)


if __name__ == '__main__':
    values = [5, 4, 3, 5, 5, 5, 5, 5, 5]
    sort(values)
