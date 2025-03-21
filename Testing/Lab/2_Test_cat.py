class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

from unittest import TestCase, main
class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Puhcho")

    def test_cat_init(self):
        self.assertEqual("Puhcho", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_is_fed_raises(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

            # Assert
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_is_fed(self):
        self.cat.size = 3
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(4, self.cat.size)

    def test_cat_sleep_raises(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

            # Assert
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    main()