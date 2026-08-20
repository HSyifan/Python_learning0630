"""函数的闭包"""
# 闭包 = 一个函数 + 它“记住”的外层变量。
def myfunc():
    x = 520
    print(x)

myfunc() # 520

# print(x) # NameError: name 'x' is not defined

def funA():
    x = 880
    def funB():
        print(x)
    funB()

# funB() # NameError: name 'x' is not defined
funA() # 880

# 不通过funA来调用funB
def funA():
    x = 880
    def funB():
        print(x)
    return funB # 不用加（），因为加了（）就是调用函数了

funA() # <function funA.<locals>.funB at 0x0000023688423040>
funA()() # 880

funny = funA()
# funA() 执行完按理说 x = 880 该“消失”了，但 funny() 还能打印 880
# 这里 funny 是 funA 函数返回的 funB 函数，所以 funny() 就是调用 funB 函数
funny() # 880

"""工厂功能"""
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of # 返回的是 exp_of 函数，不是 exp_of()

# power 相当于一个工厂，根据传入的参数，返回不同的函数
square = power(2)
cube = power(3)

print(square(2)) # 4
print(square(5)) # 25

print(cube(2)) # 8
print(cube(5)) # 125

def outer():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1 # 这里将外层函数的x = 0 变成了 x = 1
        y += y1 # 等下一次函数再调用时，外层的x 不是0，而是1
        print(f"现在，x = {x}, y = {y}")
    return inner

move = outer()
move(1, 2) # 现在，x = 1, y = 2
move(-2, 2) # 现在，x = -1, y = 4


# 小乌龟移动的游戏，展示闭包
origin = (0, 0)          # 这个是原点
legal_x = [-100, 100]    # 限定 x 轴的移动范围
legal_y = [-100, 100]    # 限定 y 轴的移动范围

def create(pos_x=0, pos_y=0):
    def moving(direction, step):
        # 没有 nonlocal，moving 里改 pos_x 只会新建局部变量，下次调用又变回 0。
        # 有了 nonlocal，改的是闭包里的那份 pos_x、pos_y
        nonlocal pos_x, pos_y
        new_x = pos_x + direction[0] * step
        new_y = pos_y + direction[1] * step

        if new_x < legal_x[0]:
            pos_x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            pos_x = legal_x[1] - (new_x - legal_x[1])
        else:
            pos_x = new_x

        if new_y < legal_y[0]:
            pos_y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y

        return pos_x, pos_y

    return moving

# 你不能写 print(pos_x)，因为 pos_x 不在全局，只在 create 的闭包空间里。
# 只能通过 move(...) 来读、改位置——这就是封装：数据藏在函数内部。
move = create()
print("向右移动20步后，位置是：", move((1, 0), 20)) # (20, 0)
print("向上移动120步后，位置是：", move((0, 1), 120)) # (20, 120)
print("向右下角移动88步后，位置是：", move((1, -1), 88)) # (92, -8)


# 练习题：
def outter():
    def innerA():
        x = 100
    
    def innerB():
        nonlocal x
        x = 250
    
    def innerC():
        global x
        x = 520
    
    x = 880
    
    innerA()
    print(f"调用完 innerA() 函数之后，x = {x}")
    
    innerB()
    print(f"调用完 innerB() 函数之后，x = {x}")
    
    innerC()
    print(f"调用完 innerC() 函数之后，x = {x}")
    
outter()
print(f"此时此刻，全局变量 x = {x}")


# 请定义 funA() 函数，使其调用结果如下。
def funA(a):
    def funB(b):
        def funC(c):
            print(a * b * c)
        return funC
    return funB

funA(3)(4)(5)
# 60

# 请将下面这个闭包函数转换为 lambda 表达式的形式
# def maker(n):
#     def action(x):
#         return x ** n
#     return action
# f = maker(2)
# f(3)
# f(5)

# maker = lambda n: lambda x: x ** n


# 动动手0：请设计一个函数，每次调用传入一个参数，并返回所有参数的平均值。

def make_avg():
    total = 0   # 闭包里记住：所有数字的总和
    count = 0   # 闭包里记住：一共传了几个数
    def avg(x):
        nonlocal total, count
        total += x
        count += 1
        print(total / count)
    return avg

avg = make_avg()
avg(5)   # 5.0 第一次调用，只有 1 个参数，平均值是 5
avg(3)   # 4.0  第二次调用，(5 + 3) / 2
avg(7)   # 5.0  第三次调用，(5 + 3 + 7) / 3
avg(19)  # 8.5  第四次调用，(5 + 3 + 7 + 19) / 4


# 列表版本的平均值计算
def make_avg():
    values = []
    def averager(value):
        values.append(value)
        total = sum(values)
        return total / len(values)
    return averager

    

# 动动手1：请设计一个闭包函数，它的功能是每次调用返回一个斐波那契数列。

def fib():
    a, b = 0, 1
    def inner():
        nonlocal a, b
        print(a)
        a, b = b, a + b # 同时赋值，先计算右边的表达式，再赋值给左边
        # 相当于：
        # old_a = a
        # a = b
        # b = old_a + b
        
        # 这样写就是先赋值给a，a的值就变了。再赋值给b，这样就错了
        # a = b 
        # b = a + b
    return inner

f = fib()
f() # 0
f() # 1
f() # 1
f() # 2
f() # 3
f() # 5
f() # 8
f() # 13
f() # 21









































