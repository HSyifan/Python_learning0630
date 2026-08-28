"""高阶函数"""
# map，filter，min, max, sorted都可以算高阶函数

# reduce() 函数
# reduce 第一个参数是函数，该函数指定2个参数
# reduce第二个参数是可迭代对象
# reduce将可迭代对象中的元素，依次传递到函数中，最终返回累积的结果
def add(x, y):
    return x + y

import functools
result = functools.reduce(add, [1, 2, 3, 4, 5])
print(result) # 15

print(add(add(add(add(1, 2), 3), 4), 5)) # 15

print(functools.reduce(lambda x, y: x * y, range(1, 11))) # 3628800

"""偏函数"""
# 偏函数是固定函数的一部分参数，返回一个新的函数，这个新的函数可以接受剩余的参数
square = functools.partial(pow, exp=2)
print(square(2)) # 4
print(square(3)) # 9

cube = functools.partial(pow, exp=3)
print(cube(2)) # 8
print(cube(3)) # 27

"""@wraps装饰器"""
def time_master(func):
    @functools.wraps(func) # 将func的属性复制到call_func中，不然call_func的__name__属性会变成call_func
    def call_func():
        print("开始运行程序...")
        return func()
    return call_func

@time_master
def myfunc():
    print("I love FishC")

myfunc()
print(myfunc.__name__) # myfunc


# 练习题：
# 请使用偏函数，基于 print() 函数打造一个新的 pr() 函数，使其实现效果如下：
pr = functools.partial(print, sep="@", end="#")
pr("I", "love", "FishC.")

# 请修改下面代码，使得执行 test.__name__ 语句后，得到的结果是 'test'，而非 'call_func'。
def myfunc(func):
    @functools.wraps(func)
    def call_func():
        func()
    return call_func

@myfunc
def test():
    print("test~")
test()

print(test.__name__) # test


# 动动手0： 还记得“斗地主” 的小程序吗？没错，我们又来添砖加瓦了
# 这回我们进一步提高了对出牌规则的检测要求，除了上一节课（传送门）要求的能够检测出 “对牌”、“火箭”、“三张牌相同”、“炸弹” 这 4 种情况之外，这次我们提高了检测的标准：
# a. 三带一（三张相同的牌 + 一张任意牌，比如 “3335”）
# b. 三带二（三张相同的牌 + 对牌，比如 “33355”）
# c. 四带二（炸弹 + 对牌，比如 “333355”）
# d. 单顺（五张或更多的连续单牌，“2” 和大小王不能参与，比如 “34567”）
# e. 双顺（三个或更多的连续对牌， “2” 和大小王不能参与，比如 “334455”）
# f. 三顺（两个或更多的连续三张相同牌， “2” 和大小王不能参与，比如 “333444”）
# g. 飞机带翅膀（两个或更多的三顺 + 相同数量的顺牌或对牌， “2” 和大小王不能参与，比如 “33344488JJ” 或 “33344455579J”）

# 展示所有牌型（考虑到用户自己输入比较麻烦，展示出来便于拷贝）
from collections import Counter
# cards_num = [1, 1, 1, 2, 2, 2, 6, 6, 9, 9]  # 对应 33344488JJ
# c = Counter(cards_num)
# Counter({1: 3, 2: 3, 6: 2, 9: 2})

def get_all_cards():
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_list = [suit + rank for suit in suits for rank in ranks]
    cards_list.append("☀")
    cards_list.append("☾")
    return cards_list

def show_cards(cards_list):
    for i in range(0, len(cards_list), 13):
        print(" ".join(cards_list[i:i+13]))
    print()

ALL_CARDS = get_all_cards()
ALL_CARDS_COUNTER = Counter(ALL_CARDS)

# 2 张牌的情况：对牌
def is_pair(cards_num):
    if cards_num[0] == cards_num[1]:
        return True
    else:
        return False

# 2 张牌的情况：火箭
def is_rocket(cards_num):
    if 14 in cards_num and 15 in cards_num:
        return True
    else:
        return False

# 3 张牌的情况：三张牌相同
def is_three(cards_num):
    if len(set(cards_num)) == 1:
        return True
    else:
        return False

# 4 张牌的情况：炸弹
def is_bomb(cards_num):
    if len(set(cards_num)) == 1:
        return True
    else:
        return False

# a. 三带一（三张相同的牌 + 一张任意牌，比如 “3335”）
def is_three_with_one(cards_num):
    if len(cards_num) == 4 and len(set(cards_num)) == 2 and sorted(Counter(cards_num).values()) == [1, 3]:
        return True
    else:
        return False

# b. 三带二（三张相同的牌 + 对牌，比如 “33355”）
def is_three_with_two(cards_num):
    if len(cards_num) == 5 and len(set(cards_num)) == 2 and sorted(Counter(cards_num).values()) == [2, 3]:
        return True
    else:
        return False

# c. 四带二（炸弹 + 对牌，比如 “333355”）
def is_four_with_two(cards_num):
    if len(cards_num) == 6 and len(set(cards_num)) == 2 and sorted(Counter(cards_num).values()) == [2, 4]:
        return True
    else:
        return False

# d. 单顺（五张或更多的连续单牌，“2” 和大小王不能参与，比如 “34567”）
def is_single_straight(cards_num):
    s = sorted(cards_num)
    if len(s) >= 5 and s == list(range(s[0], s[0] + len(s))) and s[-1] <= 12:
        return True
    else:
        return False

