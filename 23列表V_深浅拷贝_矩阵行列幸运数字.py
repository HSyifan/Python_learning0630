x =  [1, 2, 3]
y = x

# 浅拷贝
y = x.copy()
x[1] = 1
print(x, y) # [1, 1, 3] [1, 2, 3]

x = [1, 2, 3]
y = x[:]
print(x, y) # [1, 2, 3] [1, 2, 3]

# 浅拷贝对嵌套对象来说，只拷贝最外层，内层对象还是引用
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = x.copy()
x[1][2] = 0 # 修改了x的第二个元素的第三个元素, 改6为0
print(x, y) # x和y的第二个元素的第三个元素都变成了0

# 深拷贝
import copy
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = copy.copy(x) # 浅拷贝
x[1][2] = 0
print(x, y) # [[1, 2, 3], [4, 5, 0], [7, 8, 9]] [[1, 2, 3], [4, 5, 0], [7, 8, 9]]

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = copy.deepcopy(x) # 深拷贝
x[1][2] = 0
print(x, y) # [[1, 2, 3], [4, 5, 0], [7, 8, 9]] [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 练习题
x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()
y.append(7)
y[1].append(8)
print(x, y)

# 练习题
x = 1
y = x
x = 2
print(x, y)

#
s = [1]
s.append(s)
print(s) # [1, [...]]

# 练习题：创建一个 88 x 88 的随机整数矩阵（二维列表），然后匹配用户输入的整数是否与其中某元素相等，如果相等则打印其行号和列号。
# 要求1：随机整数取值范围 0~1024
# 要求2：需找出所有匹配的元素

import random

# 创建 88 x 88 的二维矩阵
nums = []
for i in range(88):
    row = [] # 每行都新建一个列表，一行一行地创建
    for j in range(88):
        row.append(random.randint(0, 1024))
    nums.append(row) # j就是一行有多少元素，也就是列数，i是行号，所以是nums[i][j]
# 用列表推导式创建 88 x 88 的二维矩阵：nums = [[random.randint(0, 1024) for j in range(88)] for i in range(88)]

target = int(input("请输入一个待匹配的整数："))

isFind = False
for i in range(88):          # 行号
    for j in range(88):      # 列号
        if nums[i][j] == target:
            print(i, j)      # 打印行号和列号
            isFind = True

if isFind == False:
    print("找不到！")

# 练习题1： 请编程找出矩阵中的幸运数字。
# 说明：假设给定一个 m * n 的矩阵（矩阵中数值的取值范围是 0~1024，且各不相同），如果某一个元素的值在同一行的所有元素中最小，并且在同一列的所有元素中最大，那么该元素便是幸运数字。
# 假设给定的矩阵如下：matrix = [[10, 36, 52], [33, 24, 88], [66, 76, 99]]，那么输出结果应该是 66（同时满足同一行的所有元素中最小，并且在同一列的所有元素中最大）。
matrix = [[10, 36, 52], [33, 24, 88], [66, 76, 99]]
for i in range(len(matrix)):  # i = 行号
    for j in range(len(matrix[i])): # j = 列号
        # 同行最小：min(matrix[i])
        # 同列最大：要把每一行的第 j 个元素拿出来再求 max
        col_max = max(matrix[k][j] for k in range(len(matrix))) # k = 行号。k独立于i，col_max表示本列的最大值
        if matrix[i][j] == min(matrix[i]) and matrix[i][j] == col_max: # 看是不是本行最小，本列最大
            print(matrix[i][j])




