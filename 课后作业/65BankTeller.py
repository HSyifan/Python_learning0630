# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-214864-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

import hashlib

# Mixin类：密码相关的功能组件
class PasswdMixin:
    # 密码长度检测
    def is_valid(self, passwd):
        while True:
            if len(passwd) != 6 or not passwd.isdigit():
                passwd = input("密码需为6位数字，请重新输入：")
            else:
                break
        return passwd

    # 将明文密码转换为MD5
    def to_md5(self, passwd):
        bstr = bytes(passwd, "utf-8")
        passwd = hashlib.md5(bstr).hexdigest()
        return passwd


# 基本账户类
class Account:
    def __init__(self, num, name, passwd, money=0):
        self.num = num
        self.name = name
        self.passwd = passwd
        self.balance = money

    # 确认姓名是否匹配
    def confirm_name(self, name):
        return name == self.name

    # 确认密码是否匹配            
    def confirm_passwd(self, passwd):
        return passwd == self.passwd

    # 取款
    def withdraw(self, money):
        if money > self.balance:
            print("余额不足，取款失败！")
        else:
            self.balance -= money
            print(f"成功取出{money}元。")

    # 存款
    def deposit(self, money):
        self.balance += money
        print(f"成功存入{money}元。")

    # 转账
    def transfer(self, account, money):
        if money > self.balance:
            print("余额不足。")
        else:
            self.balance -= money
            account.balance += money
            print("转账成功。")

    # 查询余额
    def get_balance(self):
        return self.balance


# 账户管理类
class UserManager(PasswdMixin):
    def __init__(self):
        self.accounts = {}
        self.num = 88888888

    # 检查账户是否存在及密码是否正确
    def check_account(self, num, passwd):
        if num in self.accounts:
            account = self.accounts[num]
            passwd_md5 = self.to_md5(passwd)
            if account.confirm_passwd(passwd_md5):
                return True
            else:
                print("密码错误。")
                return False
        else:
            print("该账户不存在。")
            return False

    # 创建账户
    def create_account(self, name, passwd, money=0):
        passwd = self.is_valid(passwd)
        passwd_md5 = self.to_md5(passwd)
        account = Account(self.num, name, passwd_md5, money)
        self.accounts[self.num] = account
        print(f"创建成功，卡号是：{self.num}")
        self.num += 1

    # 删除账户
    def delete_account(self, num, name, passwd):
        if self.check_account(num, passwd):
            account = self.accounts[num]
            if account.confirm_name(name):
                del self.accounts[num]
                print(f"卡号（{num}）已成功注销。")
            else:
                print("抱歉，姓名核对出错。")
    
    # 获取账户
    def get_account(self, num, passwd, nopasswd=False):
        if nopasswd:
            account = self.accounts.get(num)
            if account:
                return account
            else:
                print("该账户不存在。")
                return None
        else:
            if self.check_account(num, passwd):
                return self.accounts[num]
            else:
                return None


# 主函数
def main():
    bank = UserManager()

    # 获取信息
    def get_msg(num=False, name=False, passwd=False):
        msg = {'num':None, 'name':None, 'passwd':None}
        if num:
            msg['num'] = get_integer_input("请输入卡号：")
        if name:
            msg['name'] = input("请输入姓名：")
        if passwd:
            msg['passwd'] = input("请输入密码：")
        return msg

    # 获取整数输入
    def get_integer_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError
                break
            except ValueError:
                print("请输入一个有效的整数！")
        return value

    # 获取浮点数输入
    def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("请输入一个有效的数值！")
        return value
    
    while True:
        ins = input("\n1.创建账户/2.删除账户/3.查询余额/4.存款/5.取款/6.转账/7.退出：")

        if ins == '1':
            msg = get_msg(num=False, name=True, passwd=True)
            money = get_float_input("请输入预存款：")
            bank.create_account(msg['name'], msg['passwd'], round(money, 2))
            
        elif ins == '2':
            msg = get_msg(num=True, name=True, passwd=True)
            bank.delete_account(msg['num'], msg['name'], msg['passwd'])

        elif ins == '3':
            msg = get_msg(num=True, name=False, passwd=True)
            account = bank.get_account(msg['num'], msg['passwd'])
            if account:
                print(f"您的余额是：{account.get_balance()}")

        elif ins == '4':
            msg = get_msg(num=True, name=False, passwd=True)
            account = bank.get_account(msg['num'], msg['passwd'])
            if account:
                money = get_float_input("请输入金额：")
                account.deposit(round(money, 2))

        elif ins == '5':
            msg = get_msg(num=True, name=False, passwd=True)
            account = bank.get_account(msg['num'], msg['passwd'])
            if account:
                money = get_float_input("请输入金额：")
                account.withdraw(round(money, 2))

        elif ins == '6':
            msg = get_msg(num=True, name=False, passwd=True)
            account = bank.get_account(msg['num'], msg['passwd'])
            if account:
                target_num = get_integer_input("请输入收款人卡号：")
                target_account = bank.get_account(target_num, None, nopasswd=True)
                if target_account:
                    money = get_float_input("请输入金额：")
                    account.transfer(target_account, round(money, 2))

        elif ins == '7':
            break
        
        else:
            print("无效的输入，请输入1-7之间的数字。")
