class Flower:
    def __init__(self, name, water_requirements, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        current = ""
        if not self.is_happy:
            current = " not"
        return f"{self.name} is{current} happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
