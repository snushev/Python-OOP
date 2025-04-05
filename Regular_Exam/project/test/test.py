from unittest import TestCase, main
from project.star_system import StarSystem

class TestStarSystem(TestCase):
    def setUp(self):
        self.system = StarSystem("Test", "Red giant", 'Single', 3)

    def test_init(self):
        self.assertEqual(self.system.name, "Test")
        self.assertEqual(self.system.star_type, "Red giant")
        self.assertEqual(self.system.system_type, "Single")
        self.assertEqual(self.system.num_planets, 3)

        self.system.habitable_zone_range = (0, 2)
        self.assertEqual(self.system.habitable_zone_range, (0, 2))

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.system.name = " "

        self.assertEqual(str(ex.exception), "Name must be a non-empty string.")

    def test_star_type_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.system.star_type = " "

        self.assertEqual(str(ex.exception), "Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].")

    def test_system_type_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.system.system_type = " "

        self.assertEqual(str(ex.exception), "System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].")

    def test_num_planets_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.system.num_planets = -1

        self.assertEqual(str(ex.exception), "Number of planets must be a non-negative integer.")

    def test_habitable_zone_range_len_gt_2(self):
        with self.assertRaises(ValueError) as ex:
            self.system.habitable_zone_range = (0, 1, 2)

        self.assertEqual(str(ex.exception), "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

    def test_habitable_zone_range_first_gt_second(self):
        with self.assertRaises(ValueError) as ex:
            self.system.habitable_zone_range = (2, 1)

        self.assertEqual(str(ex.exception), "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

    def test_is_habitable_test_none(self):

        self.assertFalse(self.system.is_habitable)

    def test_is_habitable_no_planets(self):
        self.system.num_planets = 0
        self.assertFalse(self.system.is_habitable)

    def test_is_habitable_yes(self):
        self.system.habitable_zone_range = (0, 1)
        self.assertTrue(self.system.is_habitable)

    def test_greater_than_other_if_self_is_not_habitable(self):
        system2 = StarSystem("Test", "Red giant", 'Single', 3, (0, 2))

        with self.assertRaises(ValueError) as ex:
            self.system.__gt__(system2)

            self.assertEqual(str(ex.exception), "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_greater_than_other_if_other_is_not_habitable(self):
        self.system.habitable_zone_range = (0, 1)
        system2 = StarSystem("Test", "Red giant", 'Single', 3)

        with self.assertRaises(ValueError) as ex:
            self.system.__gt__(system2)

            self.assertEqual(str(ex.exception),"Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_greater_than_other(self):
        self.system.habitable_zone_range = (0, 5)
        system2 = StarSystem("Test", "Red giant", 'Single', 3, (0, 2))
        self.assertTrue(self.system.__gt__(system2))

    def test_greater_than_self(self):
        self.system.habitable_zone_range = (0, 1)
        system2 = StarSystem("Test", "Red giant", 'Single', 3, (0, 2))
        self.assertFalse(self.system.__gt__(system2))

    def test_compare_star_systems_success(self):
        self.system.habitable_zone_range = (0, 5)
        system2 = StarSystem("Test", "Red giant", 'Single', 3, (0, 2))

        result = self.system.compare_star_systems(self.system, system2)
        self.assertEqual(result, f"{self.system.name} has a wider habitable zone than {system2.name}.")

    def test_compare_star_systems_less_than_other(self):
        self.system.habitable_zone_range = (0, 1)
        system2 = StarSystem("Test", "Red giant", 'Single', 3, (0, 2))

        result = self.system.compare_star_systems(self.system, system2)
        self.assertEqual(result, f"{system2.name} has a wider or equal habitable zone compared to {self.system.name}.")

    def test_compare_star_systems_valueError(self):
        system2 = StarSystem("Test", "Red giant", 'Single', 0, (0, 2))


        result = self.system.compare_star_systems(self.system, system2)

        self.assertEqual(result, "Comparison not possible: One or both systems lack a defined habitable zone or planets.")


if __name__ == '__main__':
    main()