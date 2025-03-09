from project.animals.animal import Mammal
from project.food import *


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += 0.1 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.4 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += 0.3 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
class Tiger(Mammal):
    COEF = 1
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"