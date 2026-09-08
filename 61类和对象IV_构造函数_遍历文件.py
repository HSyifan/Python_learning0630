"""构造函数"""
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y

c = C(2, 3)
print(c.add()) # 5
print(c.mul()) # 6

print(c.__dict__) # {'x': 2, 'y': 3}

d = C(4, 5)
print(d.__dict__) # {'x': 4, 'y': 5}
print(d.add()) # 9
print(d.mul()) # 20


"""重写"""
class D(C):
    def __init__(self, x, y, z):
        C.__init__(self, x, y) # 相当于self.x = x, self.y = y
        self.z = z
    def add(self):
        return C.add(self) + self.z
    def mul(self):
        return C.mul(self) * self.z
    
d = D(2, 3, 4)
print(d.add()) # 9
print(d.mul()) # 24


"""钻石继承"""
class A:
    def __init__(self):
        print("哈喽，我是A~")
    
class B1(A):
    def __init__(self):
        A.__init__(self)
        print("哈喽，我是B1~")

class B2(A):
    def __init__(self):
        A.__init__(self)
        print("哈喽，我是B2~")

class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("哈喽，我是C~")
    
c = C()

"""使用super()来调用父类的方法"""
class B1(A):
    def __init__(self):
        super().__init__()
        print("哈喽，我是新的B1~")

class B2(A):
    def __init__(self):
        super().__init__()
        print("哈喽，我是新的B2~")

class C(B1, B2):
    def __init__(self):
        super().__init__()
        print("哈喽，我是新的C~")

c = C()

# 查看C的继承关系，类的方法解析顺序
print(C.mro()) # [<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>]
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>)


# 练习题：
class A:
    x = 250
       
class B(A):
    pass
class C(B):
    pass
class D:
    x = 520
       
class E(C, D):
    pass
print(E.x) # 250
# 请问这里会打印什么内容？


class A:
    x = 250
    def add_x(self):
        self.x += 1
class B(A):
    x = 300
    def add_x(self):
        A.add_x(self)
class C(A):
    x = 500
    def add_x(self):
        A.add_x(self)
class D(B, C):
    pass
d = D()
print(d.x) # 301
# 请问这里会打印什么内容？


class A:
    def ping(self):
        print("A ping~")
class B(A):
    def pong(self):
        print("B pong~")
class C(A):
    def pong(self):
        print("C pong~")
class D(B, C):
    def pingpong(self):
        self.ping()
        self.pong()
d = D()
print(d.pingpong()) # A ping~ B pong~ None
# 请问这里会打印什么内容？


# 动动手0：请利用 __bases__ 属性，获取一个类的 MRO 顺序。
# 这里我们获取 tkinter 模块中，Text 类的 MRO 顺序（这个 get_bases() 就是本题要求编写的函数，可以看到这里我们除了获取 MRO 顺序，还根据父类的层数，添加了相应数量的横杆）。
# 要求：1. 不能使用 mro() 方法或 __mro__ 属性
#      2. 每深入一级父类，需要在前方添加一个横杆（-）
import tkinter

def get_bases(cls, level=0):
    print("- " * level + str(cls))
    for base in cls.__bases__:
        if base is object:
            continue
        get_bases(base, level+1)

get_bases(tkinter.Text)

#######################################
# <class 'tkinter.Text'>
# - <class 'tkinter.Widget'>
# - - <class 'tkinter.BaseWidget'>
# - - - <class 'tkinter.Misc'>
# - - <class 'tkinter.Pack'>
# - - <class 'tkinter.Place'>
# - - <class 'tkinter.Grid'>
# - <class 'tkinter.XView'>
# - <class 'tkinter.YView'>


# 动动手1：解压后是一个包含多层文件夹嵌套的结构（小甲鱼：如果你能够将其执行起来，会看到女神洛天依~）。
# 先打印路径结构
# 然后通过类和对象的方式来存储每一个文件信息（包含文件名、文件尺寸、位置、创建时间、修改时间和访问时间），并定义相应的方法来获取这些文件信息
# 最后编写一个搜索函数，通过提供文件名的方式搜索对应的文件位置和信息

import time
from pathlib import Path

p = Path(r"D:\Python_learning_260630\课后作业\targetVI_I")

# 1. 打印路径结构
print("路径结构如下：")
print(p.name)
for each in p.glob("**/*"):
    print(p.name / each.relative_to(p))

# 2. 用类存储每个文件的信息，并用方法获取/展示
class FileInfo:
    def __init__(self, path):
        s = path.stat()
        self.name = path.name
        self.size = s.st_size
        self.path = path.parent          # 位置：所在目录
        self.create_time = s.st_ctime
        self.modify_time = s.st_mtime
        self.access_time = s.st_atime

    def _fmt(self, ts):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))

    def show(self, n):
        print()
        print(f"找到相关文件 ({n}) -> {self.name} ({self.size} 字节)")
        print(f"位置: {self.path}")
        print(f"创建时间: {self._fmt(self.create_time)}")
        print(f"修改时间: {self._fmt(self.modify_time)}")
        print(f"访问时间: {self._fmt(self.access_time)}")
        
        
# 3. 遍历目录，为每个文件创建对象
files = []
for each in p.glob("**/*"):
    if each.is_file():
        files.append(FileInfo(each))
# print(files) #一个个实例化后的对象 # <__main__.FileInfo object at 0x00000222EBDA15E0>

# 4. 搜索函数（写在类外面）
def search(files, keyword):
    count = 0
    for f in files:
        if keyword in f.name:
            count += 1
            f.show(count)
    if count == 0:
        print("找不到相关文件！")


target = input("请输入想要搜索的文件名:")
search(files, target)


#####################################################
# 请输入想要搜索的文件名:fishc

# 找到相关文件 (1) -> fishc.css (85965 字节)
# 位置: D:\Python_learning_260630\课后作业\targetVI_I\assets\css
# 创建时间: 2022-12-31 19:03:43
# 修改时间: 2022-07-15 17:12:09
# 访问时间: 2026-09-06 08:42:31

# 找到相关文件 (2) -> fishc.js (24200 字节)
# 位置: D:\Python_learning_260630\课后作业\targetVI_I\assets\js
# 创建时间: 2022-12-31 19:03:44
# 修改时间: 2019-07-29 11:08:00
# 访问时间: 2026-09-06 08:42:31

# 请输入想要搜索的文件名:FishC
# 找不到相关文件！











