from project.band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.skills_available = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]