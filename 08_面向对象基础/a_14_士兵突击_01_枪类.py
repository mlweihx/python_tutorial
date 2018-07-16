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


ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()
