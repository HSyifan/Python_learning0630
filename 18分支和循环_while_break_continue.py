"""while循环: 一直做到不满足条件为止"""
# love = "yes"
# while love == "yes":
#     love = input("今天你还爱我吗？")

# 求100以内所有整数的和
# i = 1
# sum = 0
# while i <= 100:
#     sum += i # sum = sum + i
#     i += 1 # i = i + 1

print(sum)

"""break语句: 跳出循环"""
# while True:
#     answer = input("主人，我可以退出循环了吗？")
#     if answer == "yes":
#         break
#     print("哎，好累~~~") # 如果答案不是yes，则继续循环print("哎，好累~~~"),直到答案为yes为止,break语句跳出循环


"""continue语句: 跳过本次循环，继续下一次循环"""
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue # 当i是偶数的时候，跳过后面的print(i)语句，继续下一次循环
    print(i) # 1，3，5，7，9

"""else语句: 当循环条件不再为真时，else语句才会被执行"""
"""else的作用：可以检测循环是否正常结束"""
"""如果循环被break语句终止，else语句块不会被执行"""

# i = 1
# while i < 5:
#     print("循环内，i的值是：", i)
#     i += 1
# else:
#     print("循环外，i的值是：", i)

i = 1
while i < 5:
    print("循环内，i的值是：", i)
    if i == 2:
        break
    i += 1
else:
    print("循环外，i的值是：", i)

# 打卡小程序: else检测有没有完整学习7天
# day = 1
# while day <= 7:
#     answer = input("今天有好好学习吗？")
#     if answer != "yes":
#         break
#     day += 1
# else:
#     print("非常棒，你已经坚持了7天！")

"""循环嵌套: 在循环中嵌套另一个循环"""
# i = 1
# while i <= 9:
#     j = 1 # 内层循环变量初始化
#     while j <= i:
#         print(j, "*", i, "=", j * i, end="\t") # 打印乘法表
#         j += 1 # 内层循环变量加1
#     print() # 换行
#     i += 1 # 外层循环变量加1

"""break语句和continue语句只能作用于一层循环体"""
# day = 1
# hour = 1
# while day <= 7:
#     while hour <= 8:
#         print("今天我一定要坚持学习8个小时！")
#         hour += 1
#         if hour > 1:
#             break # 打印了7次。break语句只跳出内层循环，day + 1，继续执行外层循环
#     day += 1

# 练习题： 找出 10 以内的所有素数，如果不是素数，请打印出该合数对应的乘积公式。
n = 2 # 例如n=7，x=2，3，4，5，6，最后x为6检验的时候7 % 6 == 0 都不成立。如果n=6，x=2时候就成立了，然后就成功打印然后break，x不用变成3来继续验证。 
while n < 10:
    x = 2 
    while x < n:
        if n % x == 0: # 如果n能被x整除，则n是合数，打印出n=x*n//x
            print(n, "=", x, "*", n // x)
            break
        x += 1
    else:
        print(n, "是一个素数")
    n += 1

