from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        valid_types = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
        if musician_type not in valid_types:
            raise ValueError("Invalid musician type!")
        if any(x for x in self.musicians if x.name == name):
            raise Exception(f"{name} is already a musician!")
        musician_class = valid_types[musician_type]
        self.musicians.append(musician_class(name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(x for x in self.bands if x.name == name):
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next((x for x in self.concerts if x.place == place), None)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        band = next((b for b in self.bands if b.name == band_name), None)

        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        musician = next((m for m in band.members if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next((c for c in self.concerts if c.place == concert_place), None)
        band = next((b for b in self.bands if b.name == band_name), None)

        singers = [x for x in band.members if x.__class__.__name__ == "Singer"]
        drummers = [x for x in band.members if x.__class__.__name__ == "Drummer"]
        guitarists = [x for x in band.members if x.__class__.__name__ == "Guitarist"]



        if not(singers or drummers or guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for singer in singers:
                if "sing high pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for drummer in drummers:
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for guitarist in guitarists:
                if "play rock" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == "Metal":
            for singer in singers:
                if "sing low pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for drummer in drummers:
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for guitarist in guitarists:
                if "play metal" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == "Jazz":
            for singer in singers:
                if "sing high pitch notes and sing low pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for drummer in drummers:
                if "play the drums with drum brushes" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for guitarist in guitarists:
                if "play jazz" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."