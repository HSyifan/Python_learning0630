"""魔法方法"""
# 继承str类。str类是不可变类型，不能__init__，所以用__new__
from re import X

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)

cs = CapStr("FishC")
print(cs) # FISHC

print(cs.lower()) # fishc

class C:
    def __init__(self):
        print("我来了~")
    def __del__(self):
        print("我走了~")

c = C()
d = c
del c
del d

# 在完全del之前，复活对象
class D:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        global x
        x = self

d = D("小甲鱼")
print(d) # <__main__.D object at 0x000001D6FA96BA70>
print(d.name)
del d
# print(d)
print(x) # <__main__.D object at 0x000001D6FA96BA70>
print(x.name) # 小甲鱼


class E:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def __del__(self):
        self.func(self) # 等于f(e)

def outer():
    x = 0
    def inner(y = None): # y是e
        nonlocal x
        if y: # e不为None，所以x = e
            x = y
        else:
            return x
    return inner

f = outer()
e = E("小狸狸", f)
print(e) # <__main__.E object at 0x00000211A629BE60>
print(e.name) # 小狸狸
del e

g = f()
print(g) # <__main__.E object at 0x00000211A629BE60>
print(g.name) # 小狸狸



# 动动手0：请按要求编写一个银行账户管理系统。
# a. 创建账户
# - 需要提供姓名和密码（要求密码需要以 MD5 哈希值的形式存储）
# - 银行卡号自动生成
# - 支持预存款
# b. 删除账户
# - 需要验证卡号、姓名和密码
# c. 查询余额
# - 需要验证卡号和密码
# d. 存款
# - 需要验证卡号和密码
# - 输入金额
# e. 取款
# - 需要验证卡号和密码
# - 输入金额，并检查余额是否足够
# f. 转账
# - 需验证我方卡号和密码，验证对方卡号是否存在
# - 输入金额，并检查我方余额是否足够
# ** 程序输入限制（如用户不按要求输入，必须予以纠正）：
# - 密码必须是 6 位数字
# - 金额必须是非负数
# - 卡号必须是正整数

import hashlib

class PasswdMixin:
    def check_password(self, password):
        password = str(password)
        while len(password) != 6 or not password.isdigit():
            password = input("密码必须是6位数字，请重新输入：")
        return hashlib.md5(password.encode("utf-8")).hexdigest()


class Account(PasswdMixin):
    """基本账户：只管理自己这一张卡的数据与存取转"""
    def __init__(self, name, card_number, password, balance=0):
        self.name = name
        self.card_number = card_number
        self.password = self.check_password(password)  # 存 MD5
        self.balance = balance

    def confirm_name(self, name):
        return self.name == name

    def confirm_passwd(self, password):
        return self.password == self.check_password(password)

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            print("金额不能为负数")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount < 0:
            print("金额不能为负数")
            return False
        if amount > self.balance:
            print("余额不足")
            return False
        self.balance -= amount
        return True

    def transfer(self, target_account, amount):
        if amount < 0:
            print("金额不能为负数")
            return False
        if amount > self.balance:
            print("余额不足")
            return False
        self.balance -= amount
        target_account.deposit(amount)
        return True


