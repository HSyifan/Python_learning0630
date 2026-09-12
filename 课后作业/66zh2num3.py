# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-214864-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

class ZH_FLOAT:    
    def __init__(self, num):
        self.num = num

    def __float__(self):
        units = {"十": 10, "拾":10, "百": 100, "佰": 100, "千": 1000, "仟": 1000,
                 "万": 10000, "萬": 10000, "亿": 100000000, "億": 100000000}
        digits = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
                  "七": 7, "八": 8, "九": 9, "壹": 1, "贰": 2, "叁": 3, "肆": 4,
                  "伍": 5, "陆": 6, "柒": 7, "捌": 8, "玖": 9, "两": 2}
        
        # 处理整数部分
        def process_integer_part(n):
            unit = 0        # 初始单位
            section = []    # 存放字符串拆解后的数据片段
            temp = 0        # 临时变量

            for i in range(len(n)-1, -1, -1):
                char = n[i]
                if char in units:
                    unit = units[char]
                    # 万和亿需要单独存储，因为需要考虑处理一百万，十亿这类重复单位的数字
                    if unit == 10000 or unit == 100000000:
                        section.append(unit)
                        unit = 1
                elif char in digits:
                    temp = digits[char]
                    # 如果有单位，则乘以单位代表的数值
                    if unit:
                        temp *= unit
                        unit = 0
                    section.append(temp)
                else:
                    raise ValueError(f"[{char}]是无效字符。")

            # “十”要单独处理，因为我们不会说“一十五”，而是习惯直接说“十五”
            # 而对于百、千、万，我们会说是“一百”，“一千”或者“一百万”
            if unit == 10:
                section.append(10)

            # 接下来将数据片段拼接起来即可 
            result = 0
            temp = 0

            for each in reversed(section):
                if each == 10000 or each == 100000000:
                    result += temp * each
                    temp = 0
                else:
                    temp += each
                    
            result += temp
            return result

        # 处理小数部分
        def process_decimal_part(d):
            result = 0
            # 0.2 = 2 * 10**(-1)
            # 0.25 = 2 * 10**(-1) + 5 * 10**(-2)
            # ...
            for i, char in enumerate(d):
                if char in digits:
                    result += digits[char] * (10 ** -(i + 1))
                else:
                    try:
                        result += int(char) * (10 ** -(i + 1))
                    except ValueError:
                        raise ValueError(f"[{char}]是无效字符。")
                    
            return result
            
        try:
            return float(self.num)
        except ValueError:
            if "点" in self.num: 
                integer_part, decimal_part = self.num.split("点", 1)
            elif "點" in self.num:
                integer_part, decimal_part = self.num.split("點", 1)
            else:
                # 如果没有小数点则直接当作整数处理完返回
                return process_integer_part(self.num)

            integer_result = process_integer_part(integer_part)
            decimal_result = process_decimal_part(decimal_part)

            return float(integer_result + decimal_result)



  
