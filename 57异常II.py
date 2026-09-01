"""try-except-else"""
try:
    1 / 0
except:
    print("逮到啦~") 
else:
    print("没逮到~") # 如果没有异常，则执行else语句

"""try-except-finally"""
# 无论是否发生异常，finally语句都会执行
try:
    1 / 0
except:
    print("逮到啦~")
else:
    print("没逮到~") 
finally:
    print("逮没逮到都会吱一声~")

# finally一般用于关闭文件、关闭数据库连接等
# try:
#     f = open("test.txt", "w")
#     f.write("I love FishC.")
# except:
#     print("出错了~")
# finally:
#     f.close()

# 即使ctrl+c退出，finally语句都会执行
# try:
#     while True:
#         pass
# finally:
#     print("晚安~") 


"""异常的嵌套"""
try:
    try:
        520 + "FishC"
    except:
        print("内部异常！")
    1 / 0
except:
    print("外部异常！")
finally:
    print("收尾工作~")

# 外部异常会覆盖内部异常,直接except打印外部异常
try:
    1 / 0
    try:
        520 + "FishC"
    except:
        print("内部异常！")
except:
    print("外部异常！") # 直接except打印外部异常
finally:
    print("收尾工作~")


"""raise语句"""
# 抛出异常,自爆卡车
# raise ValueError("值不正确。")

# 不能自定义异常，只能使用内置异常
# raise FishCError("小甲鱼说你不行你就不行~")

# 替换ZeroDivisionError，抛出ValueError
# try:
#     1 / 0
# except:
#     raise ValueError("这样可不行~")

# 异常链
# raise ValueError("这样可不行~") from ZeroDivisionError

"""assert语句"""
# 通常用于代码调试
s = "FishC"
assert s == "FishC"
# assert s != "FishC" # AssertionError

"""利用异常来实现goto"""
# break和continue只能跳出当前循环，而raise可以跳出多层循环
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    raise # 裸 raise，跳到except
                print(i)
            print("被跳过~")
        print("被跳过~")
    print("被跳过~")
except:
    print("到这儿来了~")


# 练习题：
def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return())

# 输出：False
# 解释：try语句中的return语句会立即返回，但finally语句中的return语句会覆盖try语句中的return语句
# 所以最终返回的是finally语句中的return语句

# 6. 请将下面 assert 修改为异常的实现方式。
def myfunc(x):
    assert x < 0
    return x ** 2
# 使用异常的实现方式

def myfunc(x):
    if x >= 0:
        raise ValueError("x不能大于0")
    return x ** 2


# 7. 利用异常机制，可以实现一步跳出多层循环体，来，大家自己试试吧？
# out = False
# for i in range(1000):
#     for j in range(1000):
#         for k in range(1000):
#             if i * j * k == 12321:
#                 print(f"{i} * {j} * {k} = 12321")
#                 out = True
#             if out:
#                 break
#         if out:
#             break
#     if out:
#         break

try:
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if i * j * k == 12321:
                    raise
except:
    print(f"{i} * {j} * {k} = 12321")


# 10. 请编写代码，实现在捕获异常之后，打印一句 “出错啦”，再重新抛出相对应的异常（注意，这里我们说的异常并不特指具体的哪一类，而是泛指所有的异常）。
try:
    1 / 0
except:
    print("出错啦~")
    raise

# 出错啦~
# Traceback (most recent call last):
#   File "d:\Python_learning_260630\57异常II.py", line 151, in <module>
#     1 / 0
#     ~~^~~
# ZeroDivisionError: division by zero













