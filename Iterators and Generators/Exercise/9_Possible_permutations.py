def possible_permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            for p in possible_permutations(lst[:i] + lst[i+1:]):
                yield [lst[i]] + p