from project.clients.base_client import BaseClient

class VIPClient(BaseClient):
    def __init__(self, name):
        super().__init__(name, membership_type="VIP")

###################################
    def earning_points(self, order_amount: float):
        earned_points = int(order_amount / 5)
        self.points += earned_points
        return earned_points
