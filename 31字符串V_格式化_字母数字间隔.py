"""格式化字符串"""
year = 2010
print("鱼C工作室成立于 year 年")

print("鱼C工作室成立于 {} 年".format(year))

print("1+2={}. 2的平方是{}. 3的立方是{}".format(1+2, 2**2, 3**3))

print("{1}看到{0}就很激动！".format("小甲鱼", "漂亮的小姐姐")) # 漂亮的小姐姐看到小甲鱼就很激动！

print("{0}{0}{1}{1}".format("是", "非")) # 是是非非

print("我叫{name}, 我爱{fav}".format(name = "小甲鱼", fav = "Python")) # 我叫小甲鱼, 我爱Python

print("我叫{name}, 我爱{0}, 喜爱{0}的人, 运气都不会太差.".format("Python", name = "小甲鱼"))

print("{}, {}, {}".format(1, "{}", 2)) # 1, {}, 2

print("{}, {{}}, {}".format(1, 2)) # 1, {}, 2

""".format() 的对齐 / 填充写法"""
# <左对齐
# >右对齐
# ^居中
print("{:^}".format(250)) # 250

print("{:^10}".format(250)) #'    250    '

print("{1:>10}{0:<10}".format(520, 250)) # '       250520        '

print("{left:>10}{right:<10}".format(right = 520, left = 250)) # '       250520        '

# 0填充,数字宽度为10
print("{:010}".format(250))  # 0000000250

print("{:010}".format(-250)) # -000000250

# %填充,数字宽度为10
print("{1:%>10}{0:%<10}".format(520, 250)) # %%%%%%%250520%%%%%%%

# = 也是一种对齐方式，意思是：符号放在左边，填充字符插在符号和数字中间
# 0填充,数字宽度为10,=号表示在数字前面填充0
print("{:0=10}".format(250)) # 0000000250

print("{:=10}".format(-250)) # -      250


# 练习题：
print("{}, {}, {}".format("苹果", "香蕉", "梨"))
print("{{0}}".format(1))
print("{{{0}}}".format(1))
print("{{{{{{0}}}}}}".format(1))

# 动动手0：请编写一个程序，统计字符串中的单词个数（“单词”以空格进行分隔）

# dds0_input = input("请输入字符串：")
# dds0_list = dds0_input.split()
# print(len(dds0_list))

# 动动手1：请编写一个程序，将用户输入的字符串重新格式化，使得字母和数字相互分隔（即一个字母一个数字相互间隔）
# 输入：FishC1314，输出：F1i3s1h4C；输入：FishC520，输出：字符串中数字和字母的数量不满足重新格式化的条件
# 输入：Python6543210，输出：6P5y4t3h2o1n0

dds1_input = input("输入字母数字字符串：")
letters = []
digits = []

for ch in dds1_input:
    if ch.isalpha():
        letters.append(ch)
    elif ch.isdigit():
        digits.append(ch)

# 数量差超过 1，无法一个字母一个数字交错
if abs(len(letters) - len(digits)) > 1:
    print("字符串中数字和字母的数量不满足重新格式化的条件")
else:
    result = []
    # 谁多谁先开头（一样多时字母先）
    if len(letters) >= len(digits):
        first, second = letters, digits
    else:
        first, second = digits, letters

    for i in range(len(second)):
        result.append(first[i])
        result.append(second[i])
    # 多出来的那一个接在末尾
    if len(first) > len(second):
        result.append(first[-1])

    print("".join(result))

