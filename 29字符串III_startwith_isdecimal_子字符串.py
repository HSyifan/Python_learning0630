"""字符串的判断和检测"""
# 返回布尔类型的值

# startswith():判断字符串是否以指定字符串开头
# startswith(prefix[, start[, end]])
x = "我爱Python"
print(x.startswith("我")) # True
print(x.startswith("我", 1)) # False # 从第1个字符开始判断

# endswith():判断字符串是否以指定字符串结尾
# endswith(suffix[, start[, end]])
print(x.endswith("Python")) # True
print(x.endswith("on")) # True

# 以元组的形式传入多个待匹配的字符串
x = "她爱Python"
if x.startswith(("你", "我", "她")): # 元组中的任意一个元素都符合条件，则返回True
    print("总有人喜爱Python")

# istitle():判断字符串是否是标题化的
x = "I love Python"
print(x.istitle()) # False, love的l没有大写

# isupper():判断字符串是否全是大写字母
print(x.isupper()) # False

print(x.upper().isupper()) # True

# isalpha():判断字符串是否全是字母
# Unicode 编码中定义的字母，不止是 26 个英文字母
print(x.isalpha()) #  False. 空格不是字母
print("IlovePython".isalpha()) # True
print("一二三四五上山打老虎".isalpha()) # True

# isascii():判断字符串是否全是ASCII字符
# 请使用一行代码判断 s 字符串中，是否所有字符都是英文字母？
print(x.isalpha() and x.isascii())

# isspace():判断字符串是否全是空格
print("    \n".isspace()) # True

# isprintable():判断字符串是否可打印
print("I love FishC\n".isprintable()) # False. \n 是不可打印的字符

# isdecimal():判断字符串是否全是十进制数字
# isdigit():判断字符串是否全是数字（包括十进制、二进制、八进制、十六进制）
# isnumeric():判断字符串是否全是数字。中文数字、罗马数字等也可以
# isalnum(): isalpha(), isdecimal(), isdigit(), isnumeric()任意一个是True，则返回True

x = "12345"
print(x.isdecimal()) # True
print(x.isdigit()) # True
print(x.isnumeric()) # True

x = "2²"
print(x.isdecimal()) # False
print(x.isdigit()) # True
print(x.isnumeric()) # True

x = "Ⅱ"
print(x.isdecimal()) # False
print(x.isdigit()) # False
print(x.isnumeric()) # True

x = "壹贰叁肆伍"
print(x.isdecimal()) # False
print(x.isdigit()) # False
print(x.isnumeric()) # True

x = "1我爱你我的家"
print(x.isdecimal()) # False
print(x.isdigit()) # False
print(x.isnumeric()) # False
print(x.isalnum()) # True

# isidentifier():判断字符串是否是合法的标识符
print("I am a good gay".isidentifier()) # False. 空格不是标识符
print("I_am_a_good_gay".isidentifier()) # True
print("123FishC".isidentifier()) # False. 标识符不能以数字开头

import keyword
print(keyword.iskeyword("if")) # True

# 练习题：
x = "我爱Pyhon"
# print(x.startswith(["你", "我", "她"])) # 会报错，因为startswith()的参数不能是列表，得是元组
print("I love FishC\s".isprintable()) # False. \s 是不可打印的字符
print("一二三四五上山打老虎".isalnum()) # True. 只要有一个字符是数字，则返回True
print("一二三木头人".isidentifier()) # True


# 动动手0：给定一个字符串 text 和字符串列表 words，返回 words 中每个单词在 text 中的位置（要求最终的位置从小到大进行排序）。
# 举例：text："I love FishC and FishC love me"； words："FishC"； 输出：[[7, 11], [17, 21]]

text = input("请输入text的内容：")
words = input("请输入words的内容：")
words = words.split() # 将words按空格分割成列表

result = []
for each in words:
    temp = text.find(each)
    while temp != -1:
        result.append([temp,temp+len(each)-1])
        temp = text.find(each, temp+1) # 从temp+1位置开始查找
    
print(sorted(result))

# 动动手1：编写一个程序，判断输入的字符串是否由多个子字符串重复多次构成。
# 举例：输入："FCFC"，输出：True；输入："FishCFishc"，输出：False
# 如果一个长度为 n 的字符串 s 可以由它的一个长度为 i 的子串 t 重复多次构成，那么必须要满足以下条件：
# n 一定是 i 的倍数
# t 一定是 s 的前缀子字符串
# n 除以 i 的结果必定是 t 在 s 中出现的次数

s = input("请输入一个由字母构成的字符串：")
    
n = len(s)
for i in range(1, n//2+1):
    # 如果子字符串的长度为i，则n必须可以被i整除才行
    if n % i == 0:
        # 如果子字符串的长度为i，则i到i*2之间是一个重复的子字符串
        # 判断后段等于前段，并且后段的内容在s中重复
        if s.startswith(s[i:i*2]) and s.count(s[i:i*2]) == n/i:
            print(True)
            break # 只有最里面那个 if 成立时才会执行到 break
# for...else的用法，小甲鱼希望大家还没有忘记哦^o^
else: # 整个循环都没被 break 打断才执行。for的内容全部执行完了还是没招了，才执行else。
    print(False)

# if-else：条件不成立就怎样
# for-else：整个循环都没被 break 打断才怎样



