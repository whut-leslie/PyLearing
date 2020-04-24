# 导入随机工具包
import random
# 从控制输入要出的拳

player = int(input("请输入要出的拳 石头(1)/剪刀(2)/布(3)"))
computer = random.randint(1, 3)  # 随机整数
print("玩家选择的拳头是 %d -电脑出的拳是 %d" % (player,computer))
# 比较胜负
# 胜利的条件：1胜2,2胜3,3胜1
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")


