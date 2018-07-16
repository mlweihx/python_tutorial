class Cat:

    def __init__(self):

        print("这是一个初始化方法")

        # self.属性值 = 属性的初始值
        self.name = "Tom"


# 使用 类名（） 创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
tom.name = "Lazy_cat"
print(tom.name)
