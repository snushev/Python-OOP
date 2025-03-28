from project.stores.base_store import BaseStore

class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        stats = []
        stats.append(f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}")
        stats.append(self.get_estimated_profit())
        stats.append("**Toys for sale:")

        # Group products by model
        model_counts = {}
        model_prices = {}
        for product in self.products:
            if product.model not in model_counts:
                model_counts[product.model] = 0
                model_prices[product.model] = 0.0
            model_counts[product.model] += 1
            model_prices[product.model] += product.price

        # Sort models and prepare output
        for model in sorted(model_counts.keys()):
            count = model_counts[model]
            avg_price = model_prices[model] / count
            stats.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return "\n".join(stats)