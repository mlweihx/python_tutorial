class Animal:

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


# 创建一个狗对象
wangcai = Animal()

wangcai.run()
wangcai.eat()
wangcai.drink()
wangcai.sleep()


class Dog(Animal):

    # def eat(self):
    #     print("eat")
    #
    # def drink(self):
    #     print("drink")
    #
    # def run(self):
    #     print("run")
    #
    # def sleep(self):
    #     print("sleep")

    def bark(self):
        print("bark bark bark")


class Cat(Animal):
    # 子类中有父类中所有的 属性和方法
    def catch(self):
        print("catch")

