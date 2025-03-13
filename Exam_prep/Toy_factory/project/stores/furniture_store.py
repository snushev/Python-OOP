from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        result.append(self.get_estimated_profit())

        result.append("**Furniture for sale:")
        toys = {}
        for product in self.products:
            if product.sub_type == "Furniture":
                if product.model not in toys:
                    toys[product.model] = {"count": 0, "price": 0}
                toys[product.model]["count"] += 1
                toys[product.model]["price"] += product.price

        for model, info in sorted(toys.items()):
            avg_price = info["price"] / info["count"]
            result.append(f"{model}: {info['count']}pcs, average price: {avg_price:.2f}")
        return '\n'.join(result)