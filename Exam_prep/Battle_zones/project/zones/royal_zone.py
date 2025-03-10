from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=10)
        self.type = "Royal"

    def zone_info(self):
        pirate_ships_count = sum(isinstance(obj, PirateBattleship) for obj in self.ships)
        result = ["@Royal Zone Statistics@", f"Code: {self.code}; Volume: {self.volume}",
                  f"Battleships currently in the Royal Zone: {len(self.ships)}, {pirate_ships_count} out of them are Pirate Battleships.",
                  ]
        if self.ships:
            result.append(f"#{', '.join(self.get_ships())}#")
        return '\n'.join(result)
