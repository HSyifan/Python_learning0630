"""lambda函数"""
# 不管最后的 lambda 表达式多么复杂，“冒号的左侧是参数,右侧是返回值“ 这个事实都不会改变！
# 匿名函数，一行流，处理简单的函数
# lambda arg1, arg2, ... : expression
# 传统形式：
# def <lambda>(arg1, arg2, ...): 
#     return expression

def squareX(x):
    return x * x

print(squareX(3)) # 9

# lambda表达式就是函数的引用
squareY = lambda y: y * y
print(squareY(3)) # 9

print(squareX) # <function squareX at 0x000002EE99B0CA40>
print(squareY) # <function <lambda> at 0x000002EE99D58F40>
print(squareX(3) == squareY(3)) # True
print(squareX(3) is squareY(3)) # True

# lambda表达式可以作为列表中的元素
y = [lambda x: x * x, 2, 3]
print(y[0](y[1])) # 4
print(y[0](y[2])) # 9

# map()函数结合lambda表达式使用
mapped = map(lambda x : ord(x) + 10, "FishC")
print(list(mapped)) # [80, 115, 125, 114, 77]

def boring(x):
    return ord(x) + 10
print(list(map(boring, "FishC"))) # [80, 115, 125, 114, 77]

# filter()函数结合lambda表达式使用
print(list(filter(lambda x : x % 2, range(10)))) # [1, 3, 5, 7, 9]


# 练习题：
def func(x, y, z):
    return x + y + z

def squareX(x):
    return x * x
y = [squareX, 2, 3]
print(y[0](y[1])) # 4

print(list(map(lambda x: x ** 2, range(10)))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(filter(lambda x: x % 2, range(10)))) # [1, 3, 5, 7, 9]

# 请将下面的闭包函数写成 lambda 表达式的实现形式
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)
cube = power(3)
print(square(2)) # 4
print(cube(5)) # 125

power = lambda exp: lambda base: base ** exp
square = power(2)
cube = power(3)
print(square(2)) # 4
print(cube(5)) # 125

# 请将下面三个装饰器函数写成 lambda 表达式的实现形式
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
    
def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner
    
def square(func):
    def inner():
        x = func()
        return x * x
    return inner
    
@add
@cube
@square
def test():
    return 2 
print(test()) # 65

add = lambda func: lambda: func() + 1
cube = lambda func: lambda: func() * func() * func()
square = lambda func: lambda: func() * func()
test = add(cube(square(lambda: 2)))
print(test()) # 65
# func() + 1是值，func是参数。因为func也是作为参数传入add的。

# 答案：
@lambda func: lambda : func() + 1
@lambda func: lambda : func() * func() * func()
@lambda func: lambda : func() * func()
def test():
    return 2
print(test()) # 65

# 动动手0：请使用 lambda 表达式和 filter() 函数配合，替换下面代码清单中的 for 循环。
power = {"吕布":999, "关羽":888, "刘备":666, "张飞":900, "赵云":789, "不二如是":999}
    
# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
greater = []
for k, v in power.items():
    if v > 800:
        greater.append((k,v))
    
print(greater)
[('吕布', 999), ('关羽', 888), ('张飞', 900), ('不二如是', 999)]

print(list(filter(lambda x: x[1] > 800, power.items()))) # [('吕布', 999), ('关羽', 888), ('张飞', 900), ('不二如是', 999)]
# filter(函数, 可迭代对象)
# 所以：x 就是 power.items() 里的「当前这一项」。


# 动动手1：请用一行代码找出猪队友。
# 假如有一个比赛，团队的最终得分是由每个成员的得分相加而来……因此，团队成员得分最低的，我们尊称其为 “猪队友”~
# 请使用一行代码，找到每个队伍的 “猪队友”（给大家降低一点难度，我们假设同一团队中，每位成员的得分均不相同）。

members = {
    "鱼C工作室" : {"小甲鱼":83, "不二如是":89, "二师兄":64, "小师妹":75, "鱼小二":96},
    "复仇者联盟" : {"钢铁侠":85, "绿巨人":39, "黑寡妇":82, "鹰眼":73, "雷神":99},
    "奥特曼家族" : {"迪迦":99, "艾斯":84, "泰罗":63, "佐菲":78, "赛文":78}}

# 请在此处添加一行代码，完成题目要求，并将结果保存在变量 x 中
x = [team + ':' + min(scores, key=lambda name: scores[name]) for team, scores in members.items()]
# min(候选池， key = 函数) 函数：返回值最小的元素
# lambda name: scores[name] 返回的是scores[name], 是每个团队中成员的得分
# 对字典比较来说，min函数就会按照分数scores[name]来找到最低的成员，返回其名字

print(x)
# ['鱼C工作室:二师兄', '复仇者联盟:绿巨人', '奥特曼家族:泰罗']



































