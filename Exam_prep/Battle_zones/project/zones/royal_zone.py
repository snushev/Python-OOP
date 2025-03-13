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
        all_ships = self.get_ships()
        ship_names = ', '.join([sh.name for sh in all_ships])
        if all_ships:
            result.append(f"#{ship_names}#")
        return '\n'.join(result)
