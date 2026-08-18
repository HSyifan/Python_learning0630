"""传入参数的个数"""
print("小甲鱼")
print("小甲鱼", "爱", "编程")

def myfunc(*args):
    print("有{}个参数。".format(len(args)))
    print("第2个参数是：{}".format(args[1]))

myfunc("小甲鱼", "不二如是")

myfunc(1, 2, 3, 4, 5)

def myfunc(*args):
    print(args)

myfunc(1, 2, 3, 4, 5)

"""函数结果打包元组"""
# 利用元组进行打包，也可以解包元组
def myfunc():
    return 1, 2, 3

x, y, z = myfunc()
print(x, y, z)

def myfunc(*args):
    print(type(args))

myfunc(1, 2, 3, 4, 5) # <class 'tuple'>

# 函数结果打包元组：*args 后必须用关键字传参
# 不然所有参数都会被*args搜集，导致a和b无法被正确赋值
def myfunc(*args, a, b):
    print(args, a, b)

# myfunc(1, 2, 3, 4, 5) # 报错

# *args放在前面，a和b必须用关键字传参
myfunc(1, 2, 3, a=4, b=5) # (1, 2, 3) 4 5

# 将args放在最后是可以的。a和b可以用位置传参
def myfunc(a, b, *args):
    print(a, b, args)

myfunc(1, 2, 3, 4, 5) # 1 2 (3, 4, 5)

"""函数结果打包为字典"""
def myfunc(**kwargs):
    print(kwargs)

# 打包为字典，必须用关键字传参，因为是键值对
myfunc(a=1, b=2, c=3)

def myfunc(a, *b, **c):
    print(a, b, c)

myfunc(1, 2, 3, 4, x=5, y=6) # 1 (2, 3, 4) {'x': 5, 'y': 6}

# 也有同时使用一个星号和两个星号搜集参数的情况
# print(help(str.format)) # S.format(*args, **kwargs) -> str

"""解包参数"""
args = (1, 2, 3, 4)
def myfunc(a, b, c, d):
    print(a, b, c, d)

# myfunc(args) # 报错，只传了一个

# "*" 可以解包元组，传给函数作参数
myfunc(*args) # 1 2 3 4

# "**" 可以解包字典，传给函数作参数
kwargs = {"a": 1, "b": 2, "c": 3, "d": 4}
myfunc(**kwargs) # 1 2 3 4


# 练习题：
def func(a, b=4, c=5):
    print(a, b, c)
func(1, 2)
# 1 2 5

def func(x, *y, z=3):
    print(x, y, z)
func(1, 1, 2, 3, 5)
# 1 (1, 2, 3, 5) 3

def func(x, **y):
    print(x, y)    
func(x=1, y=2, z=3)
# 1 {'y': 2, 'z': 3}

def func(x, *y, **z):
    print(x, y, z)
func(1, 2, 3, 4, y=5)
# 1 (2, 3, 4) {'y': 5}

def func(x, *y, **z):
    print(x, y, z)
func(1, 2, 3, y=4, z=5)
# 1 (2, 3) {'y': 4, 'z': 5}

# def func(x, *y, **z):
#     print(x, y, z)
# func(1, 2, x=3, y=4, z=5)
# func() got multiple values for argument 'x'

def func(x, y, z=3):
    print(x, y, z)
func((1, 2), *(3, 4)) 
# 相当于传入三个参数，一个元组，两个数字。(1, 2) 3 4
# (1, 2) 3 4


# 动动手0：编写一个函数，将指定的罗马字符转换为数字的形式。
# 罗马数字包含 I、V、X、L、C、D、M 七种字符，分别表示数值 1、5、10、50、100、500、1000
# 将数字 2 写做罗马字符的形式是 II（即 I + I），数字 12 写做 XII（即 X + I + I），27 写做 XXVII（即 X + X + V + I + I），这就有点像咱平时上市场买菜给钱的算法（一颗大白菜 27 元，那么就给两张10元，一张5元和两张1元这样的组合）。
# 罗马字符的组合也存在一些特殊规则，比如 4 不写做 IIII，而是 IV（即 I 在 V 的左边，表示 5 - 1，因此得到数字 4），类似的特例如下：
# I 可以放在 V（5）和 X（10）的左边，表示 4 和 9
# X 可以放在 L（50）和 C（100）的左边，表示 40 和 90
# C 可以放在 D（500）和 M（1000）的左边，表示 400 和 900

###############################
# 请输入一个罗马字符：II
# 转换后的结果是：2
# 请输入一个罗马字符：IX
# 转换后的结果是：9
# 请输入一个罗马字符：LV
# 转换后的结果是：55
# 请输入一个罗马字符：MMXXII
# 转换后的结果是：2022
# 请输入一个罗马字符：MMXCIX
# 转换后的结果是：2099

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_int(s):
    total = 0
    for i in range(len(s)):
        curr = roman_dict[s[i]]
        if i != len(s) - 1: # 如果 i 不是最后一个下标：
            next = roman_dict[s[i + 1]] # 取出下一个值 next = roman_dict[s[i + 1]]
            if curr < next: # curr < next  →  total 减去 curr
                total -= curr
            else: # 否则         →  total 加上 curr
                total += curr
        else: # 如果 i 是最后一个下标：
            total += curr # total 加上 curr
    return total

dds0_input = input("请输入一个罗马字符：")
roman_result = roman_to_int(dds0_input)
print(f"转换后的结果是：{roman_result}")


# 动动手1：编写一个函数，将指定的数字转换为罗马字符的形式。

#################################
# 请输入一个整数：3
# 转换后的结果是：III
# 请输入一个整数：99
# 转换后的结果是：XCIX
# 请输入一个整数：2022
# 转换后的结果是：MMXXII
# 请输入一个整数：2099
# 转换后的结果是：MMXCIX
# 请输入一个整数：10086
# 转换后的结果是：MMMMMMMMMMLXXXVI

roman_dict_reverse = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC",
    400: "CD",
    900: "CM"
}

def int_to_roman(n):
    result = ""
    # 面额必须从大到小：1000, 900, 500, 400, ... 1
    for key in sorted(roman_dict_reverse, reverse=True):
        # （能减几次就拼几次，所以这里用 while，不是 if）
        while n >= key: # 当 n 还大于等于当前面额 key 时：
            result += roman_dict_reverse[key] # result 拼上 roman_dict_reverse[value]
            n -= key # n 减去 key
    return result
    
dds1_input = int(input("请输入一个整数："))
int_result = int_to_roman(dds1_input)
print(f"转换后的结果是：{int_result}")



