# e. 双顺（三个或更多的连续对牌， “2” 和大小王不能参与，比如 “334455”）
def is_double_straight(cards_num):
    s = sorted(cards_num)
    ranks = s[::2]  # 每对的代表点数
    if len(s) >= 6 and s[::2] == s[1::2] and ranks == list(range(ranks[0], ranks[-1] + 1)) and ranks[-1] <= 12:
        return True
    else:
        return False

# f. 三顺（两个或更多的连续三张相同牌， “2” 和大小王不能参与，比如 “333444”）
def is_triple_straight(cards_num):
    s = sorted(cards_num)
    ranks = s[::3]  # 每三张的代表点数
    if len(s) >= 6 and s[::3] == s[1::3] == s[2::3] and ranks == list(range(ranks[0], ranks[-1] + 1)) and ranks[-1] <= 12:
        return True
    else:
        return False

# g. 飞机带翅膀（两个或更多的三顺 + 相同数量的顺牌或对牌， “2” 和大小王不能参与，比如 “33344488JJ” 或 “33344455579J”）
def is_airplane_with_wing(cards_num):
    c = Counter(cards_num) # 例如：Counter({1: 3, 2: 3, 6: 2, 9: 2})
    body = sorted(k for k, v in c.items() if v == 3)   # 飞机：每种正好 3 张。k是点数，v是数量
    n = len(body)
    wings = sorted(v for k, v in c.items() if v != 3)  # 翅膀：剩下的牌
    if n >= 2 and body[-1] <= 12 and body == list(range(body[0], body[-1] + 1)) and wings in ([1] * n, [2] * n):
        return True
    else:
        return False

# 获取用户输入的扑克牌
def get_input():
    cards = input("请出牌（空格间隔，退出请输入Q）：")
    if cards == 'Q':
        return 0
    else:
        cards = cards.split() # "♠1 ♠2 ♠3 ♠4 ♠5" -> ['♠1', '♠2', '♠3', '♠4', '♠5']
        return cards

# 将扑克牌映射成代表权限的数字
def change_input(cards):
    cards_num = []
    target = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, 'A':12, '2':13}
    for each in cards:
        num = target.get(each[1:]) # 获取card数字部分，转化成target点数
        if num: # 如果num不为空，则将num添加到result中
            cards_num.append(num)
        else: # 如果num为空，则将14或15添加到result中
            cards_num.append(14 if each == '☾' else 15)

    return cards_num

# 检查组合是否符合出牌规则
def check(cards_num):
    # 检查2张牌的情况
    if len(cards_num) == 2:
        if is_pair(cards_num):
            print("符合规则：对牌")
        elif is_rocket(cards_num):
            print("符合规则：火箭")
        else:
            print("不符合规则！")
            
    # 检查3张牌的情况       
    elif len(cards_num) == 3:
        if is_three(cards_num):
            print("符合规则：三张牌相同")
        else:
            print("不符合规则！")
            
    # 检查4张牌的情况
    elif len(cards_num) == 4:
        if is_bomb(cards_num):
            print("符合规则：炸弹")
        elif is_three_with_one(cards_num):
            print("符合规则：三带一")
        else:
            print("不符合规则！")
    
    elif is_three_with_two(cards_num):
        print("符合规则：三带二")
    elif is_four_with_two(cards_num):
        print("符合规则：四带二")
    elif is_single_straight(cards_num):
        print("符合规则：单顺")
    elif is_double_straight(cards_num):
        print("符合规则：双顺")
    elif is_triple_straight(cards_num):
        print("符合规则：三顺")
    elif is_airplane_with_wing(cards_num):
        print("符合规则：飞机带翅膀")
    else:
        print("不符合规则！")

def is_valid_cards(cards):
    return Counter(cards) <= ALL_CARDS_COUNTER # 判断cards中的牌是否在ALL_CARDS中，且每种牌的数量不超过ALL_CARDS中该牌的数量


# 程序主流程
show_cards(ALL_CARDS)
cards = get_input()
while cards:
    if not is_valid_cards(cards):
        print("输入有误：有不存在的牌，或同一张牌出了多次！")
    else:
        cards_num = change_input(cards)
        check(cards_num)
    cards = get_input()


#################################################
# ♠A ♠2 ♠3 ♠4 ♠5 ♠6 ♠7 ♠8 ♠9 ♠10 ♠J ♠Q ♠K
# ♥A ♥2 ♥3 ♥4 ♥5 ♥6 ♥7 ♥8 ♥9 ♥10 ♥J ♥Q ♥K
# ♦A ♦2 ♦3 ♦4 ♦5 ♦6 ♦7 ♦8 ♦9 ♦10 ♦J ♦Q ♦K
# ♣A ♣2 ♣3 ♣4 ♣5 ♣6 ♣7 ♣8 ♣9 ♣10 ♣J ♣Q ♣K
# ☀ ☾

# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♣3 ♥5
# 符合规则：三带一
# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♣3 ♥5 ♠5
# 符合规则：三带二
# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♣3 ♠3 ♥5 ♠5
# 符合规则：四带二
# 请出牌（空格间隔，退出请输入Q）：♥3 ♥4 ♥5 ♥6 ♥7
# 符合规则：单顺
# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♥4 ♠4 ♥5 ♠5
# 符合规则：双顺
# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♣3 ♦4 ♥4 ♠4
# 符合规则：三顺
# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♣3 ♦4 ♥4 ♠4 ♦8 ♣8 ♥J ♠J
# 符合规则：飞机带翅膀
# 请出牌（空格间隔，退出请输入Q）：♦3 ♥3 ♣3 ♦4 ♥4 ♠4 ♥5 ♠5 ♦5 ♥7 ♦9 ♣J
# 符合规则：飞机带翅膀
# 请出牌（空格间隔，退出请输入Q）：Q





























