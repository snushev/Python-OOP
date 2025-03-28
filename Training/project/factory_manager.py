from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            product = Chair(model, price)
        elif product_type == "HobbyHorse":
            product = HobbyHorse(model, price)
        else:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type == "FurnitureStore":
            store = FurnitureStore(name, location)
        elif store_type == "ToyStore":
            store = ToyStore(name, location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        # Check capacity
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        valid_products = []
        for product in products:
            if isinstance(store, FurnitureStore) and product.sub_type == "Furniture":
                valid_products.append(product)
            elif isinstance(store, ToyStore) and product.sub_type == "Toys":
                valid_products.append(product)

        # Преместена проверка извън цикъла
        if not valid_products:
            return "Products do not match in type. Nothing sold."

        # Process the sale
        total_price = 0.0
        for product in valid_products:
            store.products.append(product)
            self.products.remove(product)
            total_price += product.price

        store.capacity -= len(valid_products)
        self.income += total_price

        return f"Store {store.name} successfully purchased {len(valid_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        matching_products = [p for p in self.products if p.model == product_model]

        for product in matching_products:
            product.discount()

        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        stats = []
        stats.append(f"Factory: {self.name}")
        stats.append(f"Income: {self.income:.2f}")
        stats.append("***Products Statistics***")

        # Products info
        stats.append(
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}")

        # Group products by model
        model_counts = {}
        for product in self.products:
            if product.model not in model_counts:
                model_counts[product.model] = 0
            model_counts[product.model] += 1

        # Add sorted models
        for model in sorted(model_counts.keys()):
            stats.append(f"{model}: {model_counts[model]}")

        # Stores info
        stats.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            stats.append(store.name)

        return "\n".join(stats)