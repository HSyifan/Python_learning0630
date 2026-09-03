"""对象 = 属性 + 方法"""
class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True

    def crawl(self):
        print("人们总抱怨我动作慢吞吞的，殊不知如不积跬步，无以至千里的道理。")

    def run(self):
        print("虽然我行动很慢，但如果遇到危险，还是会夺命狂奔的T_T")

    def bite(self):
        print("人善被人欺，龟善被人骑，我可是会咬人的！")

    def eat(self):
        print("谁知盘中餐粒粒皆辛苦，吃得好，不如吃得饱~")

    def sleep(self):
        print("Zzzz...")

# t1为实例对象，有了turtle的属性和方法
t1 = Turtle()
print(t1.head) # 1
print(t1.legs) # 4

t1.crawl() # 人们总抱怨我动作慢吞吞的，殊不知如不积跬步，无以至千里的道理。
t1.bite() # 人善被人欺，龟善被人骑，我可是会咬人的！
t1.sleep() # Zzzz...

t2 = Turtle()
t2.legs = 3
print(t2.legs) # 3

print(t1.legs) # 4

t1.mouth = 1
print(t1.mouth) # 1

print(dir(t1)) # 打印t1的所有属性和方法
# 比t2多了一个mouth属性
# __', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__','__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bite', 'crawl', 'eat', 'eyes', 'head', 'legs', 'mouth', 'run', 'shell', 'sleep']

x = 520
print(type(x)) # <class 'int'>

y = "FishC"
print(type(y)) # <class 'str'>

class C:
    def hello():
        print("你好~")

c = C()
# c.hello() # 你好~ 
# TypeError: C.hello() takes 0 positional arguments but 1 was given

class C:
    def get_self(self):
        print(self)

c = C()
c.get_self() # <__main__.C object at 0x000001AA23A3B260>
print(c) # <__main__.C object at 0x000001AA23A3B260>


# 练习题：
class L:
    pass

l = L()
print(l) # <__main__.L object at 0x000001AA23A3B260>

class C:
    x = 250

c1 = C()
c2 = C()
print(c1 is c2) # False,因为c1和c2是不同的对象
print(c1 == c2) # False,因为c1和c2是不同的对象
print(c1.x is c2.x) # True,因为c1和c2的x属性是相同的
print(c1.x == c2.x) # True,因为c1和c2的x值是相同的


# 动动手0：请设计一个 Person 类，该类有 name 和 age 两个属性（分别用于指定对象的姓名和年龄），
# 该类还有 set_name()、set_age()、get_name() 和 get_age() 四个方法（分别用于设置、获取对象的姓名和年龄）。

class Person:
    name = None
    age = None
    
    def set_name(self):
        self.name = input("请输入名字：")
    
    def set_age(self):
        self.age = input("请输入年龄：")
    
    def get_name(self):
        if self.name:
            return self.name
        else:
            print("名字未设置！")
    
    def get_age(self):
        if self.age:
            return self.age
        else:
            print("年龄未设置！")


# 动动手1：请设计一个 Rectangle 类，该类有 length 和 width 两个属性（分别用于指定长方形的长度和宽度），
# 该类还有 set_length()、set_width()、get_ perimeter() 和 get_area() 四个方法（分别用于设置长方形的长和宽，以及获取长方形的周长和面积）。

# 给大家提升一点难度吧：对于 get_ perimeter() 和 get_area() 这两个方法，
# 在被调用的时候，应该要检测 length 和 width 两个属性是否已被设置，
# 如果未设置，应该在方法内部调用相应的 set_length() 或 set_width() 方法
# （提示：在方法内部调用对象的方法，同样需要使用 对象.方法名() 的语法，对象就是 self，大家大胆尝试一下吧~）。

# class Rectangle:
#     length = 0
#     width = 0
#     def set_length(self, length):
#         self.length = length
#     def set_width(self, width):
#         self.width = width
#     def get_perimeter(self):
#         if self.length == 0 or self.width == 0:
#             self.set_length(self.length)
#             self.set_width(self.width)
#         return 2 * (self.length + self.width)
#     def get_area(self):
#         if self.length == 0 or self.width == 0:
#             self.set_length(self.length)
#             self.set_width(self.width)
#         return self.length * self.width


# 答案：
class Rectangle:
    length = None
    width = None
    
    def set_length(self):
        self.length = float(input("请输入矩形的长度："))

    def set_width(self):
        self.width = float(input("请输入矩形的宽度："))
    
    def get_perimeter(self):
        if not self.length:
            self.set_length()
    
        if not self.width:
            self.set_width()
    
        return (self.length + self.width) * 2
    
    def get_area(self):
        if not self.length:
            self.set_length()
    
        if not self.width:
            self.set_width()
    
        return self.length * self.width

r = Rectangle()
print(r.get_perimeter())
print(r.get_area())























