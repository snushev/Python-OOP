from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    @staticmethod
    def find_object(lst, name):
        return next((obj for obj in lst if obj.name == name), None)

    def add_player(self, *players):
        added_names = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_names.append(player.name)
        return f"Successfully added: {', '.join(added_names)}" if added_names else ""

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_object(self.players, player_name)
        if not player or sustenance_type not in ("Food", "Drink"):
            return

        for i in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                supply = self.supplies.pop(i)  # Премахваме я от списъка
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")


        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player.stamina = min(100, player.stamina + supply.energy)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.find_object(self.players, first_player_name)
        player2 = self.find_object(self.players, second_player_name)

        messages = []
        for player in [player1, player2]:
            if player.stamina == 0:
                messages.append(f"Player {player.name} does not have enough stamina.")
        if messages:
            return "\n".join(messages)

        attacker, defender = (player1, player2) if player1.stamina < player2.stamina else (player2, player1)

        defender.stamina -= attacker.stamina / 2
        if defender.stamina <= 0:
            defender.stamina = 0
            return f"Winner: {attacker.name}"

        attacker.stamina -= defender.stamina / 2
        if attacker.stamina <= 0:
            attacker.stamina = 0
            return f"Winner: {defender.name}"

        return f"Winner: {player1.name if player1.stamina > player2.stamina else player2.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")
        for supply in self.supplies:
            result.append(f"{type(supply).__name__}: {supply.name}, {supply.energy}")
        return '\n'.join(result)