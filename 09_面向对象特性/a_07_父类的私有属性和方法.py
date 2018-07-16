class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):

        print(" %d ")


# 创建一个子类对象
b = B()
print(b)

# 在外界不能直接访问对象的私有 属性/调用私有方法
print()
