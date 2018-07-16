def multiple_table():
    row = 1
    col = 1

    while row <= 9:

        while col <= row:
            print("%d * %d = %d" % (col, row, row * col), end="\t")
            col += 1

        # 条件处理
        print()
        col = 1
        row += 1

