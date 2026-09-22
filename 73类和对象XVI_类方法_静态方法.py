"""类方法 / 静态方法"""

# ========== 1. self vs cls ==========
# 普通方法 self=实例；@classmethod 的 cls=类
class C:
    def funA(self):
        print(self)
    @classmethod
    def funB(cls):
        print(cls)

c = C()
c.funA() # <__main__.C object at 0x00000294D7FF1B20>
c.funB() # <class '__main__.C'>


# ========== 2. 必须用 cls.count ==========
# 写死 C.count → 子类调用也只看父类；c3.count=1 只改实例，不影响 cls.count
class C:
    count = 0
    def __init__(self):
        C.count += 1
    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了 {cls.count} 个对象")

c1 = C()
c2 = C()
c3 = C()
C.get_count() # 该类一共实例化了 3 个对象

c3.count = 1
print(c3.count) # 1
c3.get_count() # 该类一共实例化了 3 个对象


# ========== 3. 静态方法 ==========
# 无 self/cls；类名或实例都能调；写死 C 则继承也看 C
class C:
    @staticmethod
    def funC():
        print("I love FishC")

c = C()
c.funC() # I love FishC
C.funC() # I love FishC


class C:
    count = 0
    def __init__(self):
        C.count += 1
    @staticmethod
    def get_count():
        print(f"该类一共实例化了 {C.count} 个对象")

c1 = C()
c2 = C()
c3 = C()
c3.get_count() # 该类一共实例化了 3 个对象


# ========== 4. 子类各自 count=0 ==========
# 不写则第一次 += 先读到父类当前值，数字偏掉；写了才各自从0计
# 不用写 __init__/super：继承父类即可，self.add() 时 cls 仍是子类
# d1.get_count()→2：D()了两次，不是从C的1再加
class C:
    count = 0
    @classmethod
    def add(cls):
        cls.count += 1
    def __init__(self):
        self.add()
    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了 {cls.count} 个对象")


class D(C):
    count = 0

class E(C):
    count = 0

c1 = C()
d1, d2 = D(), D()
e1, e2, e3 = E(), E(), E()
c1.get_count() # 该类一共实例化了 1 个对象
d1.get_count() # 该类一共实例化了 2 个对象
e1.get_count() # 该类一共实例化了 3 个对象


# 练习题：
class C:
    def funA(self):
        return self

    @classmethod
    def funB(cls):
        return cls

c = C()
print(isinstance(c.funA(), c.funB()))
# 请问这里应该返回 True 还是 False，或者是报错呢？
# 返回 True

class C:
    @classmethod
    def funA(cls):
        print(cls.__name__)

class D(C):
    pass

d = D()
d.funA()
# 请问这里会输出什么？
# D


class C:
    count = 0
    def __init__(self):
        C.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c = C()
c.count = 10
print(c.get_count())
# 请问这里会输出什么？


class Logger:
    log_count = 0

    @classmethod
    def log(cls, message):
        cls.log_count += 1 # 如果想要1，2， 3， 4，这里写成Logger.log_count += 1
        print(f"{cls.__name__} Log #{cls.log_count}: {message}")

class FileLogger(Logger):
    pass

Logger.log("系统启动。")
# 请问这里会打印什么内容？
FileLogger.log("打开文件。")
# 请问这里会打印什么内容？
Logger.log("出错！")
# 请问这里会打印什么内容？
FileLogger.log("关闭文件。")
# 请问这里会打印什么内容？


# 动动手0：请你帮小甲鱼开发一个鱼C论坛的会员订单系统，需要根据不同的会员级别和促销活动计算订单的最终价格。
# 创建一个 Discount 类，包含一个类属性 rate，表示折扣率，默认为 0。
# 实现一个类方法 set_rate(cls, rate)，用于设置折扣率。
# 实现一个静态方法 calculate(price)，用于根据当前的折扣率计算最终价格。
# 根据不同的会员级别（如普通会员、黄金会员、白金会员）设置不同的折扣率。

class Discount:
    rate = 0
    @classmethod
    def set_rate(cls, rate):
        cls.rate = rate
    @staticmethod
    def calculate(price):
        return price * (1-Discount.rate)

# 设置至尊会员折扣率为 20%
Discount.set_rate(0.2)
original_price = 200
final_price = Discount.calculate(original_price)
print(f"原价：{original_price} 鱼币，至尊会员折后价：{final_price} 鱼币")
# 原价：200 鱼币，至尊会员折后价：160.0 鱼币

# 动动手1：请创建一个日志记录器类 Logger，满足以下需求：
# 该类包含一个类属性 log_file，表示日志文件的名称，默认为 app.log。
# 实现一个类方法 set_log_file(cls, filename)，用于更改日志文件的名称。
# 实现一个静态方法 log(message)，用于将日志消息写入指定的日志文件。
# 日志消息需要包含时间戳和日志级别（如 INFO、WARNING、ERROR）。

import time

class Logger:
    log_file = "app.log"

    @classmethod
    def set_log_file(cls, filename):
        cls.log_file = filename

    @staticmethod
    def log(message, level="INFO"):
        with open(Logger.log_file, "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} [{level}]: {message}\n")

Logger.log("应用启动。", "INFO")
Logger.log("出现异常。", "ERROR")
Logger.log("用户登入。", "INFO")
Logger.log("内存空间不足。", "WARNING")

# 日志文件内容：
# 2026-09-22 18:39:51 [INFO]: 应用启动。
# 2026-09-22 18:39:51 [ERROR]: 出现异常。
# 2026-09-22 18:39:51 [INFO]: 用户登入。
# 2026-09-22 18:39:51 [WARNING]: 内存空间不足。


# 动动手2：在库存管理系统中，需要对产品进行管理。请创建一个产品类 Product，满足以下需求：
# 使用一个类属性 products，为一个列表，存储所有产品的实例。
# 实现一个类方法 add_product(cls, product)，用于将产品添加到 products 列表中。
# 实现一个静态方法 is_valid_product(product_info)，用于在添加产品前验证产品信息的有效性。
# 在产品实例化时，自动将自身添加到 products 列表中，并确保添加前通过验证。

class Product:
    products = []  # 类属性，存储所有产品实例
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        product_info = {'name': self.name, 'price': self.price}
        if self.is_valid_product(product_info):
            self.add_product(self)
            print(f"产品 '{self.name}' 添加成功。")
        else:
            print(f"无效的产品信息，无法添加产品 '{self.name}'。")
    
    @classmethod
    def add_product(cls, product):
        cls.products.append(product)
    
    @staticmethod
    def is_valid_product(product_info):
        # 验证产品名称为非空字符串，价格为正数
        if not product_info['name'] or not isinstance(product_info['name'], str):
            print("产品名称无效。")
            return False
        if product_info['price'] <= 0:
            print("产品价格必须为正数。")
            return False
        return True
    
# 添加产品信息
product1 = Product("苹果", 5)
product2 = Product("香蕉", 3)
product3 = Product("", 10)  # 无效名称
product4 = Product("橙子", -2)  # 无效价格
    
# 输出所有有效产品的信息
print("当前产品列表：")
for product in Product.products:
    print(f"产品名称：{product.name}，价格：{product.price}")


















