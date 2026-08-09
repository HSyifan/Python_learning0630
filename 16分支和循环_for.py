for each in "FishC":
    print(each)

i = 0
while i < len("FishC"):
    print("FishC"[i])
    i += 1

"""range函数: 生成一个整数序列"""
# range(stop): 生成一个从0到stop-1的整数序列
# range(start, stop): 生成一个从start到stop-1的整数序列
# range(start, stop, step): 生成一个从start到stop-1的整数序列，步长为step

# for i in range(10): # 生成一个从0到9的整数序列
#     print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# for i in range(5, 10): # 生成一个从5到9的整数序列
#     print(i) # 5, 6, 7, 8, 9

# for i in range(5, 10, 2): # 生成一个从5到9的整数序列，步长为2
#     print(i) # 5, 7, 9

# for i in range(10, 5, -2): # 生成一个从10到0的整数序列，步长为-2
#     print(i) # 10, 8, 6

# 求1000以内所有整数的和
sum = 0
for i in range(1001):
    sum += i
print(sum)

# 找出 10 以内的所有素数，如果不是素数，请打印出该合数对应的乘积公式。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n // x)
            break
    else:
        print(n, "是一个素数")

# 练习题： 打印出10以内的所有整数
for i in range(10): 
    print(i, end=' ')
    i = 5

# 练习题： 打印出3到10的整数，步长为3，然后求和
a, b, c = range(3, 10, 3)
print(a) # 3
print(b) # 6
print(c) # 9
print(a + b + c) # 18

# 练习题： 打印出"FishC"和110的长度
# len("FishC") + len(110) 
# len() 函数的参数需要是一个序列或者集合（才能够获取长度嘛），整数是不能作为其参数的

# 练习题： 求-10到-100的整数，步长为-20，然后求和
# result = 0
# for each in range(-10, -100, -20):
#     result += each 
# print(result) # -250


# 练习题： 找出100到1000之间的所有水仙花数
for i in range(100, 1000):
    sum = 0
    temp = i # 将i的值赋给temp
    
    while temp: # 当temp不为0时，继续循环。
        sum = sum + (temp % 10) ** 3 # 计算temp的个位数的立方
        temp //= 10 # 将temp除以10，取整数部分。例如153 取15，15取1，1取0，0不为true，while结束
    
    if sum == i:
        print(i)

# 内循环：
# 第一轮：temp = 153，sum = 0 + 3^3 = 27， temp //= 10 = 15, temp = 15
# 第二轮：temp = 15，sum = 27 + 5^3 = 152， temp //= 10 = 1, temp = 1
# 第三轮：temp = 1，sum = 152 + 1^3 = 153, temp //= 10 = 0, temp = 0, while结束

# 练习题： 判断一个数是否是回文数
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
x = int(input("请输入一个正整数："))

if x < 0 or (x % 10 == 0 and x != 0):
    print("不是回文数。")
else:
    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10

    if x == revertedNumber or x == revertedNumber // 10:
        print("是回文数。")
    else:
        print("不是回文数。")