"""异常"""
# print(“I love FishC.”) # SyntaxError: invalid character '“' (U+201C)
# 1 / 0 # ZeroDivisionError: division by zero
# "FishC" + 520 # TypeError: can only concatenate str (not "int") to str

# [速查宝典] Python 内置异常大合集 https://fishc.com.cn/thread-211613-1-2.html

"""异常处理"""

try:
    1 / 0
except:
    print("出错了~")

# 如果没有错误，执行try中代码
try:
    print(1 / 1)
except:
    print("出错了~")

# 如果出现特定错误，执行except中代码，否则执行最后print
try:
    print(1 / 0)
except ZeroDivisionError:
    print("出错了~")

# 获取错误原因
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e, type(e)) # division by zero <class 'ZeroDivisionError'>

# 用元组包裹多个错误
try:
    1 / 0
    520 + "FishC"
except (ZeroDivisionError, ValueError, TypeError):
    pass

# 单独处理不同的异常
try:
    1 / 0
    520 + "FishC"
except ZeroDivisionError:
    print("除数不能为0！") # 除数不能为0！
except ValueError:
    print("值不正确！")
except TypeError:
    print("类型不正确！")


# 动动手0：利用异常捕获机制，使用 while 循环语句来实现 for 循环语句的功能。
x = "FishC"
for each in x:
    print(each)
       
try:
    while True:
        print(x[0])
        x = x[1:]
except IndexError:
    pass
    

# 动动手1：利用 Python 异常机制，编写一个检查用户输入语句是否有错误的程序。
# A. 程序能够识别出 “语法错误”、“索引错误”、“变量未定义”、“除数为0” 和 “传入参数类型不恰当” 这几个错误类型。
# B. 只有通过 Ctrl + C 快捷键才能正常退出程序。
# C. 程序实现请参考以下截图。

def dds0_judge():
    while True:
        try:
            dds0_input = eval(input("请输入一行语句："))
            if type(dds0_input) == int or type(dds0_input) == float:
                print(f"结果是：{dds0_input}")
            elif type(dds0_input) == str:
                print(dds0_input)
        except ZeroDivisionError:
            print("错误：除数为0")
        except NameError:
            print("错误：变量未定义")
        except SyntaxError:
            print("错误：语法错误")
        except ValueError:
            print("错误：传入的参数类型不恰当")  
        except IndexError:
            print("错误：索引错误")  
        except KeyboardInterrupt:
            print("\n程序结束~")
            break

dds0_judge()

# 请输入一行语句：3 / 2
# 结果是：1.5
# 请输入一行语句：3 / 0
# 错误：除数为0
# 请输入一行语句：FishC
# 错误：变量未定义
# 请输入一行语句：print("FishC")
# FishC
# 请输入一行语句：print(“FishC”)
# 错误：语法错误
# 请输入一行语句：int("FishC")
# 错误：传入的参数类型不恰当
# 请输入一行语句："FishC"[5]
# 错误：索引错误
# 请输入一行语句：程序结束~




























