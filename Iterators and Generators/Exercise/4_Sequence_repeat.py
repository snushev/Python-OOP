class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.number:
            raise StopIteration
        return self.sequence[self.index % len(self.sequence)]

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
