

def print_line(char, times):
    print(char * times)


def print_lines(num, char, times):
    """打印多行分隔线

    :param num: 打印的行数
    :param char: 字符
    :param times: 重复打印的次数
    """
    row = 0

    while row < num:
        print_line(char, times)
        row += 1


print_line("-+-", 5)
print_lines(5, "9", 9)
print_lines(2, "0", 12)