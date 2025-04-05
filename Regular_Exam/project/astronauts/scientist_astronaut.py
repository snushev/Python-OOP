from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization="ScientistAstronaut", stamina=70)

    def train(self):
        if self.stamina <= 97:
            self.stamina += 3
