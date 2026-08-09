"""列表的加法"""
s = [1, 2, 3]
t = [4, 5, 6]
print(s + t) # [1, 2, 3, 4, 5, 6]

s * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

"""列表的嵌套"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]]
print(matrix) 

"""访问嵌套列表"""
for i in matrix:
    for each in i:
        print(each, end=' ')
    print() # 换行

print(matrix[0]) # [1, 2, 3]
print(matrix[0][0]) # 1

A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

B = [[0] * 3] * 3
print(B) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

A[1][1] = 1
B[1][1] = 1
print(A) # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(B) # [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

x = "FishC"
y = "FishC"
print(x is y) # True

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y) # False

print(A[0] is A[1]) # False
print(B[0] is B[1]) # True

# 练习题
print([[1, 2, 3], [4, 5, 6]] + [7, 8, 9])
print(len([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 出于性能优化方面的考虑，Python 在内部为 -5~256 范围内的整数维护了一个数组，起到缓存的作用。
a = 250
b = 250
print(a is b) # True

# 但是，如果超过了 -5~256 这个范围（大家可以自己动手测试一下），比如 1000，那么 Python 会为两个 1000 单独开辟两块不同的内存区域，因此 a is b 的结果为 False。
a = 1000
b = 1000
print(a is b) # True

# 练习题：创建三维列表 （3x3x3的矩阵）
three = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
         [[2, 2, 2], [2, 2, 2], [2, 2, 2]]]

# 练习题：请根据下面的内存关系图，分别创建出 x、y 和 z 三个不同的列表。
A = [0] * 2
print(A) # [0, 0]

x = [[0] * 2] * 3
print(x) # [[0, 0], [0, 0], [0, 0]]

y = [1] * 3 # [1]在这里先开辟3个内存，然后再把新的i的值赋予这3个内存
for i in range(3):
    y[i] = [0] * 2
print(y) # [[0, 0], [0, 0], [0, 0]]

z = [0] * 3
for i in range(3):
    z[i] = [0] * 3
    for j in range(3):
        z[i][j] = [1] * 2
print(z) # [[[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]]]


# 练习题：“摩尔投票法”，这种方法尤其适用于在任意多的选项中找到数量占比最多的那一个。
# 这一次我们修改一下要求，编写代码，利用“摩尔投票法”来找出占比数量最多的两个元素（注意：这两个元素的数量都需要超过总数的三分之一）。
nums = [1, 1, 2, 1, 3, 2, 3, 2]
 
major1 = major2 = nums[0]
count1 = count2 = 0
    
# 对抗阶段
for each in nums:
    if major1 == each:
        count1 += 1
        continue
    
    if major2 == each:
        count2 += 1
        continue
    
    if count1 == 0:
        major1 = each
        count1 = 1
        continue
    
    if count2 == 0:
        major2 = each
        count2 = 1
        continue
    
    count1 -= 1
    count2 -= 1
    
# 统计阶段
if nums.count(major1) > len(nums) / 3:
    print(major1)
if nums.count(major2) > len(nums) / 3:
    print(major2)


# 上面if continue的等价写法。
# 这一轮只走其中一条路，走完就结束本轮，然后进行下一轮。
# if major1 == each:
#     count1 += 1
# elif major2 == each:
#     count2 += 1
# elif count1 == 0:
#     major1 = each
#     count1 = 1
# elif count2 == 0:
#     major2 = each
#     count2 = 1
# else:
#     count1 -= 1
#     count2 -= 1