from unittest import TestCase
from update import Update


class Test(TestCase):
    def setUp(self):
        self.cell = [[1, 0, 0, 1],
                     [0, 1, 0, 1],
                     [1, 0, 1, 0],
                     [1, 1, 0, 1]]
        self.new_cell = [[0, 0, 1, 0],
                         [1, 1, 0, 1],
                         [1, 0, 0, 1],
                         [1, 1, 1, 0]]

    def test_update(self):

        self.assertEqual(Update(self.cell), self.new_cell)

