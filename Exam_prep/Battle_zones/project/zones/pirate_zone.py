from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):

    def __init__(self, code: str):
        super().__init__(code, volume=8)
        self.type = "Pirate"

    def zone_info(self):
        royal_ships_count = sum(isinstance(obj, RoyalBattleship) for obj in self.ships)
        result = ["@Pirate Zone Statistics@", f"Code: {self.code}; Volume: {self.volume}",
                  f"Battleships currently in the Pirate Zone: {len(self.ships)}, {royal_ships_count} out of them are Royal Battleships.",
                  ]
        if self.ships:
            result.append(f"#{', '.join(self.get_ships())}#")
        return '\n'.join(result)
