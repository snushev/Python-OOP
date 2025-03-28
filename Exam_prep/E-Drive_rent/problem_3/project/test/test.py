from project.robot import Robot
from unittest import TestCase, main

class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("1", 'Military', 10, 250)

    def test_robot_init(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(250, self.robot.price)
        self.assertListEqual([], self.robot.hardware_upgrades)
        self.assertListEqual([], self.robot.software_updates)

    def test_category_not_allowed_raises(self):
        with self.assertRaises(ValueError) as exception:
            self.robot.category = 'Other'

        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(exception.exception))

    def test_price_less_than_0_raises(self):
        with self.assertRaises(ValueError) as exception:
            self.robot.price = -10

        self.assertEqual("Price cannot be negative!", str(exception.exception))

    def test_upgrade_if_hardware_owned(self):
        self.robot.hardware_upgrades = ['Arm']
        result = self.robot.upgrade('Arm', 100)
        self.assertEqual("Robot 1 was not upgraded.", result)

    def test_upgrade_hardware(self):
        total = self.robot.price + (100 * 1.5)
        result = self.robot.upgrade('Arm', 100)

        self.assertListEqual(['Arm'], self.robot.hardware_upgrades)
        self.assertEqual(total, self.robot.price)
        self.assertEqual(result, 'Robot 1 was upgraded with Arm.')

    def test_update_if_cannot_be_updated(self):
        self.robot.software_updates = [5]
        self.robot.available_capacity = 3

        result = self.robot.update(3, 5)

        self.assertEqual(result, 'Robot 1 was not updated.')

    def test_robot_update_success(self):
        self.robot.software_updates = [2]

        result = self.robot.update(3, 5)

        self.assertListEqual([2, 3], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(result, 'Robot 1 was updated to version 3.')

    def test_compare_if_robot_is_more_expensive_than_other(self):
        robot2 = Robot("2", 'Military', 10, 100)

        result = self.robot.__gt__(robot2)
        self.assertEqual(result, 'Robot with ID 1 is more expensive than Robot with ID 2.')

    def test_compare_if_robots_are_equal_price(self):
        robot2 = Robot("2", 'Military', 10, 250)

        result = self.robot.__gt__(robot2)
        self.assertEqual(result, 'Robot with ID 1 costs equal to Robot with ID 2.')

    def test_compare_if_robot_is_cheaper_than_other(self):
        robot2 = Robot("2", 'Military', 10, 280)

        result = self.robot.__gt__(robot2)
        self.assertEqual(result, 'Robot with ID 1 is cheaper than Robot with ID 2.')


if __name__ == '__main__':
    main()
