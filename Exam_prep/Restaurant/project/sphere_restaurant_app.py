from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        valid_waiter = {
            "FullTimeWaiter": FullTimeWaiter,
            "HalfTimeWaiter": HalfTimeWaiter
        }

        if waiter_type not in valid_waiter:
            return f"{waiter_type} is not a recognized waiter type."
        if any(waiter.name == waiter_name for waiter in self.waiters):
            return f"{waiter_name} is already on the staff."

        waiter_class = valid_waiter[waiter_type]
        self.waiters.append(waiter_class(waiter_name, hours_worked))
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        valid_client = {
            "RegularClient": RegularClient,
            "VIPClient": VIPClient
        }

        if client_type not in valid_client:
            return f"{client_type} is not a recognized client type."
        if any(client.name == client_name for client in self.clients):
            return f"{client_name} is already a client."

        client_class = valid_client[client_type]
        self.clients.append(client_class(client_name))
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if waiter is None:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client is None:
            return f"{client_name} is not a registered client."
        return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client is not None:
            discount, points = client.apply_discount()
            return f"{client_name} received a {discount}% discount. Remaining points {points}"
        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        total_earnings = sum([x.calculate_earnings() for x in self.waiters])
        unused_points = sum([x.points for x in self.clients])
        sorted_waiters = sorted(self.waiters, key=lambda x: -x.calculate_earnings()) ######
        result = ["$$ Monthly Report $$", f"Total Earnings: ${total_earnings:.2f}", f"Total Clients Unused Points: {unused_points}",
                  f"Total Clients Count: {len(self.clients)}", f"** Waiter Details **",]

        for waiter in sorted_waiters:
            result.append(waiter.__str__())

        return '\n'.join(result)