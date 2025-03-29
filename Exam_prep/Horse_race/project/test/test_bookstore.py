from project.bookstore import Bookstore

from unittest import TestCase, main

class TestBookstore(TestCase):
    def setUp(self):
        self.book_store = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.book_store.books_limit)
        self.assertDictEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)


    def test_books_limit_error(self):
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = 0

            self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

        # with self.assertRaises(ValueError) as ex:
        #     self.book_store.books_limit = -1
        #
        #     self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

    def test_length_of_books(self):
        self.book_store.availability_in_store_by_book_titles = {"A": 3, "B": 5, "C": 16}

        result = self.book_store.__len__()

        self.assertEqual(24, result)

    def test_receive_book_not_enough_space(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book("A", 11)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_success(self):
        self.book_store.availability_in_store_by_book_titles = {"A": 3, "B": 4, "C": 1}
        self.book_store.books_limit = 50

        result = self.book_store.receive_book("C", 3)

        self.assertEqual(f"4 copies of C are available in the bookstore.", result)

    def test_sell_books_not_available_book(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Test", 20)

        self.assertEqual("Book Test doesn't exist!", str(ex.exception))

    def test_sell_books_not_enough_copies(self):
        self.book_store.availability_in_store_by_book_titles = {"A": 5, "B": 4, "C": 1}

        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("A", 7)

        self.assertEqual("A has not enough copies to sell. Left: 5", str(ex.exception))

    def test_sell_books_success(self):
        self.book_store.availability_in_store_by_book_titles = {"A": 5, "B": 4, "C": 1}

        result = self.book_store.sell_book("A", 5)

        self.assertEqual("Sold 5 copies of A", result)

    def test_str(self):
        self.book_store.availability_in_store_by_book_titles = {"A": 5, "B": 4, "C": 1}
        self.book_store.sell_book("A", 5)

        result = self.book_store.__str__()
        self.assertEqual("Total sold books: 5\nCurrent availability: 5\n - A: 0 copies\n - B: 4 copies\n - C: 1 copies", result)

if __name__ == '__main__':
    main()