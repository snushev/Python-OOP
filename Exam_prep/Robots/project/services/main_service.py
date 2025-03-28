from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        robot_names = ' '.join(robot.name for robot in self.robots) if self.robots else "none"
        return f"{self.name} Main Service:\nRobots: {robot_names}"