"""描述符"""

class D:
    def __get__(self, instance, owner):
        print(f"get~\nself -> {self}\ninstance -> {instance}\nowner -> {owner}")
    def __set__(self, instance, value):
        print(f"set~\nself -> {self}\ninstance -> {instance}\nvalue -> {value}")
    def __delete__(self, instance):
        print(f"delete~\nself -> {self}\ninstance -> {instance}")

class C:
    x = D()

c = C()
c.x = 250
# set~
# self -> <__main__.D object at 0x000002BEF74D2000>
# instance -> <__main__.C object at 0x000002BEF74D2060>
# value -> 250

c.x
# get~
# self -> <__main__.D object at 0x000001AEFCBF2030>
# instance -> <__main__.C object at 0x000001AEFCBF2090>
# owner -> <class '__main__.C'>

del c.x
# delete~
# self -> <__main__.D object at 0x000001AEFCBF2030>
# instance -> <__main__.C object at 0x000001AEFCBF2090>



class D:
    def __get__(self, instance, owner):
        return instance._x
    def __set__(self, instance, value):
        instance._x = value
    def __delete__(self, instance):
        del instance._x

class C:
    def __init__(self, x = 250):
        self._x = x
    x = D()

c = C()
print(c.x) # 250
c.x = 520
print(c.__dict__) # {'_x': 520}
del c.x
print(c.__dict__) # {}


# MyProperty 凭什么能当 property 用？
# 1. 实现了 __get__/__set__/__delete__
# 2. 作为类属性 x = MyProperty(...)
# 3. 存了读/写/删三个函数并在对应方法里调用
class MyProperty():
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = 250
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = MyProperty(getx, setx, delx)

c = C()
print(c.x) # 250
c.x = 520
print(c.__dict__) # {'_x': 520}
del c.x
print(c.__dict__) # {}


# 这里写了getter，setter，deleter方法，所以下面的x可以x.setter,x.deleter
class MyProperty():
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)
    def getter(self, func):
        self.fget = func
        return self
    def setter(self, func):
        self.fset = func
        return self
    def deleter(self, func):
        self.fdel = func
        return self

class D:
    def __init__(self):
        self._x = 250
    @MyProperty
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x


d = D()
print(d.x) # 250
d.x = 520
print(d.__dict__) # {'_x': 520}
del d.x
print(d.__dict__) # {}


class E:
    def __init__(self):
        self._x = 250
    x = MyProperty()
    @x.getter
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

e = E()
print(e.x) # 250
e.x = 520
print(e.__dict__) # {'_x': 520}
del e.x
print(e.__dict__) # {}


# 浅显例子：好几个属性都要「必须 > 0」
# 用 property 要写很多遍：
class Product:
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("必须为正数")
        self._price = value

    # quantity、weight……每个都再抄一套

# 用描述符，规则写一次，挂多次：
class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("必须为正数")
        setattr(instance, self.name, value)

class Product:
    price = Positive()
    quantity = Positive()
    weight = Positive()

p = Product()
p.price = 10       # 走 Positive.__set__，存到 p._price
p.quantity = 5
print(p.price)     # 走 Positive.__get__，读 p._price
# p.price = -1     # ValueError: 必须为正数


# pydantic 库的 Field 就是描述符
# from pydantic import BaseModel, Field

# class Product(BaseModel):
#     price: float = Field(gt=0)      # 必须 > 0
#     quantity: int = Field(gt=0)
#     name: str

# p = Product(price=10, quantity=5, name="苹果")   # 成功
# # Product(price=-1, quantity=5, name="苹果")    # 报错


# 练习题：
class C:
    def __get__(self, instance, owner):
        return "FishC"

class D:
    x = C()

d = D()
d.x = 520
print()
print(d.x)
# 请问这里会输出什么？
# 520
# 赋值前：d.x → 走类上的描述符 __get__ → "FishC"；d.__dict__ 是 {}
# d.x = 520 → 没有 __set__，不能拦截赋值
#          → 直接往实例里写：d.__dict__['x'] = 520
# 赋值后：d.x → 先在实例字典里找到 x=520 → 打印 520（类上的描述符被挡住了）



# 动动手0：实现只读属性的描述符
# 创建一个只读属性的描述符类 ReadOnly, 使得被它管理的属性在实例创建后无法被修改或删除。
# 如果尝试修改或删除属性，应该抛出 AttributeError。
# 要求：该属性只能在类实例化的时候被设置，此后不允许被修改或删除。

class ReadOnly:
    def __init__(self, name):
        self.name = name  # 属性名，如 "name"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # 实例字典里还没有 → 允许第一次赋值（通常在 __init__）
        if self.name in instance.__dict__:
            raise AttributeError(f"只读属性 {self.name} 不能修改")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"只读属性 {self.name} 不能删除")


class Person:
    name = ReadOnly("name")
    def __init__(self, name):
        self.name = name

p = Person("小甲鱼")
print(Person.name) # <__main__.ReadOnly object at 0x00000279E1850800> 
print(p.name)     # 输出：小甲鱼
# p.name = "不二如是"  # AttributeError
# del p.name          # AttributeError


# 动动手1：实现类型检查的描述符
# 创建一个描述符类 Typed, 用于对属性进行类型检查。
# 在设置属性值时，如果类型不匹配，抛出 TypeError。

class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}, got {type(value)}")
        instance.__dict__[self.name] = value

class Product:
    name = Typed("name", str)
    price = Typed("price", float)

    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Apple", 10.0)
p.price = 12.5        # 正常修改
# p.price = '12.5'      # 应该抛出 TypeError


# 动动手2：编写一个描述符类 ValidString, 用于管理属性的自动验证和格式化。
# 属性值必须是字符串类型。
# 设置属性值时，自动去除首尾空白字符。
# 属性值长度不能超过指定的最大长度，否则抛出 ValueError。

class ValidString:
    def __init__(self, name, max_length):
        self.name = name
        self.max_length = max_length
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        value = value.strip()
        if len(value) > self.max_length:
            raise ValueError(f"String too long, max length is {self.max_length}")
        instance.__dict__[self.name] = value

class User:
    username = ValidString("username", max_length=20)
    email = ValidString("email", max_length=50)

    def __init__(self, username, email):
        self.username = username
        self.email = email

u = User("   FishC   ", " fishc@ilovefishc.com ")
print(u.username)     # 输出："FishC"
print(u.email)        # 输出："fishc@ilovefishc.com"
# u.username = "FishC" * 5  # 应该抛出 ValueError

























