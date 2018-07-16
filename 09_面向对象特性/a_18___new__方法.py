class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1. 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2. 为对象分配空间
        instance = super().__new__(cls)
        print(instance)

        # 3. 返回对象的引用
        return instance

    def __init__(self):
        print("init")


# 创建播放器对象
player = MusicPlayer()
print(player)
