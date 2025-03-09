import math
from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.discount: float = 0 #in percentage
        self.total_orders: int = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Name must be at least two characters long!")
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        forbidden_symbol = next((x for x in value if not x.isdigit()), None)
        if forbidden_symbol:
            raise ValueError("Phone number can contain only digits!")
        self.__phone_number = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self):
        return f"Client: {self.__name}, Phone number: {self.__phone_number}, Orders count: {self.total_orders}, Discount: {math.floor(self.discount)}%"