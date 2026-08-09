"""用python设计第一个小游戏"""

import random

counts = 3
"""随机数模块"""
answer = random.randint(1, 10)
# random.getstate()
# random.setstate()

"""while循环"""
while counts > 0:
    temp = input("猜猜小甲鱼现在心里想的是哪个数字:")
    guess = int(temp)

    """嵌套"""
    if guess == answer:
        print("你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中也没有奖励！")
        """break语句"""
        break # 如果猜到8，则退出循环
    else:
        if guess < answer:
            print("小啦~")
        else:
            print("大啦~")
        counts = counts - 1 # 如果没猜到8，则次数减1

print("游戏结束,不玩啦^_^")


