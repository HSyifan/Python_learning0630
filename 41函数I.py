"""函数的创建和调用"""
def myfunc(): 
    pass # 函数主题

myfunc()

def myfunc():
    for i in range(3):
        print("I love FishC")

myfunc()

"""函数的参数"""
def myfunc(name):
    for i in range(3):
        print(f"I love {name}.")

myfunc("Python")

def myfunc(name, times):
    for i in range(times):
        print(f"I love {name}.")

myfunc("Python", 5)

def div(x, y):
    if y == 0:
        return "除数不能为0" # return之后，函数结束运行
    else:
        return x / y

print(div(4, 2))
print(div(4, 0)) # 除数不能为0

def myfunc():
    pass

print(myfunc()) # None


# 练习题：
def funA():
    funB()
def funB():
    print("Hi~")

funA()

# 动动手0：请编写一个实现【注册】和【登陆】功能的代码，这次要求将不同的功能封装成独立的函数。
# 编写 4 个函数分别用于获取用户指令（get_int()）、注册（register()）、登陆（login()）、MD5加密（encrypt()）
# 使用一个 Python 的字典作为数据库。
# 注册时需验证用户名是否已存在于数据库
# 登陆时需验证用户名和密码是否匹配
# 密码保存需使用 MD5 加密
# 请先分别画出程序主结构、注册函数和登陆函数的流程图，再编写实现代码。

import hashlib

def get_int():
    while True:
        print("=" * 20)
        print("1. 注册")
        print("2. 登陆")
        print("3. 退出")
        input_int = int(input("请输入指令："))
        if input_int in [1, 2, 3]:
            return input_int
        else:
            print("输入不合法，请重新输入")

def register():
    print("=" * 20)
    name = input("请输入用户名：")
    while name in database: 
        print("该用户名已被注册！")
        name = input("请重新输入用户名：")
    password = input("请输入密码：")
    database[name] = encrypt(password)
    print("恭喜，注册成功~")

def login():
    print("=" * 20)
    name = input("请输入用户名：")
    while name not in database:
        print("该用户名不存在。")
        name = input("请重新输入用户名：")
    password = input("请输入密码：")
    while database[name] != encrypt(password):
        print("密码错误！")
        password = input("请重新输入密码：")
    print("恭喜，登陆成功~")

def encrypt(password):
    bstr = bytes(str(password), "utf-8") # 将整数转换为字符串，并转换为bytes类型
    hash_passwd = hashlib.md5(bstr).hexdigest() # 计算哈希值
    return hash_passwd


database = {}

print("欢迎来到鱼C论坛~")
while True:
    cmd = get_int()
    if cmd == 1:
        register()
    elif cmd == 2:
        login()
    else:          # 3. 退出
        print("=" * 20)
        break

################################
# 欢迎来到鱼C论坛~
# ====================
# 1. 注册
# 2. 登陆
# 3. 退出
# 请输入指令：1
# ====================
# 请输入用户名：小甲鱼
# 请输入密码：FishC520
# 恭喜，注册成功~
# ====================
# 1. 注册
# 2. 登陆
# 3. 退出
# 请输入指令：2
# ====================
# 请输入用户名：甲鱼
# 该用户名不存在。
# 请重新输入用户名：小甲鱼
# 请输入密码：123456
# 密码错误！
# 请重新输入密码：FishC520
# 恭喜，登陆成功~
# ====================
# 1. 注册
# 2. 登陆
# 3. 退出
# 请输入指令：3
# ====================
















































