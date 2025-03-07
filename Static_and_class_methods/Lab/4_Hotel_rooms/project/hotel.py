from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        free_rooms = [x for x in self.rooms if not x.is_taken]
        taken_rooms = [x for x in self.rooms if x.is_taken]

        return  (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(x.number) for x in free_rooms])}\n"
                f"Taken rooms: {', '.join([str(x.number) for x in taken_rooms])}")
