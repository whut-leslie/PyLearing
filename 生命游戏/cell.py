"""
细胞类
"""
import random
DEAD = 0
LIVE = 1


class Cell:
    """
    细胞类
    """
    cells = []

    def __init__(self, length):
        """
        初始化变量
        :param length: 输入细胞为length * length个
        """
        self.length = length
        # 为细胞随机分配生存状态
        self.cells = [[random.randint(DEAD, LIVE)
                       for j in range(0, self.length+2)]
                      for i in range(0, self.length+2)]

    def get_num(self, height, width):
        """
        获取附近细胞数
        :param height: 细胞的列
        :param width: 细胞的行
        :return: 细胞周围的活细胞数
        """
        num = 0
        # 左为-1、右为1
        for d_x in [-1, 0, 1]:
            for d_y in [-1, 0, 1]:
                if not (d_x == 0 and d_y == 0):
                    num += self.cells[height + d_y][width + d_x]
        return num

    def get_new(self, height, width):
        """
         获取细胞新状态
        :param height: 细胞的列
        :param width: 细胞的行
        :return: 细胞的新状态（DEAD/LIVE）
        """
        num = self.get_num(height, width)
        return LIVE if num == 3 else (DEAD if num < 2 or num > 3
                                      else self.cells[height][width])

    def update(self):
        """
          # 获取细胞新状态
        :return:
        """
        for i in range(self.length + 1):
            for j in range(self.length + 1):
                self.cells[i][j] = self.get_new(i, j)
