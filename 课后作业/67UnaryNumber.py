# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-215530-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

class UnaryNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value < 0:
            return '-' + '1' * abs(self.value)
        elif self.value == 0:
            return "没有"
        else:
            return '1' * self.value

    def __int__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value + other.value)
        else:
            raise ValueError("类型不同无法相加")

    def __sub__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value - other.value)
        else:
            raise ValueError("类型不同无法相减")

    def __mul__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value * other.value)
        else:
            raise ValueError("类型不同无法相乘")

    def __truediv__(self, other):
        if isinstance(other, UnaryNumber):
            if other.value != 0:
                return UnaryNumber(self.value // other.value)
            else:
                raise ValueError("除数不能为0")
        else:
            raise ValueError("类型不同无法相除")

    def __floordiv__(self, other):
        if isinstance(other, UnaryNumber):
            if other.value != 0:
                return UnaryNumber(self.value // other.value)
            else:
                raise ValueError("除数不能为0")
        else:
            raise ValueError("类型不同无法相除")
