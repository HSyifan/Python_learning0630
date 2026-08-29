"""元组与列表区别"""
# 元组(),也可以不带括号; 列表[]
# 元组是不可变的, 列表是可变的

rhyme = (1, 2, 3, 4, 5, "上山打老虎")
print(rhyme)
rhyme = 1, 2, 3, 4, 5, "上山打老虎"
print(rhyme)

print(rhyme[0])
print(rhyme[-1])

# rhyme[1] = 10
# print(rhyme) # 报错, 元组是不可变的

"""元组的切片"""
# 切片是把片段导出成新的对象，不改变元组本身
print(rhyme[:3])
print(rhyme[3:])
print(rhyme[:])
print(rhyme[::-1])

# 元组可以count()和index()
nums = (3, 1, 9, 6, 8, 3, 5, 3)
print(nums.count(3))

heros = ("蜘蛛侠", "绿巨人", "黑寡妇")
print(heros.index("黑寡妇"))

# 元组的相加
s = (1, 2, 3)
t = (4, 5, 6)
print(s + t)
print(s * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 元组的嵌套
# 注意写法，元组嵌套的括号要加
w = (s, t) # ((1, 2, 3), (4, 5, 6))
print(w)
# w = s + t # (1, 2, 3, 4, 5, 6)
# print(w)

for each in s:
    print(each)

for i in w:
    for each in i:
        print(each)

# 列表推导式(不存在元组推导式)
s = (1, 2, 3, 4, 5)
print([each * 2 for each in s]) # [2, 4, 6, 8, 10]
print((each * 2 for each in s)) # 生成器 <generator object <genexpr> at 0x0000027B3C1335E0>

# 元组只有一个元素时，要加逗号
x = (520)
print(type(x)) # type 查看类型为int
y = (520,)
print(type(y)) # type 查看类型为tuple元组

# 元组的解包
t = (123, "FishC", 3.14)
x, y, z = t
print(x, y, z)

# 列表的解包
t = [123, "FishC", 3.14]
x, y, z = t
print(x, y, z)

# 字符串的解包
# 赋值号左边的个数必须等于右侧序列的元素的个数
a, b, c, d, e = "FishC"
print(a, b, c, d, e)

# a, b, c, = "FishC" # 报错
a, b, *c, = "FishC" # *c 表示剩下的所有元素都赋值给c
print(a, b, c) 

# 赋值的逻辑
x, y = 10, 20
print(x, y)

_ = (10, 20) # 先通过_ 接住(10, 20)这个元组
x, y = _ # 再通过解包将(10, 20)赋值给x, y
print(x, y)

# 元组的元素内容（指向一个可变列表）是可变的，但是元组本身是不可变的
s = [1, 2, 3]
t = [4, 5, 6]
w = (s, t)
print(w) # ([1, 2, 3], [4, 5, 6])

w[0][0] = 0
print(w) # ([0, 2, 3], [4, 5, 6])

# 练习题1：
t = (3, 1, 4, 9, 8)
# t.sort() # 报错，元组是不可变的
print(sorted(t)) # [1, 3, 4, 8, 9]

# 练习题8：有一天，居委会的大妈找上门，让你帮她用 Python 创建一个对象，用于登记接种新冠疫苗的情况。登记内容包含（姓名、生日、接种日期），你应该怎么做？
# 比较恰当的方法是使用列表来存储，然后由于每个人登记的内容是不需要改变的，所以可以用元组打包。
# 这样添加一个新的登记就只需要 checked.append(("关习习", 20000220, 20210806))
checked = [("口口布", 19910220, 20210601), ("弓长飞", 19630509, 20210623), ("刘Baby", 19990520, 20210520)]

# 动动手：想知道到底是创建列表的速度快，还是创建元组的速度快，应该如何做呢？
# 请编写代码，测试一下到底是创建列表的速度快，还是创建元组的速度快？为了得到更精准的数据，请重复测试 100 次，并分别计算出平均时间。
import timeit
print(timeit.timeit('x = 123')) # 0.01202020002529025
print(timeit.timeit('x = 123', number=1)) # 9.620003402233124e-05

test = timeit.repeat('x = 123', repeat=10)
print(test)

test_list = timeit.repeat('x = [1, 2, 3]', repeat=100)
test_tuple = timeit.repeat('x = (1, 2, 3)', repeat=100)

avg_list = sum(test_list) / len(test_list)
avg_tuple = sum(test_tuple) / len(test_tuple)

print("创建列表的平均时间是：", avg_list) 
print("创建元组的平均时间是：", avg_tuple)

if avg_list < avg_tuple:
    print("创建列表的速度快")
else:
    print("创建元组的速度快")


