import random

counts = int(input("请输入抛硬币的次数："))

# 利用 ignore 变量来判断是否打印每次的结果
if counts > 100:
    ignore = True
else:
    ignore = False

heads = 0 # 统计正面的次数
tails = 0 # 统计反面的次数

i = 0
print("开始抛硬币实验……")
while i < counts:
    num = random.randint(1, 10)

    if num % 2:
        heads += 1
        if not ignore:       
            print("正面", end=" ")
    else:
        tails += 1
        if not ignore:
            print("反面", end=" ")

    i += 1

print("")
print("一共模拟了", counts, "次抛硬币，结果如下：")
print("正面：", heads, "次", sep="")
print("反面：", tails, "次", sep="")
