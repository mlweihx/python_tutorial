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


class XiaoTianQuan(Dog):

    def bark(self):
        print("叫的跟神一样")

    def fly(self):
        print("I can fly.")


class GodDog(XiaoTianQuan):
    def bark(self):
        print("God Dog bark bark bark")


xtq = XiaoTianQuan()
xtq.bark()

gdog = GodDog()

gdog.bark()
