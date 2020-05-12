import random

class LifeGame(object):

    cells = []  # 其中0代表细胞死，1代表生

    # 初始化
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 列表解析的方法给细胞随机分配生存状态
    def InitRandom(self):
        self.cells = [[random.randint(0, 1)for j in range(0,self.width-1)]
                      for i in range(0, self.height-1)]

    def GetNearbyNum(self, h, w):
        num = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not (dx == 0 and dy == 0):
                    num += self.cells[h+dy][w+dx]
        return num

    def GetNewCell(self, h, w):
        num = self.GetNearbyNum(h, w)
        return 1 if num == 3 else (0 if num < 2 or num > 3 else self.cells[h][w])

    def Update(self):
        self.cells = [[self.GetNewCell(i, j) for i in range(0,self.width-1)]
                      for j in range(0, self.height-1)]


