def read_next(*args):
    for i in args:
        for j in i:
            yield j

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

