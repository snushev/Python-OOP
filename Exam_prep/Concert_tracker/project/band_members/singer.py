from project.band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.skills_available = ["sing high pitch notes", "sing low pitch notes"]