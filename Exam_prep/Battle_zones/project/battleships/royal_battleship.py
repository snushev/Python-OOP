from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):

    SHOOT = 25
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=100)
        self.type = "Royal"

    def attack(self):
        self.ammunition -= self.SHOOT
        if self.ammunition < 0:
            self.ammunition = 0


