"""位置参数"""
# 位置参数是指函数调用时，参数按照顺序传递，参数的顺序必须与函数定义时的参数顺序一致。
def myfunc(s, vt, o):
    return "".join((o, vt, s))

print(myfunc("我", "打了", "小甲鱼")) # 小甲鱼打了我
print(myfunc("小甲鱼", "打了", "我"))

"""关键字参数"""
# 关键字参数是指函数调用时，参数按照名称传递，参数的名称必须与函数定义时的参数名称一致。
print(myfunc(o="我", vt="打了", s="小甲鱼")) # 我打了小甲鱼
# print(myfunc(o="我", "清蒸", "小甲鱼")) # 报错

# 全位置
myfunc("小甲鱼", "清蒸", "我")
# 全关键字（顺序随便）
myfunc(o="我", vt="清蒸", s="小甲鱼")
# 先位置，再关键字
myfunc("小甲鱼", "清蒸", o="我")
# 或
myfunc("小甲鱼", vt="清蒸", o="我")

"""默认参数"""
def myfunc(s, vt, o="小甲鱼"):
    return "".join((o, vt, s))

print(myfunc("香蕉", "吃")) # 小甲鱼吃香蕉

# 报错，默认参数必须放在最后
# def myfunc(s="苹果", vt, o="小甲鱼"): 
    # return "".join((o, vt, s)) 

print(help(abs))
# 斜杠左侧不能传递关键字参数，只能传递位置参数
# abs(x, /)
#     Return the absolute value of the argument.

print(abs(-1.5))
# print(abs(x = -1.5)) # 报错

def abc(a, /, b, c):
    print(a, b, c)

abc(1, 2, 3)
# print(abc(a=1, b=2, c=3)) # 报错
abc(1, b=2, c=3) # 报错

# 星号左侧都可以，星号右侧不能传递位置参数，只能传递关键字参数
def abc(a, *, b, c):
    print(a, b, c)

# abc(1, 2, 3) # 报错
abc(1, b=2, c=3)
abc(a=1, b=2, c=3)


# 动动手0：检测输入的中文字符串是否符合回文的语法
# 这个前面大家已经做过练习了，不过这一次我们将要放宽，只要该字的拼音一样，字不相同没有关系，比如 “前任只认钱” 可以符合要求
# 提示一：放宽要求后，只要文字的发音构成前后回文，即认定为符合要求。
# 提示二：将汉字转换为对应拼音的方法 -> https://fishc.com.cn/thread-213439-1-1.html
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xpinyin
# 提示三：请将各个独立的功能封装为函数。

################################
# 请输入一段话：嗯
# 字数太少，请重新输入：小甲鱼
# [小甲鱼]不是回文。
# 请输入一段话：我爱你你爱我
# [我爱你你爱我]是回文。
# 请输入一段话：前任只认钱
# [前任只认钱]是回文。
# 请输入一段话：强国中属中国强
# [强国中属中国强]是回文。

from xpinyin import Pinyin
p = Pinyin()

def is_huiwen(dds0_input):
    fa_yin = p.get_pinyin(dds0_input, tone_marks="numbers")
    fa_yin = fa_yin.split("-")
    if fa_yin == fa_yin[::-1]:
        return print(f"[{dds0_input}]是回文。")
    else:
        return print(f"[{dds0_input}]不是回文。")



dds0_input = input("请输入一段话：")
while len(dds0_input) < 2:
    dds0_input = input("字数太少，请重新输入：")

print(is_huiwen(dds0_input))


# 动动手1：利用函数模拟创建【栈】的数据结构操作。

# 栈是一种具有 FILO 特性的数据结构，即先放入的数据反而后取出。
# 比如有依次放入数据 250、251、255 到栈中，那么它们在栈中的存储结构如下：255，251，250
# 此时，执行取出命令（pop），应该将最后压入栈的 255 优先取出，取出后栈中内容如下：251，250
# 同样道理，如果我们执行压栈命令（push），将数据 520 压入栈中，那么执行后，栈中内容如下：520，251，250
# 题目要求：将压栈命令（push）、取出命令（pop）和打印栈的功能分别封装为独立的函数。

stack = []
def push(value):
    stack.insert(0, value)
    print("栈：")
    for each in stack:
        print(each)

def pop():
    if len(stack) > 0:
        print(stack[0])
        stack.pop(0)
        print("栈：")
        for each in stack:
            print(each)
    else:
        print("栈已空~")

def top():
    if len(stack) > 0:
        print(stack[0])
    else:
        print("栈已空~")


while True:
    op = input("请输入指令（push/pop/top/exit）：")
    if op == "push":
        value = input("请输入将要压入栈中的值：")
        push(value)
    elif op == "pop":
        pop()
    elif op == "top":
        top()
    elif op == "exit":
        break


# 请输入指令（push/pop/top/exit）：push
# 请输入将要压入栈中的值：250
# 栈：
# 250
# 请输入指令（push/pop/top/exit）：push
# 请输入将要压入栈中的值：251
# 栈：
# 251
# 250
# 请输入指令（push/pop/top/exit）：push
# 请输入将要压入栈中的值：255
# 栈：
# 255
# 251
# 250
# 请输入指令（push/pop/top/exit）：top
# 255
# 请输入指令（push/pop/top/exit）：pop
# 255
# 栈：
# 251
# 250
# 请输入指令（push/pop/top/exit）：pop
# 251
# 栈：
# 250
# 请输入指令（push/pop/top/exit）：pop
# 250
# 栈：
# 请输入指令（push/pop/top/exit）：pop
# 栈已空~
# 请输入指令（push/pop/top/exit）：top
# 栈已空~
# 请输入指令（push/pop/top/exit）：exit


