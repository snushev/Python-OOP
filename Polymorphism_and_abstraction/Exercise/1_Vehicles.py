from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed


    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self. fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed


    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
