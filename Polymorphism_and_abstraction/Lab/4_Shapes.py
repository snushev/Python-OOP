from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):

    def calculate_area(self):
        return math.pi * self.__radius * self.__radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def __init__(self, radius):
        self.__radius = radius

class Rectangle(Shape):

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
