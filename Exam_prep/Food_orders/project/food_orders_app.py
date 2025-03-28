from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 1
    def __init__(self):
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []

    def register_client(self, client_phone_number: str):
        if any(x for x in self.clients_list if x.phone_number == client_phone_number):
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = [meal.details() for meal in self.menu]
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client = next((x for x in self.clients_list if x.phone_number == client_phone_number), None)
        if client is None:
            self.clients_list.append(Client(client_phone_number))
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next((m for m in self.menu if m.name == meal_name), None)
            if meal is None:
                client.shopping_cart.clear()
                client.bill = 0
                raise Exception(f"{meal} is not on the menu!")
            if quantity > meal.quantity:
                client.shopping_cart.clear()
                client.bill = 0
                raise Exception(f"Not enough quantity of {self.__class__.__name__}: {meal_name}!")
            meal = next((m for m in self.menu if m.name == meal_name), None)
            client.shopping_cart.append(meal)
            client.bill += quantity * meal.price
            meal.quantity -= quantity
        #Potential error if quantity becomes 0 after few orders of the same item
        # for meal_name, quantity in meal_names_and_quantities.items():
        #     meal = next((m for m in self.menu if m.name == meal_name), None)
        #     client.shopping_cart.append(meal)
        #     client.bill += quantity * meal.price
        #     meal.quantity -= quantity
        item_names = [i.name for i in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(item_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next((x for x in self.clients_list if x.phone_number == client_phone_number), None)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for item in client.shopping_cart:
            meal = next((m for m in self.menu if m.name == item.name), None)
            meal.quantity += item.quantity
        client.shopping_cart.clear()
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next((x for x in self.clients_list if x.phone_number == client_phone_number), None)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.shopping_cart.clear()
        result = f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was successfully paid for {client_phone_number}."
        self.receipt_id += 1
        client.bill = 0
        return result

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."