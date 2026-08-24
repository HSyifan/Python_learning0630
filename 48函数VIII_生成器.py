"""生成器"""
# 生成器：除了闭包和全局变量外，另一种可以记忆上下文的结构
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1

print(counter()) # <generator object counter at 0x000001F9C5B3D3C0>

# 生成器：一个制作工具。每次调用的时候，提供一个值，然后暂停，等待下一次调用。
# 列表，元组：一个容器，装多个生成好的值。
for i in counter():
    print(i) # 0 1 2 3 4 5

# 生成器：一种特殊迭代器。不走回头路，支持next()函数。
c = counter()
print(next(c)) # 0
print(next(c)) # 1
print(next(c)) # 2
print(next(c)) # 3
print(next(c)) # 4
print(next(c)) # 5
# print(next(c)) # StopIteration

c = counter()
# print(c[2]) # 报错

# 生成器实现斐波那契数列
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2
    
f = fib()
print(next(f)) # 0
print(next(f)) # 1
print(next(f)) # 1
print(next(f)) # 2
print(next(f)) # 3
print(next(f)) # 5
print(next(f)) # 8
print(next(f)) # 13
print(next(f)) # 21

# for i in f:
#     print(i)

"""生成器表达式"""
print((i ** 2 for i in range(10))) # <generator object <genexpr> at 0x0000018CC83AE670>

t = (i ** 2 for i in range(10))
print(next(t)) # 0
print(next(t)) # 1
print(next(t)) # 4
print(next(t)) # 9
print(next(t)) # 16
print(next(t)) # 25
print(next(t)) # 36
print(next(t)) # 49
print(next(t)) # 64
print(next(t)) # 81


# 练习题：
# 3. 你觉得生成器通常应用在什么场景会比较合适？
# 答：生成器应该应用在占用大量存储空间的文件操作上，比方说日志文件通常都特别大，
# 几十上百 G 都算是小弟弟了，如果一次性把它读取到内存中，可想而知结果就是爆内存；
# 另外一个应用场景就是希望输出的结果不断更新的情况，比如生成斐波那契数列，
# 我们希望它每次产生的结果是基于上次的数据进行再运算产生。

# 4. 请问下面代码会打印 “YES” 吗？
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
    print("YES")
for each in counter():
    print(each) # 会打印出0 1 2 3 4 5 YES

# 6. print([x ** 2 for x in range(1000000)]) # 会打印出1000000个数的平方
# 对于百万级运算，生成器（表达式）对比列表推导式的优势就显而易见了；
# 上面列表推导式代码，在多数电脑是要计算很久才能得到结果，因为它是实打实地在计算的；
# 而生成器表达式则是将算法保存起来，但并没有实际去计算，所以就可以做到 “秒回”。

# 7. 将下面的 map() 函数实现改为使用生成器表达式实现。
list(map(abs, (-1, 2, -3, 4, -5)))

print(list(abs(x) for x in (-1, 2, -3, 4, -5)))

# 请将下面的生成器表达式实现改为使用 filter() 函数实现。
print("".join(x for x in "FishC" if x.isupper()))

print(list(filter(lambda x: x.isupper(), "FishC")))

# 请问下面代码会打印什么内容？
print(list(map((lambda x : x ** 2), filter((lambda x : x % 2 == 0), range(10)))))
#  [0, 4, 16, 36, 64]


# 动动手：
# 利用生成器定义一个支持浮点数的 frange() 函数，其功能与 range() 函数相仿。
# 默认的步进值为 0.1：

def frange(start, end=None, step=0.1):
    s = str(step) 
    pre = len(s[s.find('.')+1:]) # 按步长自动决定保留几位
    start += 0.0 # 确保start变成浮点数

    if end is None:          # 只传一个参数时，start 默认为 0，该参数当作 end
        end = start + 0.0
        start = 0.0

    while start < end:
        yield round(start, pre)
        start += step

for i in frange(1):
    print(i)

for i in frange(1, 2):
    print(i)

for i in frange(5, 10, 0.5):
    print(i)




















