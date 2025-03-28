from lab_2 import min_eating_speed
import unittest

class TestBananaEating(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_eating_speed([3,6,7,11], 8), 4)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 5), 30)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 6), 23)
        self.assertEqual(min_eating_speed([1,1,1,1], 4), 1)
        self.assertEqual(min_eating_speed([1000000000], 2), 500000000)
        self.assertEqual(min_eating_speed([10, 20, 30], 6), 10)

unittest.main()
