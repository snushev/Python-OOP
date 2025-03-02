from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        payment = sum([x.salary for x in self.workers])
        # a = 0
        # for worker in self.workers:
        #     a += worker.salary
        if payment <= self.__budget:
            self.__budget -= payment
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        payment = sum([x.money_for_care for x in self.animals])
        if payment <= self.__budget:
            self.__budget -= payment
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n----- {len([x for x in self.animals if x.__class__.__name__ == 'Lion'])} Lions:"
        for animal in  self.animals:
            if animal.__class__.__name__ == "Lion":
                result += f"\n{animal}"
        result += f"\n----- {len([x for x in self.animals if x.__class__.__name__ == 'Tiger'])} Tigers:"
        for animal in  self.animals:
            if animal.__class__.__name__ == "Tiger":
                result += f"\n{animal}"
        result += f"\n----- {len([x for x in self.animals if x.__class__.__name__ == 'Cheetah'])} Cheetahs:"
        for animal in  self.animals:
            if animal.__class__.__name__ == "Cheetah":
                result += f"\n{animal}"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n----- {len([x for x in self.workers if x.__class__.__name__ == 'Keeper'])} Keepers:"
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                result += f"\n{worker}"
        result += f"\n----- {len([x for x in self.workers if x.__class__.__name__ == 'Caretaker'])} Caretakers:"
        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                result += f"\n{worker}"
        result += f"\n----- {len([x for x in self.workers if x.__class__.__name__ == 'Vet'])} Vets:"
        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                result += f"\n{worker}"
        return result