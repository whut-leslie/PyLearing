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
