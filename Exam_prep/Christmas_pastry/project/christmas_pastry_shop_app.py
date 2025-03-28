from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        valid_types = {"Gingerbread": Gingerbread, "Stolen": Stolen}

        if any(d for d in self.delicacies if d.name == name):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in valid_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy_class = valid_types[type_delicacy]
        self.delicacies.append(delicacy_class(name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        valid_types = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

        if any(b for b in self.booths if b.booth_number == booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in valid_types:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth_class = valid_types[type_booth]
        self.booths.append(booth_class(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)

        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)

        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy) # Maybe delete the delicacy from the self.delicacies ?
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(b for b in self.booths if b.booth_number == booth_number)
        sum_for_all_delicacies = sum(x.price for x in booth.delicacy_orders)
        bill = booth.price_for_reservation + sum_for_all_delicacies
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        result = f"Booth {booth_number}:\nBill: {bill:.2f}lv."
        return result

    def get_income(self):
        return f"Income: {self.income:.2f}lv."