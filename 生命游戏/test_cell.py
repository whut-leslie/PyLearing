from unittest import TestCase
from cell import Cell


class Test_cell(TestCase):
    """
    测试初始化函数
    """
    def setUp(self):
        self.cell = Cell(50)

    def test_init(self):
        self.assertEqual(self.cell.length, 50)


