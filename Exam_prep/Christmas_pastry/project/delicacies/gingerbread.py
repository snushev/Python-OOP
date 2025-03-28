from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name=name, price=price, portion=200)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."