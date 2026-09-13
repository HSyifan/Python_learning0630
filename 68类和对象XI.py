"""属性访问"""

# ========== 1. 内置函数：查 / 读 / 改 / 删属性 ==========
# hasattr 判断有没有；getattr 读取；setattr 设置；delattr 删除
# 双下划线属性实际名字是 _类名__属性，所以要用 _C__age

class C:
    def __init__(self, name ,age):
        self.name = name
        self.__age = age
    
c = C("小甲鱼", 18)
print(hasattr(c, "name")) # True, 判断对象c是否有name属性
print(getattr(c, "name")) # 小甲鱼,获取对象c的name属性
print(getattr(c, "_C__age")) # 18,获取对象c的__age属性

setattr(c, "_C__age", 19)
print(getattr(c, "_C__age")) # 19,设置对象c的__age属性

delattr(c, "_C__age")
print(hasattr(c, "_C__age")) # False,判断对象c是否有_C__age属性


# ========== 2. __getattribute__：读任何属性都会先经过这里 ==========
# 包括已有属性和不存在的属性；最后要用 super() 去真正取值，否则也会死循环

class C:
    def __init__(self, name ,age):
        self.name = name
        self.__age = age
    def __getattribute__(self, attrname):
        print("拿来吧你~")
        return super().__getattribute__(attrname)

c = C("小甲鱼", 18)
print(getattr(c, "name")) # 拿来吧你~ 小甲鱼

print(c._C__age) # 拿来吧你~ 18

# print(c.FishC) # 先打印拿来吧你~， 再抛出异常


# ========== 3. __getattr__：只有属性不存在时才会走到这里 ==========
# 查找顺序：先 __getattribute__ → 找到就返回；找不到再 __getattr__
# FishC 没有这个属性，所以会打印 I love FishC

class C:
    def __init__(self, name ,age):
        self.name = name
        self.__age = age
    def __getattribute__(self, attrname):
        print("拿来吧你~")
        return super().__getattribute__(attrname)
    def __getattr__(self, attrname):
        if attrname == "FishC":
            print("I love FishC")
        else:
            raise AttributeError(attrname)

c = C("小甲鱼", 18)
c.FishC


# ========== 4. __setattr__ 错误写法：赋值会再次触发自己，死循环 ==========
# d.name = xxx 就是调用 __setattr__；里面再写 self.name = value 会无限递归

# class D:
#     def __setattr__(self, name, value):
#         self.name = value

# d = D()
# d.name = "小甲鱼"


# ========== 5. __setattr__ 正确写法：改 __dict__，绕开自己 ==========
# 不要在 __setattr__ 里用 self.xxx = ...，改 self.__dict__[name] 或 super()

class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    
d = D()
d.name = "小甲鱼"
print(d.name)


# ========== 6. __delattr__：删除属性时触发 ==========
# del d.name 会走这里；同样通过 __dict__ 删除，避免再触发魔法方法

class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def __delattr__(self, name):
        del self.__dict__[name]

d = D()
d.name = "小甲鱼"
print(d.__dict__) # {'name': '小甲鱼'}
del d.name
print(d.__dict__) # {}



# 动动手0：这一次让我们利用所学的知识来做一个文件管理的类吧~
# 要求：定义了一个名为 FileManager 的类，该类可以实现简单的文件管理功能，包括浏览目录、创建文件、重命名文件和删除文件。
# 提示：调用 pathlib 模块中的一些方法，来实现你目前不知道如何实现的文件管理操作。

from pathlib import Path


class FileManager:
    def __init__(self, path="."):
        self.path = Path(path)

    def browse(self):
        for each in self.path.iterdir():
            print(each.name)

    def create(self, name):
        (self.path / name).touch()

    def rename(self, old, new):
        (self.path / old).rename(self.path / new)

    def delete(self, name):
        (self.path / name).unlink()


# 用法和图上一样（会改当前文件夹里的真实文件，需要时再取消注释）：
# fm = FileManager()
# fm.browse()
# fm.create("test.txt")
# fm.rename("test.txt", "new_test.txt")
# fm.delete("new_test.txt")






























