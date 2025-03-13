from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def animal_sound(self):
        pass

class Dog(Animal):
    def animal_sound(self):
        return 'woof-woof'

class Cat(Animal):
    def animal_sound(self):
        return'meow'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.animal_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
