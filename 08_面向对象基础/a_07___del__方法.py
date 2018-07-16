class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s 创建完成" % self.name)

    def __del__(self):
        print("over")


tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom
print("-" * 50)
