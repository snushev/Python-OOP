from unittest import TestCase, main
# from extended_list import IntegerList


class TestList(TestCase):
    def setUp(self):
        self.cl = IntegerList(1, 2, 3)

    def test_init(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_init_non_integers_are_skipped(self):
        new_list = IntegerList("asd", 4.8, [1, 2, 3], 5)
        self.assertListEqual([5], new_list._IntegerList__data)

    def test_get_data_returns_private_data(self):
        result = self.cl.get_data()

        self.assertEqual([1, 2, 3], result)
        self.assertIs(self.cl._IntegerList__data, result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cl.add("four")
            self.cl.add(5.6)
            self.cl.add([7, 8])

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_integer(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)
        result = self.cl.add(4)
        self.assertListEqual([1, 2, 3, 4], self.cl._IntegerList__data)
        self.assertIs(self.cl._IntegerList__data, result)

    def test_remove_index_invalid_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.remove_index(length_index)
            length_index += 1
            self.cl.remove_index(length_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)
        result = self.cl.remove_index(1)
        self.assertListEqual([1, 3], self.cl._IntegerList__data)


    def test_get_invalid_index_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.remove_index(length_index)
            length_index += 1
            self.cl.remove_index(length_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)
        result = self.cl.get(1)
        self.assertEqual(2, result)
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_insert_invalid_index_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.insert(length_index, 2)
            length_index += 1
            self.cl.insert(length_index, 2)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_type_el_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.cl.insert(0, 5.6)
            self.cl.insert(0, "asd")
            self.cl.insert(0, [1, 2, 3])

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_list_insert(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)
        self.cl.insert(0, 0)
        self.assertListEqual([0, 1, 2, 3], self.cl._IntegerList__data)

    def test_list_get_bigger(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.get_biggest()

        self.assertEqual(3, result)
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_list_get_index(self):
        self.cl.add(17)
        self.assertListEqual([1, 2, 3, 17], self.cl._IntegerList__data)

        result = self.cl.get_index(17)

        self.assertEqual(3, result)
        self.assertListEqual([1, 2, 3, 17], self.cl._IntegerList__data)

if __name__ == '__main__':
    main()