class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_to_arabic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Обхождаме римското число отзад напред
        for char in reversed(value):
            value = roman_to_arabic[char]
            if value < prev_value:
                total -= value  # Изваждаме, ако текущата стойност е по-малка от предишната (напр. IV = 4)
            else:
                total += value  # Добавяме, ако текущата стойност е по-голяма или равна
            prev_value = value

        return cls(total)


    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
