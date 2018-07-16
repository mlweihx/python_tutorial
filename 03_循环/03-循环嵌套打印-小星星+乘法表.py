# 打印小星星 第一行1个，每行都多打印一个，依次递增

# # method 1
# i = 1
#
# while i <= 5:
#     print("*" * i)
#     i += 1

# method 2
print("打印小星星")

n = 1
m = 1
while n <= 5:
    while m <= n:
        print("*", end="")
        m += 1

    # 条件处理
    print()
    m = 1
    n += 1