class UserManager(PasswdMixin):
    def __init__(self):
        self.accounts = {}         # {卡号: Account对象}
        self.next_card = 88888888  # 下一张待发放的卡号

    def _input_card(self, prompt="请输入卡号："):
        """卡号必须是正整数"""
        while True:
            raw = input(prompt)
            if raw.isdigit() and int(raw) > 0:
                return int(raw)
            print("卡号必须是正整数，请重新输入。")

    def _input_amount(self, prompt="请输入金额："):
        """金额必须是非负数"""
        while True:
            raw = input(prompt)
            try:
                amount = float(raw)
                if amount < 0:
                    print("金额不能为负数，请重新输入。")
                    continue
                return amount
            except ValueError:
                print("金额格式不正确，请重新输入。")

    def get_account(self, card_number):
        """按卡号取出账户；不存在返回 None"""
        return self.accounts.get(card_number)

    def check_account(self):
        """检查账户是否存在且密码正确，成功则返回该 Account 对象"""
        card = self._input_card()
        while card not in self.accounts:
            card = self._input_card("卡号不存在，请重新输入卡号：")
        acc = self.accounts[card]
        pwd = input("请输入密码：")
        while not acc.confirm_passwd(pwd):
            pwd = input("密码错误，请重新输入密码：")
        return acc

    def create_account(self):
        """创建账户：姓名、密码、可选预存款；卡号自动生成"""
        name = input("请输入姓名：")
        password = input("请输入密码：")
        balance = self._input_amount("请输入预存款金额（可为0）：")
        card = self.next_card
        acc = Account(name, card, password, balance)
        self.accounts[card] = acc
        self.next_card += 1
        print(f"开户成功！姓名：{name}，卡号：{card}，余额：{acc.get_balance()}")
        return acc

    def delete_account(self):
        """删除账户：验证卡号、姓名、密码"""
        card = self._input_card()
        while card not in self.accounts:
            card = self._input_card("卡号不存在，请重新输入卡号：")
        acc = self.accounts[card]
        name = input("请输入姓名：")
        while not acc.confirm_name(name):
            name = input("姓名不匹配，请重新输入姓名：")
        pwd = input("请输入密码：")
        while not acc.confirm_passwd(pwd):
            pwd = input("密码错误，请重新输入密码：")
        del self.accounts[card]
        print(f"卡号 {card} 已删除。")

    def query_balance(self):
        acc = self.check_account()
        print(f"卡号 {acc.card_number} 当前余额：{acc.get_balance()}")

    def do_deposit(self):
        acc = self.check_account()
        amount = self._input_amount("请输入存款金额：")
        if acc.deposit(amount):
            print(f"存款成功，当前余额：{acc.get_balance()}")

    def do_withdraw(self):
        acc = self.check_account()
        amount = self._input_amount("请输入取款金额：")
        if acc.withdraw(amount):
            print(f"取款成功，当前余额：{acc.get_balance()}")
        else:
            # 余额不足时允许重新输入金额
            while True:
                amount = self._input_amount("请重新输入取款金额：")
                if acc.withdraw(amount):
                    print(f"取款成功，当前余额：{acc.get_balance()}")
                    break

    def do_transfer(self):
        acc = self.check_account()
        target_card = self._input_card("请输入对方卡号：")
        while target_card not in self.accounts:
            target_card = self._input_card("对方卡号不存在，请重新输入：")
        while target_card == acc.card_number:
            target_card = self._input_card("不能转给自己，请重新输入对方卡号：")
            while target_card not in self.accounts:
                target_card = self._input_card("对方卡号不存在，请重新输入：")
        target = self.accounts[target_card]
        amount = self._input_amount("请输入转账金额：")
        if acc.transfer(target, amount):
            print(f"转账成功。您的余额：{acc.get_balance()}，对方余额：{target.get_balance()}")
        else:
            while True:
                amount = self._input_amount("请重新输入转账金额：")
                if acc.transfer(target, amount):
                    print(f"转账成功。您的余额：{acc.get_balance()}，对方余额：{target.get_balance()}")
                    break

    def welcome(self):
        print("欢迎使用银行账户管理系统")
        ins = ""
        while ins != "7":
            ins = input(
                "1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出："
            )
            if ins == "1":
                self.create_account()
            elif ins == "2":
                self.delete_account()
            elif ins == "3":
                self.query_balance()
            elif ins == "4":
                self.do_deposit()
            elif ins == "5":
                self.do_withdraw()
            elif ins == "6":
                self.do_transfer()
            elif ins == "7":
                print("感谢使用，再见。")
            else:
                print("输入无效，请重新选择。")


def main():
    um = UserManager()
    um.welcome()


main()


# 欢迎使用银行账户管理系统
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：1
# 请输入姓名：吴美美
# 请输入密码：12345
# 请输入预存款金额（可为0）：300
# 密码必须是6位数字，请重新输入：123456
# 开户成功！姓名：吴美美，卡号：88888888，余额：300.0
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：1
# 请输入姓名：粟云云
# 请输入密码：234567
# 请输入预存款金额（可为0）：350
# 开户成功！姓名：粟云云，卡号：88888889，余额：350.0
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：4
# 请输入卡号：88888888
# 请输入密码：123456
# 请输入存款金额：100
# 存款成功，当前余额：400.0
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：3
# 请输入卡号：88888889
# 请输入密码：234567
# 卡号 88888889 当前余额：350.0
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：6
# 请输入卡号：88888889
# 请输入密码：234567
# 请输入对方卡号：88888888
# 请输入转账金额：100
# 转账成功。您的余额：250.0，对方余额：500.0
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：5
# 请输入卡号：88888888
# 请输入密码：123456
# 请输入取款金额：200
# 取款成功，当前余额：300.0
# 1.创建账户 2.删除账户 3.查询余额 4.存款 5.取款 6.转账 7.退出：7
# 感谢使用，再见。

























