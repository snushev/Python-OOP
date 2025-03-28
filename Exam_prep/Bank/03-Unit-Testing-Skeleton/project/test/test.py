from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar('Test', 'Testov', 200_000, 30_000)

    def test_car_init(self):
        self.assertEqual('Test', self.car.model)
        self.assertEqual('Testov', self.car.car_type)
        self.assertEqual(30_000, self.car.price)
        self.assertEqual(200_000, self.car.mileage)
        self.assertListEqual([], self.car.repairs)

    def test_price_1_or_less_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_mileage_less_than_or_equal_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_set_promotional_price_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(31000)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price(self):
        result = self.car.set_promotional_price(25000)
        self.assertEqual(25000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_impossible(self):
        result = self.car.need_repair(16000, "Engine")

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_possible(self):
        result = self.car.need_repair(1000, "Wheel")

        self.assertEqual(31_000, self.car.price)
        self.assertEqual(['Wheel'], self.car.repairs)
        self.assertEqual(f'Price has been increased due to repair charges.', result)

    def test_compare_different_car_types(self):
        car2 = SecondHandCar("Some", "Car", 1000, 1000)
        result = self.car.__gt__(car2)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_compare_price_same_car_type_true(self):
        car2 = SecondHandCar('Test', 'Testov', 200_000, 1_000)
        self.assertTrue(self.car > car2)

    def test_compare_price_same_car_type_false(self):
        car2 = SecondHandCar('Test', 'Testov', 200_000, 99_000)
        self.assertFalse(self.car > car2)

    def test_car_str(self):
        result = self.car.__str__()
        self.assertEqual(f"""Model Test | Type Testov | Milage 200000km\nCurrent price: 30000.00 | Number of Repairs: 0""", result)