
def test(num):

    print("在函数内部 %d对应的内存地址是%d" % (num, id(num)))

    # 1> 定义一个字符串变量
    result = "hello"

    print("函数要返回数据的内存地址是 %d" % id(result))

    # 2> 返回字符串变量
    return result


# 1. 定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print("a 变量保存数据的地址是 %d" % id(a))

# 2. 调用 test 函数
r = test(a)

print("%s %d" % (r, id(r)))
