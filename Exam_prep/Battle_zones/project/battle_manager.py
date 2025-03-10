from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        valid_zones = {"RoyalZone": RoyalZone,
                       "PirateZone": PirateZone}

        if zone_type not in valid_zones:
            raise Exception("Invalid zone type!")

        if any(zone.code == zone_code for zone in self.zones):
            raise Exception("Zone already exists!")

        zone_class = valid_zones[zone_type]
        self.zones.append(zone_class(zone_code))

        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        valid_ships = {'RoyalBattleship': RoyalBattleship,
                       'PirateBattleship': PirateBattleship}

        if ship_type not in valid_ships:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship_class = valid_ships[ship_type]
        self.ships.append(ship_class(name, health, hit_strength))

        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        # ship enters:
        if zone.type == ship.type:
            ship.is_attacking = True
        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        current_ship = next((x for x in self.ships if x.name == ship_name), None)
        if current_ship is None:
            return "No ship with this name!"

        if not current_ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(current_ship)

        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        if not (any(ship.is_attacking for ship in zone.ships) and any(not ship.is_attacking for ship in zone.ships)):
            return "Not enough participants. The battle is canceled."

        max_str = 0
        max_health = 0
        attacker: BaseBattleship = None
        defender: BaseBattleship = None

        for ship in zone.ships:
            if ship.is_attacking:
                if ship.hit_strength > max_str:
                    max_str = ship.hit_strength
                    attacker = ship
            else:
                if ship.health > max_health:
                    max_health = ship.health
                    defender = ship

        attacker.attack()
        defender.take_damage(attacker)

        if defender.health == 0:
            self.ships.remove(defender)
            zone.ships.remove(defender)
            return f"{defender.name} lost the battle and was sunk."
        if attacker.ammunition == 0:
            self.ships.remove(attacker)
            zone.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."

    def get_statistics(self):
        not_participating = [x.name for x in self.ships if x.is_available]
        sorted_zones = sorted(self.zones, key=lambda x: x.code)  ##########
        result = [f"Available Battleships: {len(not_participating)}"]
        if not_participating:
            result.append(f"#{', '.join(not_participating)}#")
        result.append("***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")
        if sorted_zones:
            for zone in sorted_zones:
                result.append(zone.zone_info())

        return '\n'.join(result)
