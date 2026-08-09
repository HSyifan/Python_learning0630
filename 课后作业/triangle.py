# 初始化杨辉三角形
# 创建一个10*10的二维列表，并将所有的元素初始化为0
triangle = []
for i in range(10):
    # 请在此处填写恰当的代码
    for j in range(10):
        # 请在此处填写恰当的代码

# 计算杨辉三角形
# 根据观察，我们知道杨辉三角形左右两边的元素均为1
for i in range(10):
    triangle[i][0] = 1
    # 请在此处填写恰当的代码

# 第i行j列的值 = 第(i-1)行(j-1)列的值 + 第(i-1)行(j)列的值
for i in range(2, 10):
    for j in range(1, i):
        # 请在此处填写恰当的代码

# 输出杨辉三角形
for i in range(10):
    for j in range(i+1):
        # 请在此处填写恰当的代码
    print()
