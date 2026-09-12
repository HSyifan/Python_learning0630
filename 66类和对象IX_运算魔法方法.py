"""运算符号，魔法方法"""
# __add__方法：当左边的对象支持加法运算时，会调用左边的对象的__add__方法
class S(str):
    def __add__(self, other):
        return len(self) + len(other)

s1 = S("FishC")
s2 = S("Python")
print(s1 + s2) # 11

print(s1 + "Python") # 11
print("FishC" + s2) # FishCPython

# __radd__方法：当左边的对象不支持加法运算时，会调用右边的对象的__radd__方法
class S1(str):
    def __add__(self, other):
        return NotImplemented

# __radd__,只能作用于不同的类
class S2(str):
    def __radd__(self, other):
        return len(self) + len(other)

s1 = S1("Apple")
s2 = S2("Banana")
print(s1 + s2) # 11,调用到了__radd__方法
print(s2 + s1) # BananaApple

# __iadd__方法：x += y（由运算符左侧的对象 x 触发）
class S1(str):
    def __iadd__(self, other):
        return len(self) + len(other)

s1 = S1("FishC")
s2 = S2("Banana")
s1 += s2

print(s1) # FishCPython
print(type(s1)) # <class 'int'>

s2 += s2
print(s2) # BananaBanana
print(type(s2)) # <class 'str'>

# 通过 __int__() 拦截 int() 函数的调用流程，让它在原来的基础上添加了对中文数字的识别
class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            zh = {
                "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
                "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
                "壹": 1, "贰": 2, "叁": 3, "肆": 4, "伍": 5,
                "陆": 6, "柒": 7, "捌": 8, "玖": 9
            }

            result = 0

            for each in self.num:
                if each in zh:
                    result += zh[each]
                else:
                    result += int(each)
                result *= 10

            return result // 10

n = ZH_INT("520")
print(int(n)) # 520

n = ZH_INT(3.14)
print(int(n)) # 3

n = ZH_INT("五贰零")
print(int(n)) # 520


# 动动手0：将中文转化为整数的对象 ZH_INT，优化~
# 这个实现有一个问题：它仅支持不包含单位（如十、百、千等）的中文数字转换，比如你让它处理像 “二百五”、”一千零二十四” 这些字符串，就无能为力了。
# 那么现在第一个任务就是开发一个支持中文数字单位的 ZH_INT，实现以下效果：

class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)  # "520"、3.14 仍走原来的路
        except (ValueError, TypeError):
            return self._zh_to_int(str(self.num))

    def _zh_to_int(self, text):
        """三个累计值从左扫到右：数字记下，十百千并进节，万亿放大后并进总额"""
        digits = {
            "零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
            "壹": 1, "贰": 2, "叁": 3, "肆": 4, "伍": 5,
            "陆": 6, "柒": 7, "捌": 8, "玖": 9,
        }
        small = {"十": 10, "百": 100, "千": 1000}     # 一节内部
        big = {"万": 10000, "亿": 100000000}          # 整节放大

        total = 0      # 已经乘过万/亿
        section = 0    # 当前这一节（千百十个）
        number = 0     # 刚读到、还没乘单位的数字

        for ch in text:
            if ch in digits:
                number = digits[ch]
            elif ch in small:
                if number == 0:      # 「十二」：十前面没数字，默认 1
                    number = 1
                section += number * small[ch]
                number = 0
            elif ch in big:
                section += number    # 先收尾这一节
                total += section * big[ch]
                section = 0
                number = 0
            # 「零」已经在 digits 里，值为 0，不会把后面的位撑错

        section += number            # 个位还挂在 number 上
        total += section
        return total

print(int(ZH_INT("两百五十"))) # 250
print(int(ZH_INT("一千零二十四"))) # 1024
print(int(ZH_INT("两亿九千九百七十九万两千四百五十八"))) # 299792458


# 动动手1：第二个任务让我们编写一个 ZH_FLOAT，使其支持浮点数的转换，实现效果如下：

class ZH_FLOAT:
    def __init__(self, num):
        self.num = num

    def __float__(self):
        try:
            return float(self.num)  # "520"、3.14 仍走原来的路
        except (ValueError, TypeError):
            return self._zh_to_float(str(self.num))

    def _zh_to_float(self, text):
        """三个累计值从左扫到右：数字记下，十百千并进节，万亿放大后并进总额"""
        digits = {
            "零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
            "壹": 1, "贰": 2, "叁": 3, "肆": 4, "伍": 5,
            "陆": 6, "柒": 7, "捌": 8, "玖": 9,
        }
        small = {"十": 10, "百": 100, "千": 1000}     # 一节内部
        big = {"万": 10000, "亿": 100000000}          # 整节放大

        total = 0      # 已经乘过万/亿
        section = 0    # 当前这一节（千百十个）
        number = 0     # 刚读到、还没乘单位的数字

        text = text.split("点")
        integer_part = text[0]
        decimal_part = text[1]

        for ch in integer_part:
            if ch in digits:
                number = digits[ch]
            elif ch in small:
                if number == 0:      # 「十二」：十前面没数字，默认 1
                    number = 1
                section += number * small[ch]
                number = 0
            elif ch in big:
                section += number    # 先收尾这一节
                total += section * big[ch]
                section = 0
                number = 0
            # 「零」已经在 digits 里，值为 0，不会把后面的位撑错

        section += number            # 个位还挂在 number 上
        total += section

        decimal_total = ""

        for ch in decimal_part:
            if ch in digits:
                decimal_total += str(digits[ch])

        return float(str(total) + "." + decimal_total)


print(float(ZH_FLOAT("二百五十点零二五")))
print(float(ZH_FLOAT("一千零二十四点八八八")))
print(float(ZH_FLOAT("一亿零三百八十六万零六十八点二五")))











