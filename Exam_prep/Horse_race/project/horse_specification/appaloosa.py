from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    max_speed = 120

    def train(self):
        if self.speed + 2 > self.max_speed:
            self.speed = self.max_speed
        else: self.speed += 2
