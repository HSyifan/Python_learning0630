"""字符串的查找"""
x = "上海自来水来自海上"
print(x.count("海")) # 返回2，因为x中有2个"海"
print(x.count("海", 0, 5)) # 返回1，因为x中有1个"海"，从第0个字符开始查找，到第5个字符结束

# 从左往右查找
print(x.find("海")) # 返回1

# 从右往左查找
print(x.rfind("海")) # 返回7

print(x.find("自")) # 返回2
print(x.rfind("自")) # 返回6

print(x.find("龟")) # 返回-1

# print(x.index("龟")) # 会报错

code = """
    print("I love FishC")
   print("I love my wife")"""

# 将代码中的tab键转换为4个空格
new_code = code.expandtabs(4)
print(new_code)

print("在吗！我在你家楼下，快点下来！！".replace("在吗", "想你"))

# maketrans():创建一个翻译表
table = str.maketrans("ABCDEFG", "1234567")

# translate():根据翻译表进行翻译
print("I love FishC".translate(table)) # I love 6ish3

# translate():根据翻译表进行翻译，第三个参数是需要忽略的字符
print("I love FishC".translate(str.maketrans("ABCDEFG", "1234567", "love"))) # I  6ish3


# 练习题0：
str1 = "xxxxx"
print(str1.count("xx")) # 2

x = "上海自来水来自海上"
print(x.rindex("来水来")) # 10

# print("I love FishC.com".translate(str.maketrans("ABCDEFG", "12345678"))) 

print("I love FishC.com".translate(str.maketrans("love", "1234", "love")))


# 动动手0：用户输入两个版本号 v1 和 v2，请编写代码比较它们，找出较新的版本。
# 版本号是由一个或多个修订号组成，各个修订号之间由点号（.）连接，每个修订号由多位数字组成，例如 1.2.33 和 0.0.11 都是有效的版本号。
# 从左到右的顺序依次比较它们的修订号，点号（.）左侧的值要比右侧的权重大，即 0.1 要比 0.0.99 大。
# dds0_v1 = input("请输入第一个版本号，v1 =")
# dds0_v2 = input("请输入第二个版本号，v2 =")

# # 按点号拆成修订号列表，再转成整数，例如 "1.2.33" → [1, 2, 33]
# dds0_list1 = [int(x) for x in dds0_v1.split(".")]
# dds0_list2 = [int(x) for x in dds0_v2.split(".")]

# # 补齐较短的一侧（缺的修订号当作 0），方便对齐比较
# # 例如 "0.1" → [0, 1, 0]，"0.0.99" → [0, 0, 99]
# dds0_len = max(len(dds0_list1), len(dds0_list2))
# dds0_list1 += [0] * (dds0_len - len(dds0_list1))
# dds0_list2 += [0] * (dds0_len - len(dds0_list2))

# # 从左到右逐段比较
# for i in range(dds0_len):
#     if dds0_list1[i] > dds0_list2[i]:
#         print(f"v1")
#         break
#     elif dds0_list1[i] < dds0_list2[i]:
#         print(f"v2")
#         break
# else:
#     # for 正常结束（没有 break）说明两版本相等
#     print("两个版本号相同")


# 动动手1：编写一个加密程序，其实现原理是通过替换指定的字符进行加密，附加要求是实现密文逆向检测。

plain = input("请输入需要加密的明文：") # 明文，比如 "I love FishC"
x = input("请输入需要替换的字符：") # 要被替换的字符，比如 "ABCDEFG"
y = input("请输入将要替换的字符：") # 替换成什么，比如 "1234567"
    
# 加密的代码
if len(x) != len(y):
    print("需要替换的字符数量必须跟将要替换的字符数量一致！")
else:
    cipher = plain.translate(str.maketrans(x, y))
    print("加密后的密文是：" + cipher)
    
# 检测冲突的代码
# flag 变量标志是否退出检测（只要找到一个冲突，就可以直接退出）
flag = 0
    
# 如果 x 中存在相同的字符，那么 y 对应下标的字符也应该是相同的
# 举例：x = "aba"，y = "xyz"
for each in x:
    if x.count(each) > 1 and flag == 0:
        i = x.find(each)
        last = y[i]
        while i != -1:
            if last != y[i]: # 第一圈不会报错的，last = y[i]，之后就可能报错的
                print("由于替换字符出现冲突，该密文无法解密！")
                flag = -1
                break
    
            i = x.find(each, i+1) # 从i+1位置开始查找
    
# 如果 y 中存在相同的字符，那么 x 对应下标的字符也应该是相同的
# 举例：x = "abc"，y = "xyx"
for each in y:
    if y.count(each) > 1 and flag == 0:
        i = y.find(each)
        last = x[i]
        while i != -1:
            if last != x[i]:
                print("由于替换字符出现冲突，该密文无法解密！")
                flag = -1
                break
    
            i = y.find(each, i+1)




