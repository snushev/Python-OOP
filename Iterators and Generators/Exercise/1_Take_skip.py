class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.count:
            raise StopIteration
        return self.index * self.step

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
