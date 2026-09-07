# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-214131-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

import time
import hashlib

# 会员类：记录会员的关键信息
class Member:
    def __init__(self, cardid, name, passwd, scores, regdate):
        self.cardid = cardid
        self.name = name
        self.passwd = passwd
        self.scores = scores
        self.regdate = regdate


# Mixin类：密码相关的功能组件
class PasswdMixin:
    # 密码长度检测
    def is_tooshort(self, passwd, require=6):
        while len(passwd) < require:
            passwd = input("会员密码不能小于6位，请重新输入：")
        return passwd

    # 将明文密码转换为MD5
    def to_md5(self, passwd):
        bstr = bytes(passwd, "utf-8")
        passwd = hashlib.md5(bstr).hexdigest()
        return passwd


# Mixin类：日志记录相关的功能组件
class LoggerMixin:
    def log(self, message, filename="log.txt"):
        with open(filename, "a") as f:
            f.write(message)

    
# 管理类：所有功能的实现    
class Manage(PasswdMixin, LoggerMixin):
    def __init__(self):
        self.members = {}
        self.cardid = 10000

    # 程序功能入口
    def welcome(self):
        ins = 0
        print("欢迎使用鱼C超市会员管理系统")
        while ins != '5':
            ins = input("\n1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
            if ins == '1':
                self.create_member()
            if ins == '2':
                self.modify_passwd()
            if ins == '3':
                self.pay_money()
            if ins == '4':
                self.view_scores()
            if ins == '5':
                print("感谢使用鱼C超市会员管理系统")

    # 确认卡号及密码是否匹配            
    def confirm_passwd(self):
        cardid = int(input("请输入卡号："))
        while not self.members.get(cardid):
            cardid = int(input("该卡号不存在，请重新输入："))
            
        passwd = input("请输入密码：")
        passwd = self.to_md5(passwd)
        while not self.members.get(cardid).passwd == passwd:
            passwd = input("密码不正确，请重新输入：")
            passwd = self.to_md5(passwd)

        return cardid

    # 程序功能：创建新卡
    def create_member(self):
        name = input("请输入名字：")
        passwd = input("请输入密码：")
        passwd = self.is_tooshort(passwd)
        passwd = self.to_md5(passwd)
        scores = 0
        regdate = time.localtime()
        member = Member(self.cardid, name, passwd, scores, regdate)
        self.members[self.cardid] = member
        print(f"创建成功，卡号为 {self.cardid}，关联用户 -> {name}")
        self.log(f"开卡成功：{self.cardid} -> {name}，时间：{time.strftime('%Y-%m-%d %H:%M:%S', regdate)}\n")
        self.cardid += 1

    # 程序功能：修改密码
    def modify_passwd(self):        
        cardid = self.confirm_passwd()
        newpasswd = input("请输入新密码：")
        newpasswd = self.is_tooshort(newpasswd)
        newpasswd = self.to_md5(newpasswd)
        self.members[cardid].passwd = newpasswd
        self.log(f"修改密码：卡号 -> {self.cardid}，时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
        print("密码修改成功。")

    # 程序功能：商品支付
    def pay_money(self):
        cardid = self.confirm_passwd()
        money = int(input("请输入支付金额："))
        self.members[cardid].scores += money
        self.log(f"积分累计：卡号 -> {self.cardid}，+{money}分，时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")

    # 程序功能：积分查询
    def view_scores(self):
        cardid = self.confirm_passwd()
        print(f"卡号 {cardid} 当前的消费积分为：{self.members[cardid].scores}")


def main():
    m = Manage()
    m.welcome()
