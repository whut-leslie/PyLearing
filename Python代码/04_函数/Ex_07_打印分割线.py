def print_line(char, times):
    print(char*times)


def print_5line(char, times, lines):
    """打印多行分割线
    :param char: 字符
    :param times: 次数
    :param lines: 行数
    """
    i = lines
    while i < 5:
        print_line(char, times)
        i += 1

name = "小明"
