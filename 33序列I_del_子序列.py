"""列表，元组，字符串都是序列"""
# 列表是可变序列，元组是不可变序列，字符串是不可变序列

"""作用于序列的运算符和函数"""
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print((1, 2, 3) + (4, 5, 6)) # (1, 2, 3, 4, 5, 6)
print("Hello" + "World") # HelloWorld

print([1, 2, 3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print((1, 2, 3) * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print("Hello" * 3) # HelloHelloHello

# id: 查看对象的唯一内存地址
s = [1, 2, 3]
print(id(s)) # 1654545979648

s *= 2
print(s)
print(id(s)) #1654545979648

# 不可变序列的id
t = (1, 2, 3)
print(id(t)) # 1957048532608
t *= 2
print(id(t)) # 1957045660992

# is: 判断两个对象是否是同一个对象
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # True 值相等
print(x is y) # False 不是同一个对象

# in 和 not in：判断元素是否在序列中
print("鱼" in "鱼C工作室") # True
print("C" not in "鱼C工作室") # False

# del: 删除一个或多个对象,或可变序列中的指定元素
x = "FishC"
y = [1, 2, 3]
del x, y
# print(x) # NameError: name 'x' is not defined
# print(y) # NameError: name 'y' is not defined

x = [1, 2, 3, 4, 5]
del x[1:4]
print(x) # [1, 5]

# 切片赋值删除指定元素
y = [1, 2, 3, 4, 5]
y[1:4] = []
print(y) # [1, 5]

x = [1, 2, 3, 4, 5]
del x[::2]
print(x) # [2, 4]

y = [1, 2, 3, 4, 5]
# y[::2] = [] # 报错，因为切片赋值要求左右两边的序列长度相同
# print(y) 

x = [1, 2, 3, 4, 5]
x.clear()
print(x) # []

x = [1, 2, 3, 4, 5]
del x[:]
print(x) # []


# 动动手0：给定字符串 s 和 t ，请编程判断 s 是否为 t 的子序列。
# 字符串的子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串（例如，"ace" 是 "abcde" 的子序列，而 "aec" 则不是）。
# FishC, FijkhsC; 请输入字符串s：FishC
# 请输入字符串t：FiiisjjhkkCBA
# 字符串s是字符串t的子序列

dds0_s = input("请输入字符串s：")
dds0_t = input("请输入字符串t：")

i = 0
for ch in dds0_t:
    if i < len(dds0_s) and ch == dds0_s[i]:
        i += 1
    
if i == len(dds0_s):
    print("字符串s是字符串t的子序列")
else:
    print("字符串s不是字符串t的子序列")

# 动动手1：给定一个字符串 s，请编程求出该字符串中的最大奇数。
# 输入：43383，输出：43383；输入：5926，输出：59；输入：966，输出：9；输入：64062，输出：0

dds1_s = input("输入：")

i = 0
for i in reversed(range(len(dds1_s))):
    if int(dds1_s[i]) % 2 == 1:
        print(f"输出：{dds1_s[:i + 1]}")
        break
else:
    print("输出：0")







