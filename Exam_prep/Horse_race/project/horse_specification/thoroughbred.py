from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140

    def train(self):
        if self.speed + 3 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 3
