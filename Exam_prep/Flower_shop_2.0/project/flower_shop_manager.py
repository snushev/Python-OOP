from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income: float = 0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    @staticmethod
    def _find_client_by_phone(lst, number):
        return next((p for p in lst if p.phone_number == number), None)

    @staticmethod
    def _find_flower_by_name(lst, name):
        return [f for f in lst if f.name == name]

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        valid_types = {"Flower": Flower,
                       "LeafPlant": LeafPlant}

        if plant_type not in valid_types:
            raise ValueError("Unknown plant type!")

        plant_class = valid_types[plant_type]
        self.plants.append(plant_class(plant_name, plant_price, plant_water_needed, plant_extra_data))
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        valid_types = {"RegularClient": RegularClient,
                       "BusinessClient": BusinessClient}

        if client_type not in valid_types:
            raise ValueError("Unknown client type!")

        if self._find_client_by_phone(self.clients, client_phone_number):
            raise ValueError("This phone number has been used!")

        client_class = valid_types[client_type]
        self.clients.append(client_class(client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client: BaseClient = self._find_client_by_phone(self.clients, client_phone_number)
        if not client:
            raise ValueError("Client not found!")
        plants: list[BasePlant] = self._find_flower_by_name(self.plants, plant_name)
        if not plants:
            raise ValueError("Plants not found!")
        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        price = 0

        for i in range(plant_quantity):
            current_plant = next((x for x in self.plants if x.name == plant_name), None)
            price += current_plant.price
            self.plants.remove(current_plant)

        total = price - price * client.discount
        self.income += total
        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {total:.2f}"

    def remove_plant(self, plant_name: str):
        plants:list[BasePlant] = self._find_flower_by_name(self.plants, plant_name)
        if not plants:
            return "No such plant name."
        plant = plants[0]
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        count = 0
        for client in reversed(self.clients):
            if client.total_orders == 0:
                self.clients.remove(client)
                count += 1
        return f"{count} client/s removed."

    def shop_report(self):
        count_plants = {}
        for plant in self.plants:
            if plant.name not in count_plants:
                count_plants[plant.name] = 0
            count_plants[plant.name] += 1

        sorted_plants = sorted(count_plants.items(), key=lambda x: (-x[1], x[0]))
        sorted_clients = sorted(self.clients, key= lambda x: (-x.total_orders, x.phone_number))
        count_of_orders = sum([x.total_orders for x in self.clients])
        #o	Format the income to the second decimal place.
        result = ["~Flower Shop Report~", f"Income: {self.income:.2f}", f"Count of orders: {count_of_orders}", f"~~Unsold plants: {len(self.plants)}~~"]
        for plant, count in sorted_plants:
            result.append(f"{plant}: {count}")
        result.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted_clients:
            result.append(client.client_details())

        return '\n'.join(result)
