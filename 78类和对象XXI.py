"""type"""
# --- Note：type 四种用法 ---
# 1. 查类型：type(250) → <class 'int'>
# 2. 当构造器：type(250)("520") ≡ int("520")
# 3. 动态造类：type("D", (C,), {"x": 250}) ≡ class D(C): x = 250
# 4. 造类 + 钩子：type("D", (C,), {}, value=520) → 额外 kwargs 给 __init_subclass__

print(type(250)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("Hello, World!")) # <class 'str'>

print(int) # <class 'type'>
print(float) # <class 'type'>
print(str) # <class 'type'>

print(type(250)("520")) # 520, 等效 int("520") 

print(type([])("FishC")) # ['F', 'i', 's', 'h', 'C']

print(type(())([1, 2, 3, 4, 5])) # (1, 2, 3, 4, 5)

print(type({}).fromkeys("Python")) # {'P': None, 'y': None, 't': None, 'h': None, 'o': None,'n': None}

class C:
    def __init__(self, x):
        self.x = x

c = C(250)
print(c) # <__main__.C object at 0x0000023258A12150>
d = type(c)(520)
print(d) # <__main__.C object at 0x0000023258A12120>

print(c.__class__) # <class '__main__.C'>
print(d.__class__) # <class '__main__.C'>


print(type(C)) # <class 'type'>


class C:
    pass

# 第一个参数是
C = type("C", (), {})
c = C()
print(c.__class__) # <class '__main__.C'>
print(C.__base__) # <class 'object'>

D = type("D", (C,), {}) # 第二个是元组，得有个逗号
print(D.__base__) # <class '__main__.C'>

E = type("E", (), dict(x = 250, y = 520))
print(E.x) # 250
print(E.y) # 520

# 往type里传方法
def funC(self, name = "FishC"):
    print(f"Hello {name}!")

F = type("F", (), dict(say_hi = funC))
f = F()
f.say_hi() # Hello FishC!
f.say_hi("小甲鱼") # Hello 小甲鱼!


class C:
    def __init_subclass__(cls):
        print("父爱如山")
        cls.x = 520 # 后面执行D.x = 520

class D(C):
    x = 250

# 触发init_subclass方法：，打印父爱如山

print(D.x) # 520

class C:
    def __init_subclass__(cls, value):
        print("父爱如山")
        cls.x = value

class D(C, value = 520):
    x = 250

# 触发init_subclass方法：，打印父爱如山
print(D.x) # 520

# 用type构造类D，父类是C，类字典是dict(x = 520)，钩子参数是value = 520
D = type("D", (C,), dict(x = 520), value = 520) # 父爱如山
print(D.x) # 520


class C:
    def __init_subclass__(cls, value1, value2):
        print("父爱如山")
        cls.x = value1
        cls.y = value2

D = type("D", (C,), dict(x = 250), value1 = 520, value2 = 666)

# 触发init_subclass方法：，打印父爱如山
print(D.x) # 520
print(D.y) # 666

# --- Note（__init_subclass__ + type 额外参数）---
# 1. 子类一创建就会调父类的 __init_subclass__(子类本身, ...)
# 2. class D(C, value=520) 里的 value 不是父类，是传给 __init_subclass__ 的参数
# 3. type("D", (C,), {...}, value=520) 等价于上面这种 class，多出来的 kwargs 同样进 __init_subclass__
# 4. type 三件套：名字 / 父类元组 / 类字典；再往后才是钩子参数





