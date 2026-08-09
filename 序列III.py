x = [1, 1, 0]
y = [1, 1, 9]

"""all()和any()函数"""
# all()函数：如果所有元素都为真，则返回True，否则返回False
# any()函数：如果至少有一个元素为真，则返回True，否则返回False

print(all(x)) # False
print(all(y)) # True

print(any(x)) # True
print(any(y)) # True

# enumerate()函数：返回一个枚举对象，包含索引和元素
season = ["Spring", "Summer", "Fall", "Winter"]
print(enumerate(season)) #　<enumerate object at 0x00000260A577AD90>
print(list(enumerate(season))) 
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

print(list(enumerate(season, 10))) # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#　[(10, 'Spring'), (11, 'Summer'), (12, 'Fall'), (13, 'Winter')]   

# zip()函数：返回一个元组，将两个序列合并，返回一个元组

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped)) # [(1, 4), (2, 5), (3, 6)]

z = [7, 8, 9]
zipped = zip(x, y, z)
print(list(zipped)) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# 如果两个序列的长度不一致，则返回长度最短的序列的长度
z = "FishC"
zipped = zip(x, y, z)
print(list(zipped)) # [(1, 4, 'F'), (2, 5, 'i'), (3, 6, 's')]

# zip_longest()函数：返回一个元组，如果两个序列的长度不一致，则返回长度最长的序列的长度
import itertools
zipped = itertools.zip_longest(x, y, z)
print(list(zipped)) 
# [(1, 4, 'F'), (2, 5, 'i'), (3, 6, 's'), (None, None, 'h'), (None, None, 'C')]

# map()函数：返回一个迭代器，将一个函数应用到序列的每个元素，返回一个迭代器
# ord()函数：返回一个字符的ASCII码
mapped = map(ord, "FishC")
print(list(mapped)) # [70, 105, 115, 104, 67]

# pow()函数：返回一个数的幂
mapped = map(pow, [2, 3, 10], [5, 2, 3])
print(list(mapped)) # [32, 9, 1000]

# 如果传入多个，但是函数只需要前面两个，后面的参数会被忽略
print(list(map(max, [1, 3, 5], [2, 2, 2], [0, 3, 9, 8]))) # [2, 3, 9]

# filter()函数：计算结果为真的元素构成的迭代器.过滤函数+待过滤序列
print(list(filter(str.islower, "FishC"))) # ['i', 's', 'h']

"""迭代器与可迭代对象"""
# 一个迭代器肯定是一个可迭代对象
# 可迭代对象可重复使用，而迭代器只能被使用一次

mapped = map(ord, "FishC")
for each in mapped:
    print(each)

print(list(mapped)) # []

# iter()函数：将一个可迭代对象转换为迭代器
x = [1, 2, 3, 4, 5]
y = iter(x)

print(type(x)) # <class 'list'>
print(type(y)) # <class 'list_iterator'>

# next()函数：将迭代器中的元素提取出来
print(next(y)) # 1
print(next(y)) # 2
print(next(y)) # 3
print(next(y)) # 4
print(next(y)) # 5
# print(next(y)) # StopIteration。异常

z = iter(x)
print(next(z, "没啦，被你掏空啦~")) # 1
print(next(z, "没啦，被你掏空啦~")) # 2
print(next(z, "没啦，被你掏空啦~")) # 3
print(next(z, "没啦，被你掏空啦~")) # 4
print(next(z, "没啦，被你掏空啦~")) # 5
print(next(z, "没啦，被你掏空啦~")) # 没啦，被你掏空啦~


# 练习题：

matrix = [[1, 3, 2],
           [5, 4, 6],
           [8, 7, 9]]
mapped = map(sorted, matrix)
print(list(mapped)) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(filter(str.islower, "FishC")))
print([x for x in "FishC" if x.islower()])

x = [1, 2, 3, 4, 5]
y = "FishC"

zipped = zip(x, y)
print(list(zipped))


# 动动手0：请使用学过的知识，自己动手编写代码，利用 for 循环语句，模拟 all()、any()、enumerate()、zip() 这4个函数的实现。

# all()函数
x = [1, 2, 0]
for each in x:
    if not each:
        print(False)
        break
else:
    print(True)

# any()函数
x = [1, 2, 0]
for each in x:
    if each:
        print(True)
        break
else:
    print(False)

# enumerate()函数
season = ["Spring", "Summer", "Fall", "Winter"]

result = []
for each in list(enumerate(season)):
    result.append(each)
print(result)

# zip()函数
x = [1, 2, 3]
y = [4, 5, 6]
z = "FishC"

result = []
for i in range(min(len(x), len(y), len(z))):
    result.append((x[i], y[i], z[i]))
print(result)

# 动动手1：假设有一个密室，每次只能放一个人进去，在进去之前和出来之后都要求摁一下门口的打卡机按钮，打卡机会依次将名字和进出时间戳记录为以下的格式：
# A 君是从时间戳为 0 的时候进入，从时间戳为 1 的时候出来，总共耗时为 1
# B 君是从时间戳为 1 的时候进入，从时间戳为 3 的时候出来，总共耗时为 2
# C 君是从时间戳为 3 的时候进入，从时间戳为 3.5 的时候出来，总共耗时为 0.5
# ...
# G 君是从时间戳为 10 的时候进入，从时间戳为 10.8 的时候出来，总共耗时为 0.8

times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]

time_intervals = []
for i in range(len(times)):
    if i == 0:
        time_intervals.append((times[i]))
    else:
        time_intervals.append(times[i] - times[i-1])
print(time_intervals)

fastest = min(time_intervals)
slowest = max(time_intervals)

fast_names = [names[i] for i in range(len(names)) if time_intervals[i] == fastest]
slow_names = [names[i] for i in range(len(names)) if time_intervals[i] == slowest]

print("速度最快的是：", fast_names, "，耗费时间是：", fastest)
print("速度最慢的是：", slow_names, "，耗费时间是：", slowest)


# fast_names = [n for n, t in zip(names, time_intervals) if t == fastest]
# slow_names = [n for n, t in zip(names, time_intervals) if t == slowest]
