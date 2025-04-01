from project.gallery import Gallery

from unittest import TestCase, main

class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("Test", "Testovo", 100.0)

    def test_init(self):
        self.assertEqual("Test", self.gallery.gallery_name)
        self.assertEqual("Testovo", self.gallery.city)
        self.assertEqual(100, self.gallery.area_sq_m)
        self.assertEqual(True, self.gallery.open_to_public)
        self.assertDictEqual({}, self.gallery.exhibitions)

    def test_name_property(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "1f()-vvwd"

        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_city_property(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "1f()-vvwd"

        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_area_property(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -1

        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition_already_in_dict(self):
        self.gallery.add_exhibition("Exhibition 1", 2010)

        result = self.gallery.add_exhibition("Exhibition 1", 2015)

        self.assertEqual('Exhibition "Exhibition 1" already exists.', result)

    def test_add_exhibition_success(self):
        result = self.gallery.add_exhibition("Exhibition 1", 2010)

        self.assertEqual('Exhibition "Exhibition 1" added for the year 2010.', result)

    def test_remove_exhibition_name_not_in_dict(self):
        result = self.gallery.remove_exhibition("Exhibition 1")

        self.assertEqual('Exhibition "Exhibition 1" not found.', result)

    def test_remove_exhibition_success(self):
        result = self.gallery.add_exhibition("Exhibition 1", 2010)
        self.assertEqual('Exhibition "Exhibition 1" added for the year 2010.', result)
        self.assertDictEqual({"Exhibition 1": 2010}, self.gallery.exhibitions)

        result = self.gallery.remove_exhibition("Exhibition 1")

        self.assertEqual('Exhibition "Exhibition 1" removed.', result)
        self.assertDictEqual({}, self.gallery.exhibitions)

    def test_list_exhibitions_success(self):
        result = self.gallery.add_exhibition("Exhibition 1", 2010)
        self.assertEqual('Exhibition "Exhibition 1" added for the year 2010.', result)

        result = self.gallery.add_exhibition("Exhibition 2", 2015)
        self.assertEqual('Exhibition "Exhibition 2" added for the year 2015.', result)

        expected_output = [
            'Exhibition 1: 2010',
            'Exhibition 2: 2015'
        ]

        self.assertEqual('\n'.join(expected_output), self.gallery.list_exhibitions())

    def test_list_exhibitions_not_open_to_public(self):
        self.gallery.open_to_public = False

        result = self.gallery.add_exhibition("Exhibition 1", 2010)
        self.assertEqual('Exhibition "Exhibition 1" added for the year 2010.', result)

        result = self.gallery.list_exhibitions()

        self.assertEqual('Gallery Test is currently closed for public! Check for updates later on.', result)

if __name__ == '__main__':
    main()