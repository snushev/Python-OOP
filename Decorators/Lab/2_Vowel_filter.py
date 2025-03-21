def vowel_filter(function):

    def wrapper():
        vowels = ["a", "e", "o", "y", "u", "i"]
        result = [x for x in function() if x in vowels]
        return result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
