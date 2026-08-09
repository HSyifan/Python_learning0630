"""用python设计第一个小游戏"""

temp = input("猜猜小甲鱼现在心里想的是哪个数字:")
guess = int(temp)

if guess == 8:
    print("你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中也没有奖励！")
else:
    print("猜错了，小甲鱼现在心里想的是8！")

print("游戏结束,不玩啦^_^")

逻辑判断 = """
小于 <
小于等于 <=
大于 >
大于等于 >=
==
!=
is
is not
"""