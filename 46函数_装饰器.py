""""""
# 把一个函数作为参数传递给另一个函数
def myfunc():
    print("正在调用myfunc...")

def report(func):
    print("主人，我要开始调用函数了...")
    func()
    print("主人，我调用完函数啦，快夸夸我^o^")

report(myfunc)

import time
def time_master(func):
    print("开始运行程序...")
    start = time.time() # 通过time模块的time函数获取当前时间戳
    func()
    stop = time.time()
    print("结束程序运行...")
    print(f"一共耗费了{(stop - start):.5f}秒。")

def myfunc():
    time.sleep(1)
    print("Hello FishC.")

time_master(myfunc)

"""装饰器"""
def time_master(func):
    def call_func():
        print("开始运行程序...")
        start = time.time() # 通过time模块的time函数获取当前时间戳
        func()
        stop = time.time()
        print("结束程序运行...")
        print(f"一共耗费了{(stop - start):.5f}秒。")
    return call_func

# 把@time_master装饰器放在myfunc函数的定义上方，相当于执行了myfunc = time_master(myfunc)
# 把myfunc作为参数塞给time_master
@time_master
def myfunc():
    time.sleep(1)
    print("I love FishC.")

myfunc()

# 另一种传统写法
# myfunc = time_master(myfunc) # 返回call_func函数，并赋值给myfunc
# myfunc() # 调用call_func函数


"""多个装饰器"""
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

# 相当于test = add(cube(square(test)))
# 2*2 再 4*4*4 = 64 再 64+1 = 65
@add
@cube
@square
def test():
    return 2

print(test())


"""给装饰器传递参数"""
def logger(msg):  # 第1层：接收装饰器的参数 msg
    def time_master(func): 
        def call_func(): 
            start = time.time()
            func() # 调用原来的 funA
            stop = time.time()
            print(f"[{msg}]一共耗费了 {(stop-start):.2f}")
        return call_func
    return time_master
 
@logger(msg="A") # 返回 time_master
# time_master 在定义阶段就已经跑完了，它的任务就是把原始 funA 包成 call_func 并返回。之后不会再调用 time_master
def funA():
    time.sleep(1)
    print("正在调用funA...")

@logger(msg="B")
def funB():
    time.sleep(1)
    print("正在调用funB...")

funA() # 调用call_func函数
funB()

# 第1步：logger(msg="A") # time_master_A = logger(msg="A")
#        → 返回 time_master # 此时 msg="A" 被闭包记住了，但还不知道要装饰哪个函数。

# 第2步：time_master(原始funA) # call_func_for_funA = time_master_A(原始funA)
#        → 返回 call_func # 此时 call_func 通过闭包记住了两样东西：1. msg = "A"（从 logger 传下来的）；2. func = 原始funA（从 time_master 传下来的）

# 第3步：funA = call_func  # funA = logger(msg="A")(funA)

# 第4步：用户写 funA() 时 # 调用 call_func


# 另一种传统写法
# def funA():
#     time.sleep(1)
#     print("正在调用funA...")

# def funB():
#     time.sleep(1)
#     print("正在调用funB...")
# funA = logger(msg="A")(funA)
# fubB = logger(msg="B")(funB)
# funA()
# funB()


# 动动手0：在软件行业里，类似这种“项目经理要求这里运行缓慢，好让客户给钱优化”的梗，大家应该有听说过吧……
# 下面这段代码实现斐波那契数列：
# 请大家编写一个装饰器，并将其放到适当的位置，目的是让代码 1 秒钟打印一个结果。

################################
# 请输入需要获取的斐波那契数：5
# 1 1 2 3 5

def fib_decorator(func):
    def call_func(n):
        f = func()
        for i in range(n):
            time.sleep(1)
            f()
            # 如果这么写：func()() # 1 1 1 1 1    # 全是 1，不是斐波那契数列
    return call_func

@fib_decorator
def fib():
    back1, back2 = 0, 1
    def inner_func():
        nonlocal back1, back2
        back1, back2 = back2, back1 + back2
        print(back1, end=' ', flush=True)
        # print(back1)
    return inner_func

n = int(input("请输入需要获取的斐波那契数："))
fib(n)

# 答案：
# import time
    
# def delay(func):
#     def call_func():
#         time.sleep(1)
#         func()
#     return call_func
    
# def fib():
#     back1, back2 = 0, 1
#     @delay # 返回了call_func函数
#     def func():
#         nonlocal back1, back2
#         back1, back2 = back2, back1 + back2
#         print(back1, end=' ')
#     return func
    
# def get_fib(n):
#     f = fib() # 这里调用了fib，也包装了call_func函数，但还没调用
#     for i in range(n):
#         f() # ← 每次 f() 才真正执行 sleep(1) + 打印
    
# n = int(input("请输入需要获取的斐波那契数："))
# get_fib(n)

# 动动手1：请修改附件代码，添加一个装饰器，检测对象类型是否正确的装饰器。

##############################
# <<<--- 测试整数 --->>>
# 4
# 参数类型错误！

# <<<--- 测试字符串 --->>>
# I LOVE FISHC.
# 参数类型错误！

# 请在此处补充装饰器 type_check() 的代码
print("<<<--- 测试整数 --->>>")

def type_check(arg_type):
    def decorator(func):
        def call_func(x):
            if type(x) == arg_type:
                return func(x)
            else:
                return "参数类型错误！"
        return call_func
    return decorator

@type_check(int)
def double(x):
    return x * 2

print(double(2))      # 这里打印结果应该是 4
print(double("2"))    # 这里打印结果应该是 “参数类型错误”


print("\n<<<--- 测试字符串 --->>>")

@type_check(str)
def upper(s):
    return s.upper()

print(upper('I love FishC.'))   # 这里打印结果应该是 I LOVE FISHC
print(upper(250))               # 这里打印结果应该是 “参数类型错误”




































