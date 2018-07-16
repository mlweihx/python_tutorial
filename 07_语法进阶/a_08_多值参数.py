#
#
# def demo(num, *nums, **person):
#
#     print(num)
#     print(nums)
#     print(person)
#
#
# demo(1)
# demo(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, name="xiaoming", age=18)


# def sum_num(num):
#
#     print(num)
#
#     if num == 1:
#         return
#
#     sum_num(num - 1)
#
#     print("完成 %d" % num)
#
#
# sum_num(5)


def sum_numbers(num):

    # 1.出口
    if num == 1:
        return 1

    # 2.数字的累加 num +（1 ... num-1）
    # 假设 sum_numbers 能够正确的处理 1 ... num - 1
    temp = sum_numbers(num - 1)

    return num + temp


result = sum_numbers(100)
print(result)
