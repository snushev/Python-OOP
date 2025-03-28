
from project.vehicle import Vehicle
from unittest import TestCase, main

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20, 100)

    def test_init(self):
        self.assertEqual(20, self.vehicle.fuel)
        self.assertEqual(20, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(10)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_drive_error_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(20, self.vehicle.fuel)

    def test_refuel_success(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(10)
        self.assertEqual(15, self.vehicle.fuel)

    def test_refuel_exception_error_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_(self):
        result = "The vehicle has 100 "\
                 "horse power with 20 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, self.vehicle.__str__())

if __name__ == '__main__':
    main()