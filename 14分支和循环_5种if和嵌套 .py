"""if语句"""
# 1. 判断一个条件，如果这个条件成立，就执行if语句块中的代码
if 3 > 5:
    print("我在里面~")
    print("我也在里面~")
print("我在外面~")

# 2. 判断一个条件，如果这个条件成立，就执行if语句块中的代码，否则执行else语句块中的代码
if "小甲鱼" == "小姐姐":
    print("小甲鱼是小姐姐!")
else:
    print("小甲鱼不是小姐姐!")

# 3. 判断多个条件,如果第1个条件不成立,则继续判断第2个条件,如果第2个条件也不成立,则继续判断第3个条件
score = int(input("请输入你的分数："))
score = int(score)

if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")  

# 4. 在第三种情况下加一个else,表示上面条件均不成立的情况下,执行某条语句或代码块
if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")  
else:
    print("请输入0-100之间的分值!")

# 5. 条件成立时执行的语句 if condition else 条件不成立时执行的语句
# 5.1 简单条件判断
age = 16
if age < 18:
    print("抱歉，未满18岁禁止访问。")
else:
    print("欢迎您来^o^")

print("抱歉，未满18岁禁止访问。") if age < 18 else print("欢迎您来^o^")

a = 3
b = 5
if a <b:
    small = a
else:
    small = b

small = a if a < b else b
print(small)

# 5.2 多条件判断
score = 66
level = ( 'D' if 0 <= score < 60 else 
          'C' if 60 <= score < 80 else 
          'B' if 80 <= score < 90 else 
          'A' if 90 <= score < 100 else 
          'S' if score == 100 else '请输入0-100之间的分值!')
print(level)

# 6. 嵌套条件判断
age = 18
isMale = True
if age < 18:
    print("抱歉，未满18岁禁止访问。")
else: 
    if isMale:
        print("任君选购！")
    else:
        print("抱歉,本店商品可能不适合小公举哦~")

print("抱歉，未满18岁禁止访问。") if age < 18 else print("任君选购！") if isMale else print("抱歉，本店商品可能不适合小公举哦~")






# # 练习题:判断一个整数是奇数还是偶数
# number = input("请输入一个整数：")
# number = int(number)

# if number % 2 == 0:
#     print(number, "是一个偶数。", sep='')
# else:
#     print(number, "是一个奇数。", sep='')

# profit = float(input("请输入今年的利润："))

# # 练习题:根据利润计算奖金
# if profit <= 100000:
#     reward = profit * 0.1
# elif 100000 < profit <= 200000:
#     reward = 100000 * 0.1 + (profit - 100000) * 0.075
# elif 200000 < profit <= 400000:
#     reward = 100000 * 0.1 + 100000 * 0.075 + (profit - 200000) * 0.05
# elif 400000 < profit <= 600000:
#     reward = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
# elif 600000 < profit <= 1000000:
#     reward = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015
# else:
#     reward = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01
    
    
# # 练习题: 将下面的条件分支语句,使用条件表达式实现
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#         print(c)

# (print(a) if a < c else print(c)) if a < b else (print(b) if b < c else print(c))

# # 练习题: 验证角谷猜想: 对于任意一个自然数,如果是偶数,则除以2,如果是奇数,则乘以3加1,得到一个新的自然数,按照这样的方法计算下去,最终结果为1.
# n = int(input("请输入一个自然数："))
    
# while n > 0:
#     if n % 2 == 0:
#         print(n, "/2 = ", n // 2, sep='')
#         n = n // 2
#     else:
#         print(n, "*3+1 = ", n * 3 + 1, sep='')
#         n = n * 3 + 1
#     if n == 1:
#         break