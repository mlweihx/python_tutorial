
def measure():

    print("...")
    tem = 35
    wetness = 40
    print("...")

    # 元组 - 可以包含多个数据，因此可以使用元组让函数一个返回多个值
    # 如果返回的类型是元组，小括号可以省略
    # return (tem, wetness)
    return tem, wetness


result = measure()
print(type(result))

# 需要单独处理温度或者湿度 - 不方便
print(result[0])
print(result[1])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个全局变量，一次接收函数的返回结果
# 使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
gl_tem, gl_wetness = measure()

print(gl_tem)
print(gl_wetness)

