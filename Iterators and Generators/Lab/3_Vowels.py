class vowels:
    def __init__(self, text: str):
        self.text = text
        self.index = -1
        self.valid = "aoeiuy"
        self.vowels = [x for x in self.text if x.lower() in self.valid]

    def __iter__(self):
        return self

    def __next__(self):

        self.index += 1
        if self.index >= len(self.vowels):
            raise StopIteration
        return self.vowels[self.index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
