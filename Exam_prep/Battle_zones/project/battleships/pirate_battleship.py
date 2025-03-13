from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    SHOOT = 10

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=80)
        self.type = "Pirate"

    def attack(self):
        self.ammunition = max(self.ammunition - self.SHOOT, 0)
