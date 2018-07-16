gl_num_list = [6, 4,  9]

gl_num_list.sort()
print(gl_num_list)

gl_num_list.sort(reverse=True)

print(gl_num_list)


def print_info(name, gender=True):
    """答应性别信息

    :param name: 姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


print_info("小明")
print_info("小妹", gender=False)
