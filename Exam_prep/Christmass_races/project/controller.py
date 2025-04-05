from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: list[Car] = []
        self.drivers: list[Driver] = []
        self.races: list[Race] = []

    @staticmethod
    def _find_car(collection, model):
        return next((car for car in collection if car.model == model), None)

    @staticmethod
    def _find_object_by_name(collection, name):
        return next((obj for obj in collection if obj.name == name), None)

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_types = {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar,
        }
        if car_type not in valid_types:
            return

        if self._find_car(self.cars, model):
            raise Exception(f"Car {model} is already created!")

        car_class = valid_types[car_type]
        self.cars.append(car_class(model, speed_limit))
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._find_object_by_name(self.drivers, driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._find_object_by_name(self.races, race_name):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver: Driver = self._find_object_by_name(self.drivers, driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = [c for c in self.cars if type(c).__name__ == car_type and not c.is_taken][-1]
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            driver.car.is_taken = False
            old_model = driver.car.model
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race: Race = self._find_object_by_name(self.races, race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver: Driver = self._find_object_by_name(self.drivers, driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race: Race = self._find_object_by_name(self.races, race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        arrange_by_speed = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        winners = arrange_by_speed[:3]

        result = []

        for winner in winners:
            result.append(f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.")
            winner.number_of_wins += 1

        return '\n'.join(result)