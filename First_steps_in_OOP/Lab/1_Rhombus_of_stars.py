n = int(input())

def print_spaces(spaces, stars):
    result = ' ' * spaces + '* ' * stars
    print(result[:-1])

def print_bottom(n):
    for row in range(1, n):
        print_spaces(row, n - row)


def print_top(n):
    for row in range(1, n + 1):
        print_spaces(n - row, row)


def print_rhombus(n):
    print_top(n)
    print_bottom(n)

print_rhombus(n)