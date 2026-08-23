# 错误的创建列表，只是对原列表的应用，而不是创建新的列表
B = [[0] * 3] * 3
print(B) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B[1][1] = 1
print(B) # [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
A[1][1] = 1
print(A) # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

"""列表推导式创造二维列表"""
S = [[0] * 3 for i in range(3)] # i重复3次的意思，但是表达式里没有i。
print(S) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
S[1][1] = 1
print(S) # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

"""列表推导式if condition"""
even = [i for i in range(10) if i % 2 == 0] 
print(even) # [0, 2, 4, 6, 8]
even = [i + 1 for i in range(10) if i % 2 == 0] # 先执行for语句，再执行if语句，最后执行表达式。
print(even) # [1, 3, 5, 7, 9]

words = ["Great", "FishC", "Brilliant", "Excellent", "Fantastic"]
fwords = [w for w in words if w[0] == "F"] # 筛选5个字符串中以F开头的字符串
print(fwords) # ["FishC", "Fantastic"]

"""列表推导式嵌套循环"""
# 降级二维列表为一维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [col for row in matrix for col in row]
print(flatten) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 用循环的传统方法实现
flatten = []
for row in matrix:
    for col in row:
        flatten.append(col)
print(flatten) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

fishc = [x + y for x in "fishc" for y in "FiSHC"] 
print(fishc) 

_ = [] # 临时变量，用于存储中间结果
for x in "fishc":
    for y in "FiSHC":
        _.append(x + y)
print(_) # ['fs', 'fi', 'fh', 'fc', 'is', 'ii', 'ih', 'ic', 'hs', 'hi', 'hh', 'hc', 'cs', 'ci', 'ch', 'cc']

"""列表推导式for与if同时使用"""
_ = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(_) 

_ = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                _.append([x, y])
print(_) # [[0, 0], [0, 3], [0, 6], [2, 0], [2, 3], [2, 6], [4, 0], [4, 3], [4, 6], [6, 0], [6, 3], [6, 6], [8, 0], [8, 3], [8, 6]]

"""KISS原则：Keep It Simple Stupid"""

# 练习题1：请使用列表推导式创建一个 4 * 5 的二维列表，并将每个元素初始化为数字 8。
ans1 = [[8] * 5 for i in range(4)]
print(ans1)

# 练习题3：将下面的嵌套循环语句使用列表推导式实现。
result = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 2 != 0:
                result.append([x, y])

ans2 = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(ans2)

# 练习题4：请将下面 matrix 矩阵反向展开，即使得最终的结果为 [9, 8, 7, 6, 5, 4, 3, 2, 1]。
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

ans3 = [col for row in matrix[::-1] for col in row[::-1]]
ans3 = [col for row in matrix for col in row][::-1]
print(ans3)

# 练习题5：有 2 种颜色（"BLACK", "WHITE"）和 10 个码数（"WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"）的选择
# 请使用列表推导式，统计得出下面的结果
colors = ["BLACK", "WHITE"]
sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]

ans5 = [[x, y] for x in colors for y in sizes] 
print(ans5)

# 动动手0：请使用列表推导式，获得 matrix 矩阵的转置矩阵 Tmatrix（将 matrix 的行列互换之后得到的矩阵，称为 matrix 的转置矩阵）。
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

Tmatrix = []
for i in range(len(matrix[0])):   # i = 0,1,2,3  → 新矩阵要造 4 行
    row_new = []
    for row in matrix:            # 依次取出原矩阵的每一行
        row_new.append(row[i])    # 取这一行的第 i 个元素
    Tmatrix.append(row_new)
print(Tmatrix)

dds0 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(dds0)

# 动动手1：请按照顺时针螺旋顺序输出矩阵中的所有元素。
# 输出为：[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# 1 → 2 → 3 → 4
#             ↓
# 5 → 6 → 7   8
# ↑           ↓
# 9 ←10 ←11 ←12

#          top=0      right=3
#           ↓           ↓
# left=0 →  1   2   3   4
#           5   6   7   8
# bottom=2→ 9  10  11  12


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

# 获取二维列表的行数并存放到变量 rows 中
# 获取二维列表的列数并存放到变量 cols 中
rows = len(matrix)
cols = len(matrix[0])

left = 0          # 左边界列号
right = cols - 1  # 右边界列号 = 3
top = 0           # 上边界行号
bottom = rows - 1 # 下边界行号 = 2

result = []

while left <= right and top <= bottom:
    # 从左往右遍历
    for col in range(left, right + 1):  # col = 0,1,2,3
        result.append(matrix[top][col]) # 第 top 行

    # 从上往下遍历
    for row in range(top + 1, bottom + 1):  # row = 1,2（跳过已取过的4）
        result.append(matrix[row][right])   # 第3列

    if left < right and top < bottom: # 当只剩一行或一列时：上边 / 右边已经取完了，如果还走下边、左边，会重复或越界
        # 从右往左遍历
        for col in range(right - 1, left, -1): # col = 2,1（不取两端角）
            result.append(matrix[bottom][col]) # 第2行

        # 从下往上遍历
        for row in range(bottom, top, -1): # row = 2,1（不取已取过的1）
            result.append(matrix[row][left]) # 第0列

    left = left + 1
    right = right - 1
    top = top + 1
    bottom = bottom - 1

print(result)





