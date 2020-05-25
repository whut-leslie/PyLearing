"""
图形用户界面
"""
import tkinter
from cell import Cell
from get_num import getNearbyNum
from get_new import getNewCell
from update import Update
DEAD = 0
LIVE = 1


class Game:
    """
    game类，对cell实现GUI
    """
    # 初始屏幕
    screen = None
    canvas = None

    def __init__(self, length):
        """
        :param length: 细胞个数为length*length
        """
        self.length = length
        self.cells = Cell(length)

    def print_screen(self):
        """
        :return: 输出界面
        """
        self.screen = tkinter.Tk()
        self.screen.title("生命游戏")
        self.screen.geometry(str('410x410'))
        self.canvas = tkinter.Canvas(self.screen, bg='white',
                                     height=400, width=400)
        self.canvas.pack()
        self.draw_cells()
        self.update_screen()
        self.screen.mainloop()

    # 绘制画布上的细胞，用小矩形代表细胞，填充为绿色代表活细胞，灰色代表死细胞
    def draw_cells(self):
        """
        :return: 画出当前细胞生命状态的界面
        """
        width = int(400 / self.length)
        for i in range(len(self.cells.cells)):
            for j in range(len(self.cells.cells)):
                if self.cells.cells[i][j] == LIVE:
                    # 根据初始
                    self.canvas.create_rectangle(i * width, j * width,
                                                 (i + 1) * width,
                                                 (j + 1) * width, fill='green')
                else:
                    self.canvas.create_rectangle(i * width, j * width,
                                                 (i + 1) * width,
                                                 (j + 1) * width, fill='grey')

    def update_screen(self):
        """
        更新画布界面
        :return:
        """
        self.cells.cells = Update(self.cells.cells)
        self.draw_cells()
        self.canvas.after(100, self.update_screen)
