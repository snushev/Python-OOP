from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    def __init__(self, name):
        super().__init__(name, available_money=25_000, available_space=3000)

    def increase_money(self):
        self.available_money += 5000
