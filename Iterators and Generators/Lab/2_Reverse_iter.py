class reverse_iter:
    def __init__(self, iterable: iter):
        self.iterable = iterable
        self.temp = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.temp -= 1
        if self.temp < 0:
            raise StopIteration
        return self.iterable[self.temp]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
