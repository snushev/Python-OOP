from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        valid_items = {"Chair": Chair,
                       "HobbyHorse": HobbyHorse}

        if product_type not in valid_items:
            raise Exception("Invalid product type!")
        product_class = valid_items[product_type]
        current_item = product_class(model, price)
        self.products.append(current_item)
        return f"A product of sub-type {current_item.sub_type} was produced."     ######

    def register_new_store(self, store_type: str, name: str, location: str):
        valid_stores = {'FurnitureStore': FurnitureStore,
                        'ToyStore': ToyStore}
        if store_type not in valid_stores:
            raise Exception(f"{store_type} is an invalid type of store!")

        store_class = valid_stores[store_type]
        self.stores.append(store_class(name, location))
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        searched_type = ""
        num_of_purchased_products = 0

        if store.__class__.__name__ == "FurnitureStore":
            searched_type = "Furniture"
        elif store.__class__.__name__ == "ToyStore":
            searched_type = "Toys"

        for product in products:
            if product.sub_type == searched_type:
                num_of_purchased_products += 1
                self.products.remove(product)
                store.products.append(product)
                store.capacity -= 1
                self.income += product.price

        if num_of_purchased_products > 0:
            return f"Store {store.name} successfully purchased {num_of_purchased_products} items."

        return "Products do not match in type. Nothing sold."
        # if store.capacity < len(products):
        #     return f"Store {store.name} has no capacity for this purchase."
        # furniture_items = [x for x in products if x.sub_type == "Furniture"]
        # toys_items = [x for x in products if x.sub_type == "Toys"]
        #
        # store_type = store.store_type
        # if store_type == "FurnitureStore" and furniture_items:
        #     purchased_products = 0
        #     for item in furniture_items:
        #         store.products.append(item)
        #         self.products.remove(item)
        #         store.capacity -= 1
        #         self.income += item.price
        #         purchased_products += 1
        #     return f"Store {store.name} successfully purchased {purchased_products} items."
        #
        # if store_type == "ToyStore" and toys_items:
        #     purchased_products = 0
        #     for item in toys_items:
        #         store.products.append(item)
        #         self.products.remove(item)
        #         store.capacity -= 1
        #         self.income += item.price
        #         purchased_products += 1
        #     return f"Store {store.name} successfully purchased {purchased_products} items."
        #
        # return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        counter = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                counter += 1
        return f"Discount applied to {counter} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        products = {}
        for product in self.products:
            if product.model not in products:
                products[product.model] = 0
            products[product.model] += 1
        result = [f"Factory: {self.name}", f"Income: {self.income:.2f}", "***Products Statistics***",
                  f"Unsold Products: {len(self.products)}. Total net price: {sum(x.price for x in self.products):.2f}"]
        sorted_products = sorted(products.items(), key=lambda x: x[0])
        for product, count in sorted_products:
            result.append(f"{product}: {count}")
        result.append(f"***Partner Stores: {len(self.stores)}***")
        sorted_stores = sorted(self.stores, key=lambda x: x.name)
        for store in sorted_stores:
            result.append(store.name)
        return '\n'.join(result)