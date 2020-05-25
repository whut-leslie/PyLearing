from unittest import TestCase
from cell import Cell


class Test_new(TestCase):
    def setUp(self):
        cell = Cell(50)

    def test_get_new(self):
        self.assertEqual(cell.get_new())