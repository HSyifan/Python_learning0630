"""字符串"""
# 字符串解决回文判断问题
x = "12321"
print("是回文数" if x == x[::-1] else "不是回文数")

"""字符串为不可变对象"""
# 大小写转换
# 返回的不是原字符串，而是新字符串

x = "I love FishC"

# capitalize() 将字符串的第一个字符转换为大写
print(x.capitalize()) # I love fishc

# casefold() 将字符串转换为小写---可以转换例如德语字符
print(x.casefold()) # i love fishc

# title() 将字符串转换为每个单词首字母大写
print(x.title()) # I Love Fishc

# swapcase() 将字符串中的大小写字母翻转
print(x.swapcase()) # i LOVE fISHC

# upper() 将字符串转换为大写
print(x.upper()) # I LOVE FISHC

# lower() 将字符串转换为小写---只能处理英文字符ACCII
print(x.lower()) # i love fishc

# 左中右对齐

x = "有内鬼，停止交易！"

# center() 将字符串居中对齐。如果例如center(5)小于x长度，则返回原字符串
print(x.center(20)) # '      有内鬼，停止交易！        '
print(x.center(20, "淦")) # 淦淦淦淦淦有内鬼，停止交易！淦淦淦淦淦淦

# ljust() 将字符串左对齐。
print(x.ljust(20)) # 有内鬼，停止交易！     

# rjust() 将字符串右对齐。
print(x.rjust(20)) #      有内鬼，停止交易！

# zfill() 将字符串填充为指定长度。做数据报表，可将520变成00520.
print(x.zfill(20)) # 00000000000有内鬼，停止交易！




# 练习题
print("-520".zfill(10)) 
print("-520".rjust(10, "0"))
print("-520".center(6, "0").zfill(10))
print("I love FishC".swapcase()[::-1])

list5 = ["123", "33211", "12321", "13531", "112233"]
ans5 = []
for i in list5:
    if i == i[::-1]:
        ans5.append(i)
print(ans5)

base = (ord('a'), ord("b"), ord("c"))
print(base)

# 动动手0：一个整理好的字符串中，两个相邻字符 s[j] 和 s[j+1]，其中 0 <= j <= s.length - 2，要满足如下条件：
# 若 s[j] 是小写字符，则 s[j+1] 不可以是相同的大写字符
# 若 s[j] 是大写字符，则 s[j+1] 不可以是相同的小写字符
# 如果 s[j] 和 s[j+1] 满足以上两个条件，则将它们一并删除

dds0_input = input("请输入一个字符串：")
s = list(dds0_input)  # 字符串不能改，先转成列表

# 一轮一轮删：每轮找到一对就删，删完再从头扫；扫完整轮都没得删才结束
while True:
    deleted = False # 用来结束while循环2
    i = 0
    while i < len(s) - 1: # 用来结束while循环1
        # 小写+相同大写，或大写+相同小写 → 一并删除
        if s[i] == s[i + 1].swapcase():
            del s[i:i + 2]  # 一次删两个
            deleted = True          
        else:
            i += 1 # 用来结束while循环1

    # 用来结束while循环2
    if deleted == False:    # 一整轮都没删到，说明已经干净
        break 

print("".join(s))

# 答案：
# s = input("请输入一个字符串：")
    
# res = []
# for each in s:
#     if res and res[-1].lower() == each.lower() and res[-1] != each:
#         res.pop()
#     else:
#         res.append(each)
    
# for each in res:
#     print(each, end='')
# 解析：这里比较难理解的应该是判断部分，它是先判断列表是否为空；如果不为空，则将列表中最后一个元素（即上一轮迭代放进去的字符）拿出来比对，大家都转换成小写，如果一样，那么说明它是同一个字母（此时可能是一个大写一个小写，两个都是大写，或者两个都是小写 3 种可能性）；最后判断如果两者不相同，则说明是同一个字母的大小写。

# 动动手1：1. 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母，奇数下标为正整数。
# 题目要求：编写代码，将奇数下标的数字转换为相对于上一个字母偏移后的字母。
# 比如 s = "a1b2c3" 转换后的结果是 "abbdcf"（a1 -> ab，b2 -> bd，c3 -> cf）；s = "x7y8z9" 转换后的结果是 "xeygzi"（遇到最后字母 z ，则从 a 继续计算偏移）
dds1_input = input("请输入一个字符串：")
result = []

i = 0
while i < len(dds1_input):
    letter = dds1_input[i]          # 偶数下标：字母
    digit = int(dds1_input[i + 1])  # 奇数下标：数字（偏移量）
    # 字母往后偏移 digit 位，超过 z 就从 a 继续（% 26）
    new_letter = chr((ord(letter) - ord('a') + digit) % 26 + ord('a'))
    result.append(letter)      # 原来的字母留下
    result.append(new_letter)  # 数字换成偏移后的字母
    i += 2                     # 下一组

print("".join(result))


# 答案：
# s = input("请按规则输入一个字符串：")
    
# length = len(s)
# # 获取字母 a 的编码值
# base = ord('a')
    
# # 从第一个元素开始，每次迭代跳过一个元素
# for i in range(0, length, 2):
#     # ord(s[i]) - base 操作得到一个字母的偏移值，比如 b 就是 1
#     # 跟 26 求余数的作用是防止溢出，循环计算偏移
#     shift = chr((ord(s[i]) - base + int(s[i+1])) % 26 + base)
#     print(s[i]+shift, end="")

