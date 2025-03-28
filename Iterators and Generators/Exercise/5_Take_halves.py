def solution():

    def integers():
        current = 1
        while True:
            yield current
            current += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for item in seq:
            if len(result) >= n:
                break
            result.append(item)
        return result


    return (take, halves, integers)

# project zero
# project zero
import unittest

class TakeHalvesTests(unittest.TestCase):
    def test_zero(self):
        take = solution()[0]
        halves = solution()[1]
        result = take(0, halves())
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()