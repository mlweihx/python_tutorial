import random

player = int(input("请输入您要出的拳 石头（1） 剪刀（2） 布（3）"))
computer = random.randint(1, 3)

print("player is %d - computer is %d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("player win")
elif player == computer:
    print("win win")
else:
    print("computer win")
