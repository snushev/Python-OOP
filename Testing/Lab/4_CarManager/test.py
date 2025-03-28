from unittest import TestCase, main
# from car_manager import Car

class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Test", "Testov", 10, 100)

    def test_car_init(self):
        self.assertEqual("Test", self.car.make)
        self.assertEqual("Testov", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
            self.car.make = None
            self.car.make = []

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
            self.car.model = None
            self.car.model = []

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_0_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_0_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_0_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_0_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_more_than_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual(100, self.car.fuel_capacity)

        self.car.refuel(110)

        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_invalid_fuel_raises(self):
        self.car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        self.car.fuel_amount = 10
        self.car.drive(10)

        self.assertEqual(9, self.car.fuel_amount)

if __name__ == "__main__":
    main()