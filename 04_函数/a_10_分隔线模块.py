

def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    """打印多行分隔线

    :param char: 字符
    :param times: 重复打印的次数
    """
    row = 0

    while row < 5:
        print_line(char, times)
        row += 1


name = "黑马程序员"
