from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for char in value:
            if not (char.isalpha() or char.isdigit()):
                raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        valid_type = {"KneePad": KneePad, "ElbowPad": ElbowPad}
        if equipment_type not in valid_type:
            raise Exception("Invalid equipment type!")
        self.equipment.append(valid_type[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        valid_type = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}
        if team_type not in valid_type:
            raise Exception("Invalid team type!")
        if self.capacity == 0:
            return "Not enough tournament capacity."
        self.teams.append(valid_type[team_type](team_name, country, advantage))
        self.capacity -= 1
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]
        team = next((t for t in self.teams if t.name == team_name), None)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.budget -= equipment.price
        team.equipment.append(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        self.capacity += 1 #TODO
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                count += 1
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        protection1 = sum(x.protection for x in team1.equipment)
        protection2 = sum(x.protection for x in team2.equipment)

        if protection1 + team1.advantage > protection2 + team2.advantage:
            team1.win()
            return f"The winner is {team1.name}."
        elif protection1 + team1.advantage < protection2 + team2.advantage:
            team2.win()
            return f"The winner is {team2.name}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]
        for team in sorted_teams:
            result.append(team.get_statistics())
        return '\n'.join(result)