class Gun:

    def __init__(self, model):

        # 枪的型号
        self.model = model

        # 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1。判读子弹数量
        if self.bullet_count <= 1:
            print("[%s] 没有子弹" % self.model)
            return

        # 2。发射子蛋，-1
        self.bullet_count -= 1

        # 3。提示发射信息
        print("[%s] 突突突... %d" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪 新兵没有枪，不用传递，不设置形参
        self.gun = None

    def fire(self):
        pass

        # 1 判断是否有枪，没有枪没法冲锋

        # 2 喊一声口号
        # 3 装填子弹
        # 4 射击


# 1 创建枪对象
ak47 = Gun("AK47")

ak47.add_bullet(20)
ak47.shoot()

# 2 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47

print(xusanduo)