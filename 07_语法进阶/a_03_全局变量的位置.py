# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证说有的函数
# 都能正常的访问到每一个全局变量
gl_num = 10
# 在定义一个变量
gl_title = "程序员"
# 在定义一个变量
name = "黑马"


def demo():

    num = 121212
    print("%d" % gl_num)
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % name)


# # 在定义一个变量
# gl_title = "程序员"

demo()

# # 在定义一个变量
# name = "黑马"
