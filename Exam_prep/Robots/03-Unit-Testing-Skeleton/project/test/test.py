from project.tennis_player import TennisPlayer

from unittest import TestCase, main

class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer(name="Test", age=20, points=10.5)

    def test_tennis_player_init(self):
        self.assertEqual("Test", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(10.5, self.player.points)
        self.assertListEqual([], self.player.wins)

    def test_name_if_2_or_less_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "da"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_less_than_eighteen(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win(self):
        self.player.add_new_win("Test_tournament")
        self.assertListEqual(["Test_tournament"], self.player.wins)

    def test_add_new_win_when_tournament_already_added(self):
        self.player.wins = ["Test_tournament"]
        result = self.player.add_new_win("Test_tournament")
        self.assertEqual("Test_tournament has been already added to the list of wins!", result)

    def test_if_less_than_new_player(self):
        player2 = TennisPlayer(name="Peter", age=22, points=11.5)
        result = self.player.__lt__(player2)
        self.assertEqual('Peter is a top seeded player and he/she is better than Test', result)

    def test_if_player_better_than_new_player(self):
        player2 = TennisPlayer(name="Peter", age=22, points=3.5)
        result = self.player.__lt__(player2)
        self.assertEqual('Test is a better player than Peter', result)

    def test_final_string(self):
        self.player.wins = ["Wimbledon", "Dumbledore"]
        result = f"Tennis Player: Test\n" \
               f"Age: 20\n" \
               f"Points: 10.5\n" \
               f"Tournaments won: Wimbledon, Dumbledore"

        func_result = self.player.__str__()
        self.assertEqual(result, func_result)

if __name__ == '__main__':
    main()