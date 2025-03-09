from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.clients.base_client import BaseClient
from project.plants.base_plant import BasePlant
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income: float = 0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type == "Flower":
            self.plants.append(Flower(plant_name, plant_price, plant_water_needed, plant_extra_data))
        elif plant_type == "LeafPlant":
            self.plants.append(LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data))
        else:
            raise ValueError("Unknown plant type!")
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in ["RegularClient", "BusinessClient"]:
            raise ValueError("Unknown client type!")
        elif [x.phone_number for x in self.clients if x.phone_number == client_phone_number]:
            raise ValueError("This phone number has been used!")
        elif client_type == "RegularClient":
            self.clients.append(RegularClient(client_name, client_phone_number))
        elif client_type == "BusinessClient":
            self.clients.append(BusinessClient(client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((x for x in self.clients if x.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")
        plants = [x for x in self.plants if x.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")
        if len(plants) < plant_quantity:
            return "Not enough plant quantity."
        price = 0
        for i in range(plant_quantity):
            current_plant = next((x for x in self.plants if x.name == plant_name), None)
            price += current_plant.price
            self.plants.remove(current_plant)
        total = price - (price * client.discount / 100)
        self.income += total
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {total:.2f}"

    def remove_plant(self, plant_name: str):
        plant = next((x for x in self.plants if x.name == plant_name), None)
        if plant is None:
            return "No such plant name."
        result = plant.plant_details()
        self.plants.remove(plant)
        return f"Removed {result}"

    def remove_clients(self):
        count = 0
        for client in reversed(self.clients):
            if client.total_orders == 0:
                self.clients.remove(client)
                count += 1
        return f"{count} client/s removed."

    def shop_report(self):
        plants = {}
        for plant in self.plants:
            if plant.name not in plants:
                plants[plant.name] = 0
            plants[plant.name] += 1
        sorted_plants = sorted(plants.items(), key=lambda x: (-x[1], x[0]))
        sorted_clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))
        count_of_all_orders = sum(x.total_orders for x in sorted_clients)
        result = ["~Flower Shop Report~", f"Income: {self.income:.2f}",
                  f"Count of orders: {count_of_all_orders}", f"~~Unsold plants: {len(self.plants)}~~",]
        for plant_name, count in sorted_plants:
            result.append(f"{plant_name}: {count}")
        result.append(f"~~Clients number: {len(sorted_clients)}~~")
        for client in sorted_clients:
            result.append(client.client_details())
        return "\n".join(result)