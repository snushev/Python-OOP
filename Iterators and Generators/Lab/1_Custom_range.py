class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.temp = self.start -1

    def __iter__(self):
        return self

    def __next__(self):
        self.temp += 1
        if self.temp > self.end:
            raise StopIteration
        return self.temp

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

