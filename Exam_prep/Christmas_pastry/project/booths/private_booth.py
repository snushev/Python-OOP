from project.booths.booth import Booth


class PrivateBooth(Booth):

    def reserve(self, number_of_people: int):
        price_per_person = 3.5
        self.price_for_reservation = price_per_person * number_of_people
        self.is_reserved = True