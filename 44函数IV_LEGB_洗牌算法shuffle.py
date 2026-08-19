"""作用域：变量在代码中可以访问的区域"""

"""局部作用域"""
def myfunc():
    x = 520
    print(x)

myfunc()

# 局部作用域的变量不能在全局作用域中访问
# print(x) 
# NameError: name 'x' is not defined

"""全局作用域"""
# 全局作用域的变量可以在全局作用域和局部作用域中访问
x = 880

def myfunc():
    print(x)
myfunc() # 880

def myfunc():
    x = 520
    print(x)

# 在函数中，局部变量会覆盖全局变量
myfunc() # 520
print(x) # 880

x = 880
print(id(x)) # 1850324829136

def myfunc():
    print(id(x))
myfunc() # 1850324829136

def myfunc():
    x = 520
    print(id(x))

myfunc() # 2777608722736

x = 880
def myfunc():
    global x # 声明 x 为全局变量
    x = 520
    print(x)

# 不提倡这么做！！！！
myfunc() # 520
print(x) # 520

"""嵌套函数"""
def funA():
    x = 520
    def funB():
        x = 880
        print("In funB, x = ", x)
    print("In funA, x = ", x)

# funB() # NameError: name 'funB' is not defined

def funA():
    x = 520
    def funB():
        x = 880
        print("In funB, x = ", x)
    funB()
    print("In funA, x = ", x)

funA()
# In funB, x =  880
# In funA, x =  520

"""nonlocal语句"""
# global改的是文件最外层的那个 x（这里是全局变量 x）
# nonlocal改的是最近一层外层函数里的那个 x（这里是 funA）

def funA():
    x = 520
    def funB():
        nonlocal x
        x = 880
        print("In funB, x = ", x)
    funB()
    print("In funA, x = ", x)

funA()
# In funB, x =  880
# In funA, x =  880

"""LEGB规则"""
# Local: 局部作用域
# Enclosing: 嵌套作用域
# Global: 全局作用域
# Built-in: 内置作用域

# Global优先级比Built-in高，所以str(520)会报错，此时str是全局变量，不是内置函数了
# 起名的时候尽量避免使用内置函数名
str = "小甲鱼把str给毁咯"
# str(520) # TypeError: 'str' object is not callable


# 练习题：
x = 250
def set_x(v):
    x = v
    print(x, end=' ')
       
set_x(520)
print(x)
# 520 250

x = 123
y = 456
def exchange(x, y):
    x, y = y, x
       
exchange(x, y)
print(x, y)
# 123 456

x = [1, 2, 3]
def invert(x):
    x = x[::-1]
invert(x)
print(x)
# [1, 2, 3]

x = [1, 2, 3]
def invert(x):
    x[:] = x[::-1]
invert(x)
print(x)
# [3, 2, 1]

# x = 100
# def funA():
#     global x
#     x = 250
#     def funB():
#         nonlocal x
#         x = 520
#     funB()
# funA()
# print(x)
# SyntaxError: no binding for nonlocal 'x' found


# 洗牌算法 —— Fisher-Yates
# 所谓洗牌算法，就是将一组数据打乱的算法，比如像 random 模块中的 shuffle 函数做的就是这么一个事儿。
# 对于该算法的实现描述如下（假设需要打乱 N 个数）：
# 1. 写下从 1 到 N 的数字
# 2.获取一个 1 到剩下数字（包括这个数字）的随机数 k
# 3.从低位开始，取出第 k 个数字（这个数字还没有被取出），把它写在独立的一个列表的最后一位
# 4.重复前两个步骤，直到所有数据都被取出
# 5.现在，新的列表中就是打乱了顺序的结果

# 动动手0：请封装一个 fy_shuffle() 函数。
# 要求：请按 Fisher-Yates 要求的算法步骤实现。
# 参数1：可迭代对象类型，存储原始的数据
# 参数2：整数类型，指定洗牌的次数
# 返回值：列表类型，存储打乱后的数据

################################
# 请输入需要打乱的序列：ABCDEFGH
# 请输入需要打乱的次数：3
# 第1次打乱后的结果：EDCBFAGH
# 第2次打乱后的结果：EFGHCBDA
# 第3次打乱后的结果：HFGBADCE
# 最终的结果是：HFGBADCE

import random

def fy_shuffle(iterable, times):
    i = 0
    while i < times:
        result = ""  # 每一轮重新开始，否则会把上一轮的结果叠进去
        while len(iterable) > 1:
            num = random.randint(1, len(iterable))
            result += iterable[num - 1]
            iterable = iterable[:num - 1] + iterable[num:]
        else:
            result += iterable[0]
        iterable = result
        print(f"第{i + 1}次打乱后的结果：{result}")
        i += 1
    return iterable

# iterable = input("请输入需要打乱的序列：")
# times = int(input("请输入需要打乱的次数："))
# final = fy_shuffle(iterable, times)
# print(f"最终的结果是：{final}")


# 动动手1：运用上面的打乱算法，设计一个 “斗地主” 的发牌程序。
# 游戏介绍：斗地主游戏由 54 张牌组成，包含两张 Joker 牌（大王和小王），游戏人数一般为三人，一人为地主，另外两人为农民。双方出牌对战，地主先出牌，任何一方有一人出完牌时，该方获胜。
# 发牌规则：每人先发 17 张牌，留 3 张作为地主牌，再随机选择 1 名地主，将地主牌给到他。

###########################################
# 请输入第一位玩家的名称：小
# 请输入第二位玩家的名称：甲
# 请输入第三位玩家的名称：鱼
# 地主是：鱼
# 小拿到的牌是：['♦4', '♥K', '♦5', '☀', '♥7', '♠10', '♣7', '♣8', '★', '♠6', '♣3', '♥Q', '♦8', '♦9', '♦J', '♠K', '♦10']
# 甲拿到的牌是：['♦7', '♣5', '♥4', '♦A', '♥8', '♦2', '♣9', '♥3', '♥2', '♠2', '♠9', '♠A', '♠5', '♥5', '♠3', '♦K', '♣4']
# 鱼拿到的牌是：['♣A', '♥6', '♣Q', '♠Q', '♦Q', '♠4', '♦6', '♣10', '♥10', '♠8', '♥J', '♠J', '♦3', '♣J', '♣6', '♣2', '♥9', '♣K', '♠7', '♥A']

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_list = []
for suit in suits:
    for rank in ranks:
        cards_list.append(suit + rank)
cards_list.append("☀")
cards_list.append("★")

def card_game(p_x, p_y, p_z):

    cards = cards_list.copy()
    result = []

    while len(cards) > 1:
        num = random.randint(1, len(cards))
        result.append(cards[num - 1])  # 必须用 append，+= 会把 "♠A" 拆成 '♠' 和 'A'
        cards = cards[:num - 1] + cards[num:]
    else:
        result.append(cards[0])

    # 玩家名字是字符串，不能 append；手牌另外用列表存
    hands = []
    for i in range(3):
        hands.append(result[:17])
        result = result[17:]

    dizhu_index = random.randint(0, 2)
    hands[dizhu_index] += result  

    names = [p_x, p_y, p_z]
    print(f"地主是：{names[dizhu_index]}")
    print(f"{p_x}拿到的牌是：{hands[0]}")
    print(f"{p_y}拿到的牌是：{hands[1]}")
    print(f"{p_z}拿到的牌是：{hands[2]}")

p_x = input("请输入第一位玩家的名称：")
p_y = input("请输入第二位玩家的名称：")
p_z = input("请输入第三位玩家的名称：")
card_game(p_x, p_y, p_z)































