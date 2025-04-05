from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization="EngineerAstronaut", stamina=80)

    def train(self):
        if self.stamina <= 95:
            self.stamina += 5

