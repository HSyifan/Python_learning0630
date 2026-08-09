# 循环：通过迭代来逐个修改原列表的元素
oho = [1, 2, 3, 4, 5]
for i in range(len(oho)):
    oho[i] = oho[i] * 2

print(oho) # [2, 4, 6, 8, 10]

"""列表推导式：[表达式 for 变量 in 列表]"""
# 列表推导式直接创建新列表，再赋值给原列表
oho = [1, 2, 3, 4, 5]
oho = [i * 2 for i in oho]
print(oho) # [2, 4, 6, 8, 10]

x = [i for i in range(10)] # 最终由表达式决定
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i + 1 for i in range(10)]
print(x) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

x = []
for i in range(10):
    x.append(i + 1)
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = [c * 2 for c in "FishC"]
print(y) # ['FF', 'ii', 'ss', 'hh', 'CC']

code = [ord(c) for c in "FishC"] # ord() 函数返回字符的 ASCII 值
print(code) # [70, 105, 115, 104, 67]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in matrix] # 取每行的第 2 个元素
print(col2) # [2, 5, 8]

# 这里的i是索引值，不是元素值[0][0], [1][1], [2][2]
diag = [matrix[i][i] for i in range(len(matrix))] # 取对角线元素
print(diag) # [1, 5, 9]


# 练习题0
ans0 = [i**2 for i in range(1, 7)]
print(ans0) 

# 练习题1
matrix1 = [[i, i + 2] for i in range(6)]
print(matrix1)

# 练习题2
double = []
for i in "FishC":
    double.append(i * 2)
print(double)

# 练习题3
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
diag = []
for i in range(len(matrix)):
    i *= matrix[i][i] # i = i * matrix[i][i]
    diag.append(i)
print(diag)

diag = [i * matrix[i][i] for i in range(len(matrix))]
print(diag)

# 练习题4
x = "FishC"
y = [x for x in "123"]
print(x, y)

# 练习题5: 如何获取矩阵从右上角到左下角这条对角线上的元素
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

ans5 = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
print(ans5)

# 动动手0：打印杨辉三角形
# 杨辉三角形第i行j列的值 = 第 (i-1) 行 (j-1) 列的值 + 第 (i-1) 行 (j) 列的值
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1

# 初始化杨辉三角形
# 创建一个10*10的二维列表，并将所有的元素初始化为0
triangle = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    triangle.append(row)

# 计算杨辉三角形
# 根据观察，我们知道杨辉三角形左右两边的元素均为1
for i in range(10):
    triangle[i][0] = 1
    triangle[i][i] = 1

# 第i行j列的值 = 第(i-1)行(j-1)列的值 + 第(i-1)行(j)列的值
for i in range(2, 10):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

# 输出杨辉三角形
for i in range(10):
    for j in range(i+1): # 打印第i行的前i+1个元素
        print(triangle[i][j], end=" ")
    print()


# 动动手1：更改杨辉三角形的打印样式
# 初始化杨辉三角形
# 创建一个10*10的二维列表，并将所有的元素初始化为0
triangle = []
for i in range(10):
    triangle.append([])
    for j in range(10):
        triangle[i].append(0)
    
# 计算杨辉三角形
# 根据观察，我们知道杨辉三角形左右两边的元素均为1
for i in range(10):
    triangle[i][0] = 1
    triangle[i][i] = 1
    
# 第i行j列的值 = 第(i-1)行(j-1)列的值 + 第(i-1)行(j)列的值
for i in range(2, 10):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
# 输出杨辉三角形
for i in range(10):
    # 因为是三角形，所以i越小，前边需要填充的TAB越多
    for k in range((10-i)//2):
        print('\t', end='')
    for j in range(i+1):
        # 要形成“隔行错开”的效果，所以我们在偶数行加4个空格
        if i % 2 == 1:
            print("    ", end='')
        # 为何要使用TAB而非空格，大家可以将下面的end='\t'改成对应的空格数即可知晓
        print(triangle[i][j], end='\t')
    print()