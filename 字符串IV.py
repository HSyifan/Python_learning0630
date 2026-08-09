"""字符串的截取"""
# 去除左侧的空格
print("    左侧不要留白".lstrip()) 

# 去除右侧的空格
print("右侧不要留白    ".rstrip()) 

# 去除两侧的空格
print("    两侧不要留白    ".strip()) 

# 去除字符串中的指定字符
# 规则是：从左 / 从右 / 从两边，只要当前字符在这个集合里就删掉，碰到不在集合里的字符就停。不是整串搜索删除。
# 去除左侧的指定字符
print("www.ilovefishc.com".lstrip("wcom.")) # ilovefishc.com

# 去除右侧的指定字符
print("www.ilovefishc.com".rstrip("wcom.")) # www.ilovefish

# 去除两侧的指定字符
print("www.ilovefishc.com".strip("wcom.")) # ilovefish

# 删除参数指定的整个字符串
# removeprefix():删除指定前缀
# removeprefix 只会在字符串真正以该前缀开头时才删掉它。
print("www.ilovefishc.com".removeprefix("www.")) # ilovefishc.com
print("www.ilovefishc.com".removeprefix("w.")) # www.ilovefishc.com

# removesuffix():删除指定后缀
print("www.ilovefishc.com".removesuffix(".com")) # www.ilovefishc

"""字符串的拆分和拼接"""
# partition():从左到右，将字符串拆分为三部分：前缀、分隔符、后缀
print("www.ilovefishc.com".partition(".")) # ('www', '.', 'ilovefishc.com')

# rpartition():从右到左，将字符串拆分为三部分：前缀、分隔符、后缀
print("www.ilovefishc.com".rpartition(".")) # ('www.ilovefishc', '.', 'com')

print("苟日新，日日新，又日新".split("，")) # ['苟日新', '日日新', '又日新。']

# split():从左到右，将字符串切1次，返回列表
print("苟日新，日日新，又日新，又日新".split("，", 2)) # ['苟日新', '日日新', '又日新，又日新']

# rsplit():从右到左，将字符串切1次，返回列表
print("苟日新，日日新，又日新".rsplit("，", 1)) # ['苟日新，日日新', '又日新']

"""字符串按行分割"""
print("苟日新\n日日新\n又日新".split("\n"))

print("苟日新\n日日新\r\n又日新".splitlines()) # ['苟日新', '日日新', '又日新']
print("苟日新\n日日新\r\n又日新".splitlines(keepends=True)) # ['苟日新\n', '日日新\r\n', '又日新']

"""字符串的拼接"""
# join():将列表中的元素拼接成一个字符串
print(".".join(["www", "ilovefishc", "com"])) # www.ilovefishc.com

# join():将元组中的元素拼接成一个字符串
print("^".join(("F", "ish", "C"))) # F^ish^C
print("".join(("FishC", "FishC"))) # FishCFishC


# 练习题：
print("www.ilovefishc.com".removeprefix("w."))

print("https://ilovefishc.com/html5/index.html".split("/")[2].split(".")[0])

print(" ".join(["I", "love", "FishC"]))

print(",\n".join("FishC")) 
# F,
# i,
# s,
# h,
# C

# 动动手0：编写一个生成凯撒密码的程序
# 凯撒密码是一种通过位移加密的方法，对 26 个（大小写）字母进行位移加密，比如下方是正向位移 6 位的字母对比表：
# 明文字母表如下：ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# GHIJKLMNOPQRSTUVWXYZABCDEFghijklmnopqrstuvwxyzabcdef
# 所以，如果给定加密的明文是：I love FishC
# 移动 6 位后，得到的密文是：O rubk LoynI
dds0_word = input("请输入需要加密的明文（只支持英文字母）：")
dds0_offset = int(input("请输入移动的位数："))
result = []

dds0_list = [x for x in dds0_word.split(" ")]

for each in dds0_list:
    for i in each:
        if i.isalpha():
            if i.isupper():
                result.append(chr((ord(i) - ord('A') + dds0_offset) % 26 + ord('A')))
            else:
                result.append(chr((ord(i) - ord('a') + dds0_offset) % 26 + ord('a')))
    result.append(" ") # 每个单词之间添加一个空格
print("".join(result))

# 答案：
# plain = list(input("请输入需要加密的明文（只支持英文字母）："))
# key = int(input("请输入移动的位数："))
    
# base_A = ord('A')
# base_a = ord('a')
    
# cipher = []
# for each in plain:
#     if each == ' ':
#         cipher.append(' ')
#     else:
#         if each.isupper():
#             base = base_A
#         else:
#             base = base_a
#         cipher.append(chr((ord(each) - base + key) % 26 + base))
    
# print(''.join(cipher))
 

# 动动手1：1. 给定一个字符串数组 words，只返回可以使用在美式键盘同一行的字母打印出来的单词，键盘布局如下图所示。
# 第一行由字符 "qwertyuiop" 组成
# 第二行由字符 "asdfghjkl" 组成
# 第三行由字符 "zxcvbnm" 组成
# 输入：words = ["Twitter", "TOTO", "FishC", "Python", "ASL"])
# 输出：['Twitter', 'TOTO', 'ASL']

words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
result = []

for word in words:
    lower_word = word.lower()  # 忽略大小写
    for row in rows:
        ok = True
        for ch in lower_word:
            if ch not in row:  # 有一个字母不在这一行，就不行
                ok = False
                break
        if ok:  # 整词都在同一行
            result.append(word)
            break

print(result)

# 答案：
# words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]

# res = []
# for i in words:
#     # 由于单词存在大小写，所以这里统一先转换为小写字母
#     j = i.lower()
#     # 灵活运用 strip() 方法，判断 j 是否所有字符都在键盘的同一行内
#     if j.strip("qwertyuiop") == '' or j.strip("asdfghjkl") == '' or j.strip("zxcvbnm") == '':
#         res.append(i)

# print(res)


