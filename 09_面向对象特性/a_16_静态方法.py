class Dog(object):

    count = 0

    @staticmethod
    def run():

        # 不访问实例属性/实例方法
        print("小狗要跑... ...")

    def __init__(self, name):
        self.name = name


# 通过类名，调用静态方法
Dog.run()
