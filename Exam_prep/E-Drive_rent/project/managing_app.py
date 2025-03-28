from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    # @staticmethod
    # def get_object_by_name(object_list, name):
    #     found_object = next((obj for obj in object_list if obj.name == name), None)
    #     return found_object

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user =  next((obj for obj in self.users if obj.driving_license_number == driving_license_number), None)
        if user is not None:
            return f"{driving_license_number} has already been registered to our platform."
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        valid_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

        if vehicle_type not in valid_types:
            return f"Vehicle type {vehicle_type} is inaccessible."
        vehicle =  next((obj for obj in self.vehicles if obj.license_plate_number == license_plate_number), None)
        if vehicle is not None:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle_class = valid_types[vehicle_type]
        self.vehicles.append(vehicle_class(brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        if any(x for x in self.routes if (x.start_point == start_point and x.end_point == end_point and x.length == length)):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        if any(x for x in self.routes if (x.start_point == start_point and x.end_point == end_point and x.length < length)):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."
        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        longer_route = next((x for x in self.routes if (x.start_point == start_point and x.end_point == end_point and x.length > length)), None)
        if longer_route is not None:
            longer_route.is_locked = True ###
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user =  next((obj for obj in self.users if obj.driving_license_number == driving_license_number), None)
        vehicle =  next((obj for obj in self.vehicles if obj.license_plate_number == license_plate_number), None)
        route = self.routes[route_id - 1]
        if user.is_blocked:
           return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        repaired = 0
        if count > len(sorted_vehicles):
            for v in sorted_vehicles:
                v.change_status()
                v.recharge()
                repaired += 1
        else:
            cars_for_repair = sorted_vehicles[:count]
            for v in cars_for_repair:
                v.change_status()
                v.recharge()
            repaired = count
        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key= lambda u: -u.rating)
        result = ["*** E-Drive-Rent ***"]
        for user in sorted_users:
            result.append(user.__str__())
        return '\n'.join(result)