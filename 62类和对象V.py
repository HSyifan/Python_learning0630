"""Mix-in类"""
# Mixin（混入） = 一小包“可拼上去的能力”，本身通常不当完整业务类用，而是混进别的类里，给它多几个方法。
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我叫{self.name}，今年{self.age}岁。")

class FlyMixin:
    def fly(self):
        print("哦豁，我还会飞~")

class Pig(Animal, FlyMixin):
    def special(self):
        print("我的技能是拱大白菜~")

p = Pig("大肠", 5)
p.say()
p.special()
p.fly()


class Displayer:
    def display(self, message):
        print(message)

class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        with open(filename, "a") as f:
            f.write(message)

    def display(self, message):
        super().display(message) # 根据实例的mro顺序，这里的display会在Displayer类中找
        self.log(message) # 这里的log在MySubClass类中找


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename="subclasslog.txt")


# subclass = MySubClass()
# subclass.display("This is a test.")

print(MySubClass.mro())
# [<class '__main__.MySubClass'>, <class '__main__.LoggerMixin'>, <class '__main__.Displayer'>, <class 'object'>]  


# 练习题：
class A:
    def say_hi(self):
        print("Hi from A~")
    def say(self):
        super().say_hi()
class B1(A):
    def say_hi(self):
        print("Hi from B1~")
    def say(self):
        super().say()
class B2:
    def say_hi(self):
        print("Hi from B2~")
   
    def say(self):
        super().say()
class C(B1, B2):
    def say(self):
        super().say()
c = C()
c.say()
# 请问这里会打印什么内容？

print(C.mro())


class A:
    def say(self):
        print("FishA")
class B:
    def say(self):
        print("FishB")
        
class C(A):
    def say(self):
        super().say()
        print("FishC")
        
class D(B):
    def say(self):
        super().say()
        print("FishD")
class E(C, D):
    def say(self):
        super().say()
        print("FishE")
e = E()
e.say()
# 请问这里会打印什么内容？


# 动动手0：这次要求大家编写一个鱼C超市会员管理系统。
# 1. 会员开卡
# - 会员开卡自动赋予一个新的卡号（默认从 10000 开始递增）
# - 要求输入用户名和密码
# - 密码要求长度不低于 6 位
# 2. 修改密码
# - 先确认输入卡号是否存在
# - 再判断旧密码是否正确
# - 新密码长度同样不能低于 6 位
# 3. 商品支付
# - 先确认输入卡号是否存在
# - 再判断密码是否正确
# - 根据输入的消费金额增加会员卡积分（比如输入 250 消费金额，那么积分增加 250）
# 4. 积分查询
# - 先确认输入卡号是否存在
# - 再判断密码是否正确
# 代码要求：
# 1. 创建一个会员类（Member），包含信息：卡号、用户名、密码（要求密码需要以 MD5 哈希值的形式存储）、积分、注册日期
# 2. 创建一个管理类（Manage），用于实现上方要求的主要程序功能
# 3. 创建一个 Mixin 类（PasswdMixin），用于实现密码相关的功能组件（密码长度检测和将明文密码转换为 MD5 的操作）
# 4. 创建一个 Mixin 类（LoggerMixin），用于实现日志记录相关的功能组件

import datetime
import hashlib

class PasswdMixin:
    def check_password(self, password):
        while len(password) < 6:
            password = input("会员密码长度不能小于6位，请重新输入：")
        bstr = bytes(str(password), "utf-8")
        hash_passwd = hashlib.md5(bstr).hexdigest() # 计算哈希值
        return hash_passwd

class Member:
    def __init__(self, name, card_number, password, integral, register_date):
        self.name = name
        self.card_number = card_number
        self.password = password
        self.integral = integral
        self.register_date = register_date

class LoggerMixin:
    def log(self, message, filename="log.txt"):
        # import datetime 时要用 datetime.datetime.now()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as f:
            f.write(f"{message}, 时间: {now}\n")

class Manage(PasswdMixin, LoggerMixin):
    def __init__(self):
        self.members = {}       # {卡号: Member对象}
        self.next_card = 10000  # 下一张待发放的卡号

    def welcome(self):
        ins = 0
        print("欢迎使用鱼C超市会员管理系统")
        while ins != '5':
            ins = input("1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
            if ins == '1':
                self.open_card()
            if ins == '2':
                self.change_password()
            if ins == '3':
                self.pay()
            if ins == '4':
                self.query_integral()
            if ins == '5':
                print("感谢使用鱼C超市会员管理系统")

    def _authenticate(self):
        """校验卡号存在且密码正确，返回本次操作的卡号"""
        card = int(input("请输入卡号："))
        while card not in self.members:
            card = int(input("卡号不存在，请重新输入卡号："))
        pwd = self.check_password(input("请输入密码："))
        while pwd != self.members[card].password:
            pwd = self.check_password(input("密码错误，请重新输入密码："))
        return card

    def open_card(self):
        name = input("请输入名字：")
        password = self.check_password(input("请输入密码："))
        card = self.next_card   # 本次新卡的卡号
        member = Member(name, card, password, 0, datetime.datetime.now())
        self.members[card] = member
        print(f"创建成功，卡号为 {card}, 关联用户 -> {name}")
        self.log(f"开卡成功: {card} -> {name}")
        self.next_card += 1     # 准备下一张号
        return member
        
    def change_password(self):
        card = int(input("请输入卡号："))
        while card not in self.members:
            card = int(input("卡号不存在，请重新输入卡号："))
        old = self.check_password(input("请输入旧密码："))
        while old != self.members[card].password:
            old = self.check_password(input("旧密码错误，请重新输入旧密码："))
        new_password = self.check_password(input("请输入新密码："))
        self.members[card].password = new_password
        print("密码修改成功。")
        self.log(f"修改密码: 卡号 -> {card}")
        return self.members[card]

    def pay(self):
        card = self._authenticate()
        amount = int(input("请输入支付金额："))
        self.members[card].integral += amount
        self.log(f"积分累计: 卡号 -> {card}, +{amount}分")

    def query_integral(self):
        card = self._authenticate()
        print(f"卡号 {card} 当前的消费积分为: {self.members[card].integral}")


def main():
    manage = Manage()          # 整个系统只用这一个管理器
    manage.welcome()

main()

# 欢迎使用鱼C超市会员管理系统
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：1
# 请输入名字：吴美美
# 请输入密码：12345
# 会员密码长度不能小于6位，请重新输入：123456
# 创建成功，卡号为 10000, 关联用户 -> 吴美美
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：2
# 请输入卡号：10000
# 请输入旧密码：123456
# 请输入新密码：1234567
# 密码修改成功。
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：4
# 请输入卡号：10000
# 请输入密码：1234567
# 卡号 10000 当前的消费积分为: 0
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：3
# 请输入卡号：10000
# 请输入密码：1234567
# 请输入支付金额：300
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：4
# 请输入卡号：10000
# 请输入密码：1234567
# 卡号 10000 当前的消费积分为: 300
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：1
# 请输入名字：粟云云
# 请输入密码：888888
# 创建成功，卡号为 10001, 关联用户 -> 粟云云
# 1.创建新卡; 2.修改密码; 3.商品支付; 4.积分查询; 5.退出程序：5
# 感谢使用鱼C超市会员管理系统，再见！







































