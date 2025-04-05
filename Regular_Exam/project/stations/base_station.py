from abc import ABC, abstractmethod

class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        for char in value:
            if not (char.isalnum() or char == '-'):
                raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salaries = 0
        for astronauts in self.astronauts:
            total_salaries += astronauts.salary

        return f"{total_salaries:.2f}"

    def status(self):
        result = [f"Station name: {self.name}"]
        if self.astronauts:
            sorted_astronauts = sorted(self.astronauts, key=lambda a: a.id_number)
            names = [x.id_number for x in sorted_astronauts]
            result.append(f"Astronauts: {' #'.join(names)}")
        else:
            result.append('Astronauts: N/A')
        result.append(f"Total salaries: {self.calculate_total_salaries()}")

        return '; '.join(result)

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass