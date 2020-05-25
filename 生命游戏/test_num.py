from unittest import TestCase
from cell import Cell


class Test_num(TestCase):
    def setUp(self):
        self.cell = Cell(50)

    def test_get_num(self,weight,height):

