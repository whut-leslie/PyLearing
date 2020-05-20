
import random
DEAD = 0
LIVE = 1


class Cell:

    cells = []

    def __init__(self, length):

        self.length = length
        # 为细胞随机分配生存状态
        self.cells = [[random.randint(DEAD, LIVE)
                       for j in range(0, self.length+2)]
                      for i in range(0, self.length+2)]

    def getNearbyNum(self, height, width):
        num = 0
        # 左为-1、右为1
        for d_x in [-1, 0, 1]:
            for d_y in [-1, 0, 1]:
                if not (d_x == 0 and d_y == 0):
                    num += self.cells[height + d_y][width + d_x]
        return num

    def getNewCell(self, h, w):
        num = self.getNearbyNum(h, w)
        return LIVE if num == 3 else (DEAD if num < 2 or num > 3
                                      else self.cells[h][w])

    def Update(self):
        for i in range(self.length + 1):
            for j in range(self.length + 1):
                self.cells[i][j] = self.getNewCell(i, j)
