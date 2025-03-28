from unittest import TestCase, main

from project.toy_store import ToyStore

class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_add_toy_shelf_not_in_shelves_raises(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("M", "train")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_on_shelf_raises(self):
        self.toy_store.toy_shelf["A"] = "train"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "train")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_already_taken(self):
        self.toy_store.toy_shelf["A"] = "train"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "car")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_success(self):
        result = self.toy_store.add_toy("A", "car")

        self.assertEqual("Toy:car placed successfully!", result)

    def test_remove_toy_shelf_not_in_shelves(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("M", "car")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_different_toy(self):
        self.toy_store.toy_shelf["A"] = "truck"
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "car")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_success(self):
        self.toy_store.toy_shelf["A"] = "truck"

        result = self.toy_store.remove_toy("A", "truck")

        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual("Remove toy:truck successfully!", result)

if __name__ == '__main__':
    main()