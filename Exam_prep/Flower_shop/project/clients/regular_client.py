from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def update_discount(self):
        self.discount = 5 if self.total_orders >= 1 else 0