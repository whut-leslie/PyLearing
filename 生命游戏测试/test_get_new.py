from unittest import TestCase
from get_new import getNewCell


class Test(TestCase):
    def setUp(self):
        self.cell = [[1, 0, 0, 1],
                     [0, 1, 0, 1],
                     [1, 0, 0, 0],
                     [1, 1, 0, 0]]

    def test_get_new_cell(self):
        self.assertEqual(getNewCell(self.cell, 1, 1), 1)
        self.assertEqual(getNewCell(self.cell, 2, 3), 0)
        self.assertEqual(getNewCell(self.cell, 0, 3), 0)
        self.assertEqual(getNewCell(self.cell, 1, 0), 1)
        self.assertEqual(getNewCell(self.cell, 3, 2), 0)
        self.assertEqual(getNewCell(self.cell, 2, 2), 1)


