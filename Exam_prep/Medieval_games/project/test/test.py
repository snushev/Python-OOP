from project.movie import Movie

from unittest import TestCase, main

class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Test", 2000, 10.0)

    def test_init(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertListEqual([], self.movie.actors)

    def test_name_property(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_property(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_success(self):
        self.movie.actors = ["Test1", "Test2"]
        self.movie.add_actor("Test3")

        self.assertListEqual(["Test1", "Test2", "Test3"], self.movie.actors)

    def test_add_actor_already_in_list(self):
        self.movie.actors = ["Test1", "Test2"]
        result = self.movie.add_actor("Test1")

        self.assertEqual("Test1 is already added in the list of actors!", result)

    def test_rating_grater_than_other(self):
        movie2 = Movie("Testtest", 2000, 9)

        result = self.movie.__gt__(movie2)

        self.assertEqual('"Test" is better than "Testtest"', result)

    def test_other_grater_than_movie(self):
        movie2 = Movie("Testtest", 2000, 11)

        result = self.movie.__gt__(movie2)

        self.assertEqual('"Testtest" is better than "Test"', result)

    def test_repr(self):
        self.movie.actors = ["Test1", "Test2"]
        result = repr(self.movie)
        string = f"Name: Test\n" \
               f"Year of Release: 2000\n" \
               f"Rating: 10.00\n" \
               f"Cast: Test1, Test2"
        self.assertEqual(string, result)

if __name__ == '__main__':
    main()