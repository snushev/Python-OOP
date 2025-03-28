from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = 'Test'
    health = 100.0
    damage = 100.0
    level = 10

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)


    def test_global_variables_types(self):
        self.assertIsInstance(self.username, str)
        self.assertIsInstance(self.health, float)
        self.assertIsInstance(self.damage, float)
        self.assertIsInstance(self.level, int)

    def test_init(self):
        self.assertEqual('Test', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_name_same_as_enemy(self):
        hero2 = Hero('Test', 10, 100, 100)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(hero2)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_less_than_or_equal_to_0(self):
        hero2 = Hero('Test2', 10, 100, 100)

        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health -= 1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_less_than_or_equal_to_0(self):
        hero2 = Hero('Test2', 10, 0, 100)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual(f"You cannot fight {hero2.username}. He needs to rest", str(ex.exception))

        hero2.health -= 1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual(f"You cannot fight {hero2.username}. He needs to rest", str(ex.exception))

    def test_battle_success_with_both_equal_or_less_than_0_hp_left(self):
        hero2 = Hero('Test2', 10, 100, 100)

        result = self.hero.battle(hero2)
        self.assertEqual("Draw", result)

    def test_battle_success_hero_won(self):
        hero2 = Hero('Test2', 10, 100, 5)

        result = self.hero.battle(hero2)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_success_enemy_won(self):
        hero2 = Hero('Test2', 10, 100, 100)
        self.hero.damage = 0

        result = self.hero.battle(hero2)

        self.assertEqual(11, hero2.level)
        self.assertEqual(105, hero2.health)
        self.assertEqual(105, hero2.damage)
        self.assertEqual("You lose", result)

    def test_hero_str(self):
        result = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(result, self.hero.__str__())

if __name__ == '__main__':
    main()