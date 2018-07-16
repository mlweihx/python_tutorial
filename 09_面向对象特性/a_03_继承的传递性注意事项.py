class Animal:

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):

    def bark(self):
        print("bark bark bark")


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


class XiaoTianQuan(Dog):

    def fly(self):
        print("I can fly.")


# 创建一个狗对象
wangcai = XiaoTianQuan()

wangcai.ca
wangcai.fly()
wangcai.bark()
wangcai.run()
wangcai.eat()
wangcai.drink()
wangcai.sleep()
