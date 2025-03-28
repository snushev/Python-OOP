from project.truck_driver import TruckDriver

from unittest import TestCase, main

class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Test", 10.0)

    def test_init(self):
        self.assertEqual("Test", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertDictEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_property_earn_money_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1

        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ex.exception))

    def test_add_cargo_offer_success(self):
        result = self.driver.add_cargo_offer("Sofia", 20)

        self.assertEqual({"Sofia": 20}, self.driver.available_cargos)
        self.assertEqual(f"Cargo for 20 to Sofia was added as an offer.", result)

    def test_add_cargo_offer_fail_raises(self):
        self.driver.available_cargos = {"Sofia": 20}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 20)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_success(self):
        self.driver.available_cargos = {"Sofia": 20}
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(200, self.driver.earned_money)
        self.assertEqual(20, self.driver.miles)
        self.assertEqual(f"Test is driving 20 to Sofia.", result)

    def test_check_for_activities(self):
        self.driver.earned_money = 30
        self.driver.check_for_activities(250)

        self.assertEqual(10, self.driver.earned_money)

    def test_eat(self):
        self.driver.earned_money = 30
        self.driver.eat(250)

        self.assertEqual(10, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 50
        self.driver.sleep(1000)

        self.assertEqual(5, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 510
        self.driver.pump_gas(1500)

        self.assertEqual(10, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 7510
        self.driver.repair_truck(10000)

        self.assertEqual(10, self.driver.earned_money)

    def test_repr(self):
        result = "Test has 0 miles behind his back."
        self.assertEqual(result, self.driver.__repr__())

if __name__ == "__main__":
    main()