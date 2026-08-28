"""函数文档"""
# print(help(print))

def exchange(dollar, rate = 6.32):
    """
    功能：汇率转换，美元 -> 人民币
    参数：
    - dollar：美元数量
    - rate：汇率，默认值为6.32（2022-03-08）
    返回值：
    - 人民币的数量
    """
    return dollar * rate

print(exchange(20)) # 126.4
# print(help(exchange))


"""类型注释"""

# 作者希望times函数接收两个参数，一个是字符串，一个是整数，返回一个字符串
def times(s:str, n:int) -> str:
    return s * n
print(times("FishC", 5)) # FishCFishCFishCFishCFishC
print(times(5, 5)) # 25

# 希望传入有默认值的参数，返回一个字符串
def times(s:str = "FishC", n:int = 3) -> str:
    return s * n
print(times()) # FishCFishCFishC

# 希望传入列表，返回一个列表
def times(s:list, n:int = 3) -> list:
    return s * n
print(times([1, 2, 3])) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 希望传入列表的内容类型是整数
def times(s:list[int], n:int = 3) -> list[int]:
    return s * n

# 希望传入字典，且键是字符串，值是整数
def times(s:dict[str, int], n:int = 3) -> list:
    return list(s.keys()) * n
print(times({"A": 1, "B": 2, "C": 3})) # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']


"""内省"""
print(times.__name__) # times
print(times.__annotations__) # {'s': dict[str, int], 'n': <class 'int'>, 'return': <class 'list'>}
# print(exchange.__doc__)


# 练习题：
def times(s:str, n:int) -> str:
    return s * n
print(times(5, "FishC")) # FishCFishCFishCFishCFishC
# 请问这里会打印什么内容？

def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):
    pass
print(foo.__annotations__) # {'a': 'x', 'b': 11, 'c': <class 'list'>, 'return': 9}
# 请问这里会打印什么内容？


# 动动手0：Mypy 模块的安装及使用介绍，并将里边的代码跟着动手练习一遍。
# python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple mypy
# 使用：在concole里输入 mypy 51函数XI.py 来检查函数输入输类型出是否正确

# 动动手1：“斗地主” 的发牌程序添砖加瓦~
# 要求：a. 展示所有的牌面（如下图）
# b. 获取用户输入的出牌
# c. 判断用户输入的组合是否符合 “斗地主” 的出牌规则（由于完成程序的代码量有点儿大，本题仅要求检测 “对牌”、“火箭”、“三张牌相同”、“炸弹” 这 4 种情况）。
# 注解：“对牌” 即两张相同的牌；“火箭” 即两张王；“炸弹” 即四张相同的牌

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_list = []
for suit in suits:
    for rank in ranks:
        cards_list.append(suit + rank)
cards_list.append("☀")
cards_list.append("☾")

# 每行打印 13 张牌
for i in range(0, len(cards_list), 13):
    print(" ".join(cards_list[i:i+13]))

def get_num(card):
    """去掉花色，只留点数：♠A -> A，♥10 -> 10"""
    return card[1:]

while True:
    op = input("请出牌（空格间隔，退出请输入Q）：")
    if op.upper() == "Q":
        break

    s = op.split()
    # s 里每一张牌都在 cards_list 里吗？
    if not all(card in cards_list for card in s) or len(s) != len(set(s)):
        print("输入有误")
        continue

    # 火箭：大小王（先判断，因为王没有点数）
    if set(s) == {"☀", "☾"}:
        print("符合规则：火箭")
    # 对牌 / 三张 / 炸弹：比的是点数，不是整张牌（花色不同没关系）
    elif len(s) == 2 and get_num(s[0]) == get_num(s[1]):
        print("符合规则：对牌")
    elif len(s) == 3 and get_num(s[0]) == get_num(s[1]) == get_num(s[2]):
        print("符合规则：三张牌相同")
    elif len(s) == 4 and len(set(get_num(c) for c in s)) == 1:
        print("符合规则：炸弹")
    else:
        print("不符合规则！")


##############################################
# ♠A ♠2 ♠3 ♠4 ♠5 ♠6 ♠7 ♠8 ♠9 ♠10 ♠J ♠Q ♠K
# ♥A ♥2 ♥3 ♥4 ♥5 ♥6 ♥7 ♥8 ♥9 ♥10 ♥J ♥Q ♥K
# ♦A ♦2 ♦3 ♦4 ♦5 ♦6 ♦7 ♦8 ♦9 ♦10 ♦J ♦Q ♦K
# ♣A ♣2 ♣3 ♣4 ♣5 ♣6 ♣7 ♣8 ♣9 ♣10 ♣J ♣Q ♣K
# ☀ ☾
# 请出牌（空格间隔，退出请输入Q）：♥8 ♠8
# 符合规则：对牌
# 请出牌（空格间隔，退出请输入Q）：☾ ☀
# 符合规则：火箭
# 请出牌（空格间隔，退出请输入Q）：♦9 ♥9 ♠9
# 符合规则：三张牌相同
# 请出牌（空格间隔，退出请输入Q）：♦6 ♥6 ♣6 ♠6
# 符合规则：炸弹
# 请出牌（空格间隔，退出请输入Q）：♥7 ♥8 ♥9
# 不符合规则！
# 请出牌（空格间隔，退出请输入Q）：♣3 ♣4  
# 不符合规则！
# 请出牌（空格间隔，退出请输入Q）：Q





















