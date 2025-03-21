def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator = fibonacci()
for i in range(6):
    print(next(generator))
