from get_num import getNearbyNum
DEAD = 0
LIVE = 1


def getNewCell(cell, height, width):
    """
     获取细胞新状态
    :param cell: 细胞数组
    :param height: 细胞的列
    :param width: 细胞的行
    :return: 细胞的新状态（DEAD/LIVE）
    """
    num = getNearbyNum(cell, width, height)
    return LIVE if num == 3 else (DEAD if num < 2 or num > 3
                                  else cell[width][height])
