import tkinter
import random
DEAD = 0
LIVE = 1


class LifeGame(object):
    cells = []
    canvas = None

    # 初始化变量
    def __init__(self, length):
        self.length = length
        # 为细胞随机分配生存状态
        self.cells = [[random.randint(DEAD, LIVE) for j in range(0, self.length+2)]
                      for i in range(0, self.length+2)]


    # 初始屏幕
    def print_screen(self):
        screen = tkinter.Tk()
        screen.title("生命游戏")
        screen.geometry(str('400x400'))
        self.canvas = tkinter.Canvas(screen, bg='white', height=400, width=400)
        self.canvas.pack()
        self.draw_cells()
        self.update_screen()
        screen.mainloop()

    # 绘制画布上的细胞，用小矩形代表细胞，填充为绿色代表活细胞，灰色代表死细胞
    def draw_cells(self):
        width = 400 / self.length
        for i in range(len(self.cells)):
            for j in range(len(self.cells)):
                if self.cells[i][j] == LIVE:
                    # 根据初始

                    self.canvas.create_rectangle(i * width, j * width, (i + 1) * width, (j + 1) * width, fill='green')
                else:
                    self.canvas.create_rectangle(i * width, j * width, (i + 1) * width, (j + 1) * width, fill='grey')

    # 更新画布界面
    def update_screen(self):
        self.Update()
        self.draw_cells()
        self.canvas.after(100, self.update_screen)

    # 获取附近细胞数
    def GetNearbyNum(self, h, w):
        num = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not (dx == 0 and dy == 0):
                    num += self.cells[h+dy][w+dx]
        return num

    # 获取细胞新状态
    def GetNewCell(self, h, w):
        num = self.GetNearbyNum(h, w)
        return LIVE if num == 3 else (DEAD if num < 2 or num > 3 else self.cells[h][w])

    # 更新所有细胞状态
    def Update(self):
        for i in range(self.length+1):
            for j in range(self.length+1):
                self.cells[i][j] = self.GetNewCell(i, j)


game = LifeGame(20)
game.print_screen()


