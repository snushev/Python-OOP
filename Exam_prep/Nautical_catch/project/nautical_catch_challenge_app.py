from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        valid_type = {"FreeDiver": FreeDiver,
                      "ScubaDiver": ScubaDiver}

        if diver_type not in valid_type:
            return f"{diver_type} is not allowed in our competition."
        if any(d for d in self.divers if d.name == diver_name):
            return f"{diver_name} is already a participant."

        diver_class = valid_type[diver_type]
        self.divers.append(diver_class(diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        valid_type = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

        if fish_type not in valid_type:
            return f"{fish_type} is forbidden for chasing in our competition."

        if any(f for f in self.fish_list if f.name == fish_name):
            return f"{fish_name} is already permitted."

        fish_class = valid_type[fish_type]
        self.fish_list.append(fish_class(fish_name, points))

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."


        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

        elif is_lucky:
            diver.hit(fish)

            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

        elif not is_lucky:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

    def health_recovery(self):
        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
            diver.renew_oxy()
            count += 1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        result = [f"**{diver_name} Catch Report**"]
        diver = next((d for d in self.divers if d.name == diver_name), None)
        for fish in diver.catch:
            result.append(fish.fish_details())
        return '\n'.join(result)

    def competition_statistics(self):
        divers = [d for d in self.divers if d.oxygen_level > 0]
        sorted_divers = sorted(divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        for diver in sorted_divers:
            result.append(diver.__str__())
        return '\n'.join(result)