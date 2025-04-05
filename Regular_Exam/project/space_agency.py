from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    @staticmethod
    def _find_object_by_id(lst, id_):
        return next((obj for obj in lst if obj.id_number == id_), None)

    @staticmethod
    def _find_object_by_name(lst, name):
        return next((obj for obj in lst if obj.name == name), None)

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        valid_types = {"EngineerAstronaut": EngineerAstronaut, "ScientistAstronaut": ScientistAstronaut}

        if astronaut_type not in valid_types:
            raise ValueError("Invalid astronaut type!")

        if self._find_object_by_id(self.astronauts, astronaut_id_number):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        astronaut_class = valid_types[astronaut_type]
        self.astronauts.append(astronaut_class(astronaut_id_number, astronaut_salary))
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        valid_types = {"ResearchStation": ResearchStation, "MaintenanceStation": MaintenanceStation}

        if station_type not in valid_types:
            raise ValueError("Invalid station type!")

        if self._find_object_by_name(self.stations, station_name):
            raise ValueError(f"{station_name} has been already added!")

        station_class = valid_types[station_type]
        self.stations.append(station_class(station_name))
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station: BaseStation = self._find_object_by_name(self.stations, station_name)
        if not station:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut: BaseAstronaut = next((a for a in self.astronauts if type(a).__name__ == astronaut_type), None)
        if not astronaut:
            raise ValueError("No available astronauts of the type!")

        if station.capacity == 0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for astronaut in station.astronauts:
            for _ in range(sessions_number):
                astronaut.train()

        total_stamina = sum([x.stamina for x in station.astronauts])

        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astronaut: BaseAstronaut = self._find_object_by_id(station.astronauts, astronaut_id_number)
        if not astronaut or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda x: (-len(x.astronauts), x.name))
        total_available_capacity = sum([x.capacity for x in sorted_stations])

        result = ["*Space Agency Up-to-Date Report*", f"Total number of available astronauts: {len(self.astronauts)}",
        f"**Stations count: {len(self.stations)}; Total available capacity: {total_available_capacity}**"]

        for station in sorted_stations:
            result.append(station.status())

        return '\n'.join(result)