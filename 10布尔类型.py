print(bool(250))
print(bool(False))
print(bool('')) # 空字符串为False
print(bool(' ')) # 非空字符串为True
print(bool([])) # 空列表为False
print(bool(0)) # 非空列表为True
print(bool(0.0)) # 0.0为False
print(bool(1)) # 非空列表为True
print(bool(None)) # None为False

# bool定义为false的对象：False, None
# 值为0的数字类型：0, 0.0, 0j, Decimal(0), Fraction(0, 1) （fraction分子为0，分母为1的分数）
# 空序列和集合：'', (), [], {}, set(), range(0)

if 520 > 250:
    print("520大于250")
else:
    print("520小于250")

if bool(250):
    print("250为True")
else:
    print("250为False")

print(1 == True)
print(0 == False)

print(True + False) # 1
print(True - False) # 1
print(True * False) # 0
# print(True / False) # 报错

"""逻辑运算符/布尔运算"""
# and: 与
# or: 或
# not: 非

print(3 < 4 and 4 < 5) # True
print(3 > 4 and 4 < 5) # False
print(3 < 4 or 4 < 5) # True
print(3 > 4 or 4 < 5) # True
print(not 3 < 4) # False
print(3 and 4) # 4
print(3 or 4) # 3
print("FishC" and "LOVE") # LOVE
print("FishC" or 250) # FishC

"""短路逻辑""" 
# 当and的第一个条件为False时，后面的条件不会执行，直接返回False
# 当or的第一个条件为True时，后面的条件不会执行，直接返回True
# 当not的后面条件为False时，直接返回True，否则返回False
# 当and的第一个条件为True时，后面的条件会执行，直到找到第一个为False的条件，然后返回False
# 当or的第一个条件为False时，后面的条件会执行，直到找到第一个为True的条件，然后返回True
# 当not的后面条件为True时，直接返回False，否则返回True

print(3 and 4) # 4
print(3 or 4) # 3
print("FishC" and "LOVE") # LOVE
print("FishC" or 250) # FishC

"""运算符优先级"""
# 从低到高优先级排序：lambda, if-else, or, and, not, |, ^, &, <<, >>, +, -, *, /, %, //, **
# 从高到低优先级排序：** , * , / , % , + , - , << , >> , & , ^ , | , == , != , > , >= , < , <= , not , and , or
print(1 + 2 > 3 - 4) # True
print(not 1 < 2) # False
# 0 or 1 and not 2
# 0 or 1 and False
# 0 or False
# False
