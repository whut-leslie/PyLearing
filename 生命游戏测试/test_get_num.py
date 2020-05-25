from unittest import TestCase
from get_num import getNearbyNum


class Test(TestCase):
    def setUp(self):
        self.cell = [[1, 0, 0, 1],
                     [0, 1, 0, 1],
                     [1, 0, 1, 0],
                     [1, 1, 0, 1]]

    def test_get_nearby_num(self):
        self.assertEqual(getNearbyNum(self.cell, 1, 1), 3)
        self.assertEqual(getNearbyNum(self.cell, 2, 3), 3)
        self.assertEqual(getNearbyNum(self.cell, 3, 3), 1)


