from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def update_discount(self):
        if self.total_orders >= 1:
            self.discount = 0.05 #percent