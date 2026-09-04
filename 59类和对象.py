"""继承"""
class A:
    x = 520
    def hello(self):
        print("你好，我是A~")

class B(A):
    pass

# 子类可以继承父类的属性和方法
b = B()
print(b.x) # 520
b.hello() # 你好，我是A~

# 子类可以覆盖父类的方法
class B(A):
    x = 880
    def hello(self):
        print("你好，我是B~")

b = B()
print(b.x) # 880
b.hello() # 你好，我是B~

# isinstance() 函数用于检查一个对象是否是一个类的实例
print(isinstance(b, B)) # True
print(isinstance(b, A)) # True

# issubclass() 函数用于检查一个类是否是另一个类的子类
print(issubclass(B, A)) # True

class B:
    x = 880
    y = 250
    def hello(self):
        print("你好，我是B~")

class C(A, B):
    pass

c = C()
print(c.x) # 520, 来自A类
print(c.y) # 250, 来自B类，A类中没有y属性
c.hello() # 你好，我是A~，来自A类

"""组合"""
class Turtle:
    def say(self):
        print("不积跬步，无以至千里！")

class Cat:
    def say(self):
        print("喵喵喵~")

class Dog:
    def say(self):
        print("哟吼，我是一只小狗~")

class Garden:
    t = Turtle()
    c = Cat()
    d = Dog()
    def say(self):
        self.t.say()
        self.c.say()
        self.d.say()

g = Garden()
g.say() 
# 不积跬步，无以至千里！
# 喵喵喵~
# 哟吼，我是一只小狗~


# 练习题：
print(issubclass(bool, int)) # True

class lxt1:
    l = 1

class lxt1_1(lxt1):
    l = 2

c = lxt1_1()
print(c.l) # 2

# 6. 请看下面代码，如果调用 test() 函数，那么打印的值分别是什么呢？
x = 1
def test():
    x = 2
    print(x)

    class C:
        x = 3
        print(x)

        def m1(self):
            print(x)
            print(self.x)

        def m2(self):
            x = 4
            print(x)
            self.x = 5

        def m3(self):
            print(x)
            print(self.x)

    c = C()
    c.m1()
    c.m2()
    c.m3()

test()

# 2
# 3
# 2
# 3
# 4
# 2
# 5  # m2 给这个对象写了 self.x = 5，后面再读 self.x 就是 5


# 动动手0：请根据下图所示继承关系创建 A~H 共计 8 个类，其中，父类 A 和 B 均拥有 x 属性（A.x = 250，B.x = 520），
# 其余子类均为 pass 填充，然后判断 类 H 的实例化对象 h 的 x 属性值应该是多少？

class A():
    x = 250

class B():
    x = 520

class C(B):
    pass

class D(A, B):
    pass

class E():
    pass

class F(D):
    pass

class G(D):
    pass

class H(E, F, G):
    pass

h = H()
print(h.x) # 250


# 动动手1：这次要求大家依葫芦画瓢，定义一个动物园类（Zoo），里面有鸟类如 1 只孔雀（Peacock）、
# 2 只天鹅（Swan）、3 只八哥（Myna），猫科动物类如 4 头狮子（Lion）、5 头老虎（Tiger）、
# 6 头豹子（Leopard），灵长类（Primate）如 7 只猴子（Monkey）、8 只猩猩（Chimpanzee）、
# 9 只狒狒（Baboon），题目要求就这 ３ 类动物（当然你想继续发挥也可以），
# 只需要定义类的构成框架就行，内部用 pass 语句填充即可。

class Birds:
     pass

class Peacock(Birds):
     pass

class Swan(Birds):
     pass

class Myna(Birds):
     pass

class Cats:
     pass

class Lion(Cats):
     pass

class Tiger(Cats):
     pass

class Leopard(Cats):
     pass

class Primates:
     pass

class Monkey(Primates):
     pass

class Chimpanzee(Primates):
     pass

class Baboon(Primates):
     pass

class Zoo:
    peacocks = Peacock()
    swans = [Swan(), Swan()]
    mynas = [Myna(), Myna(), Myna()]
    lions = [Lion() for i in range(4)]
    tigers = [Tiger() for i in range(5)]
    leopards = [Leopard() for i in range(6)]
    monkeys = [Monkey() for i in range(7)]
    chimpanzees = [Chimpanzee() for i in range(8)]
    baboons = [Baboon() for i in range(9)]





















