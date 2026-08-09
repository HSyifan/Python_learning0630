"""列表"""
[1, 2, 3, 4, 5]
rhyme = [1, 2, 3, 4, 5, "上山打老虎"]
print(rhyme)

for each in rhyme:
    print(each)

print(rhyme[0])
print(rhyme[-1])
print(rhyme[len(rhyme) - 1])

"""列表的切片，左闭右开"""
print(rhyme[0:3]) # 1, 2, 3, 不包括索引为3的元素
print(rhyme[3:6]) # 4, 5, "上山打老虎", 不包括索引为6的元素
print(rhyme[:3]) # 1, 2, 3, 不包括索引为3的元素
print(rhyme[3:]) # 4, 5, "上山打老虎", 包括索引为3的元素
print(rhyme[:]) # 1, 2, 3, 4, 5, "上山打老虎", 全部元素

print(rhyme[0:6:2]) # 1, 3, 5
print(rhyme[::2]) # 1, 3, 5
print(rhyme[::-2]) # "上山打老虎", 4, 2
# 翻转列表，相当于将列表倒序
print(rhyme[::-1]) 

# 练习题：将两个列表合并成一个列表
list1 = [1, 2, 8, 9]
list2 = [3, 4, 5, 6, 7]

list1 = list1[:2] + list2 + list1[2:]
print(list1, end="\n \n \n")

# 练习题：0. 给定一个整数列表 nums 和一个目标值 target，请在该数组中找出和为目标值的两个元素，并将它们的数组下标值打印出来。
# 1. 输入一个整数列表，输入STOP结束
# nums = []
# while True:
#     temp = input("请输入一个整数（输入STOP结束）：")
#     if temp == "STOP":
#         break
#     nums.append(int(temp))
# target = int(input("请输入目标整数："))

# # 获取 nums 的长度，并将结果存放到 n 变量中 #
# n = len(nums)
# for i in range(n):
#     for j in range(i + 1, n):
#         if nums[i] + nums[j] == target:
#             # 将找到的两个元素下标值以列表的形式打印出来 #
#             print([i, j])

# 2. 最后，回忆前面我们学习过的 random 模块，生成一个由 10000 个整数（范围是 1 ~ 65535）构成的随机列表，目标值 target 由用户输入。
import random
nums = []
for i in range(10):
    nums.append(random.randint(1, 65535))
# 或者使用列表推导式
# nums = [random.randint(1, 65535) for i in range(10000)]
target = int(input("请输入目标整数："))

isFind = False
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            # 将找到的两个元素下标值以列表的形式打印出来 #
            print([i, j])
            isFind = True

if isFind == False:
    print("找不到！")





