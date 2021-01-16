class A:
    def __init__(self, size: int) -> None:
        self.size = size

    def __str__(self):
        return f'A - {self.size}'

    def __add__(self, other):
        pass

    def __len__(self):
        return self.size




if __name__ == '__main__':
    a = A(5)
    print(a.__str__())
    l = [1, 2, 3]
    print(len(l))
    print(l.__len__())

    print(len(a))


