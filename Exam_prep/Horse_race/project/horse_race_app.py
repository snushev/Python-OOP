from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    @staticmethod
    def find_object_by_name(lst, name):
        return next((obj for obj in lst if obj.name == name), None)

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_types = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
        if horse_type in valid_types:
            horse = self.find_object_by_name(self.horses, horse_name)
            if horse:
                raise Exception(f"Horse {horse_name} has been already added!")
            horse_class = valid_types[horse_type]
            self.horses.append(horse_class(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.find_object_by_name(self.jockeys, jockey_name)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = next((r for r in self.horse_races if r.race_type == race_type),None)
        if race:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_object_by_name(self.jockeys, jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horses = [h for h in self.horses if h.__class__.__name__ == horse_type if not h.is_taken]
        if not horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horses[-1]
        horses[-1].is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horses[-1].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.find_object_by_name(self.jockeys, jockey_name)
        horse_race = next((h for h in self.horse_races if h.race_type == race_type), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = next((h for h in self.horse_races if h.race_type == race_type), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        highest_speed = 0
        jockey_name = ""
        horse_name = ""
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name
        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."