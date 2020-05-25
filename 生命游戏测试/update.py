from get_new import getNewCell


def Update(cell):
    """
      # 获取细胞新状态
    """
    temp = cell
    length = len(cell)
    cell = [[getNewCell(temp, i, j) for j in range(0, length)]
            for i in range(0, length)]
    return cell


