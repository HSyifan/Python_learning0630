"""递归"""
# 函数调用自身的过程

def funA():
    print("AWBDYL")

def funB():
    funA()
funB() # AWBDYL

# def funC():
#     print("AWBDYL")
#     funC()
# funC() # 递归错误：超过最大递归深度

def funC(i):
    if i > 0:
        print("AWBDYL")
        i -= 1
        funC(i)
funC(10) # AWBDYL 10 次

"""求一个数的阶乘"""
# 使用迭代
def factIter(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
print(factIter(5)) # 120
print(factIter(10)) # 3628800

# 使用递归
def factRecur(n):
    if n == 1:
        return 1
    else:
        return n * factRecur(n-1)
print(factRecur(5)) # 120
print(factRecur(10)) # 3628800

"""斐波那契数列"""
# 使用迭代
def fibIter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c
print(fibIter(12)) # 144
print(fibIter(120)) # 5358359254990966640871840

# 使用递归
# 递归非常消耗内存
def fibRecur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)
print(fibRecur(12)) # 144
# print(fibRecur(120)) # 反应很久很久


# 练习题：
# 下面代码利用递归实现将列表的各个元素进行相加，请补全红色方框中的代码，使其能够成功执行并获取结果。
def recsum(x):
    if not x:
        return 0
    else:
        return x[0] + recsum(x[1:])
print(recsum([1, 2, 3, 4, 5])) # 15

# 下面代码利用递归实现将嵌套列表的各个元素进行相加，请补全红色方框中的代码，使其能够成功执行并获取结果。
def sumtree(x):
    total = 0
    for i in x:
        if type(i) is not list:
            total += i
        else:
            total += sumtree(i)
    return total
print(sumtree([1, 2, 3, [4, 5, [6, 7, 8, [9, 10]]]])) # 55


# 动动手0：请动手优化课堂中递归实现斐波那契的代码。
# 原始代码：
# def fibRecur(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibRecur(n-1) + fibRecur(n-2)
# print(fibRecur(12)) # 144
# # print(fibRecur(120)) # 反应很久很久

# 优化：
# def fibRecur_opt(n, cache=None):
#     if cache is None:
#         cache = {}
#     if n in cache:
#         return cache[n]
#     if n == 1 or n == 2:
#         return 1
#     cache[n] = fibRecur_opt(n - 1, cache) + fibRecur_opt(n - 2, cache)
#     return cache[n]

# print(fibRecur_opt(120)) # 5358359254990966640871840

# 答案：
# 这里优化的技巧就是尽可能地将更多的操作放到参数中去实现
# Guido van Rossum 认为递归并不是 Python 的核心特性，如果需要大量递归，那么可能应该选择其他语言，或者改写代码使用循环结构更合适。
def tailFibRecur(n, x, y):
    if n == 1 or n == 2:
        return y
    else:
        return tailFibRecur(n-1, y, x+y)
tailFibRecur(12, 1, 1)



# 动动手1：请编写代码，统计使用课堂中的普通递归算法，上一题优化后的递归算法，以及迭代计算斐波那契数列的运行时间。
# 为了时间上的考虑，我们仅对比计算斐波那契数列第 12 位数的值：
import timeit

t1 = timeit.timeit("fibRecur(12)", setup="from __main__ import fibRecur")
t2 = timeit.timeit("fibIter(12)", setup="from __main__ import fibIter")
t3 = timeit.timeit("fibRecur_opt(12)", setup="from __main__ import fibRecur_opt")

print(f"普通递归消耗: {round(t1, 6)}秒。")
print(f"优化递归消耗: {round(t2, 6)}秒。")
print(f"普通迭代消耗: {round(t3, 6)}秒。")











































