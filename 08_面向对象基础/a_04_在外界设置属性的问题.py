

class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# tom.name = "Tom"

tom.drink()
tom.eat()
tom.name = "Tom"



