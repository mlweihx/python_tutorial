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

    def __init__(self):
        self.n = 10

    def fly(self):
        print("I can fly.")

    def bark(self):

        # 1 针对子类特有的需求，编写代码
        print("叫的跟神一样")

        if self.n == 0:
            return

        self.n -= 1

        # 2 使用 super（） 调用原本在父类中封装的代码
        # super().bark()

        # 父类名.方法(self)
        # Dog.bark(self)

        # 注意：如果使用子类调用方法，会出现递归调用
        XiaoTianQuan.bark(self)

        # 3 增加其它子类的代码
        print("$%#$%^&*$%^&*%^&*")


xtq = XiaoTianQuan()
xtq.bark()
