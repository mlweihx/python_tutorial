class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s，我的体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s run" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s eat" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)
