

def getNearbyNum(cell, height, width):
    """
    获取附近细胞数
    :param cell:
    :param height: 细胞的列
    :param width: 细胞的行
    :return: 细胞周围的活细胞数
    """
    num = 0
    length = len(cell)
    # 左为-1、右为1
    for d_x in [-1, 0, 1]:
        for d_y in [-1, 0, 1]:
            b = height + d_y
            a = width + d_x
            if 0 <= a < length and 0 <= b < length:
                if not (d_x == 0 and d_y == 0):
                    num += cell[a][b]
    return num
