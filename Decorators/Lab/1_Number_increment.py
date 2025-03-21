def number_increment(numbers):

    def increase():
        result = [i + 1 for i in numbers]
        return result

    return increase()

print(number_increment([1, 2, 3]))