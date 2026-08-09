"""字符串符号位格式化"""
# 正数前面加+，负数前面加-
print("{:+}{:-}".format(520, -250)) # +520-250

# 千分位分隔符
print("{:,}".format(1234)) # 1,234
print("{:_}".format(1234)) # 1_234
print("{:,}".format(123)) # 123
print("{:,}".format(123456789)) # 123,456,789


# 对于[type]设置为'f或'F'的浮点数来说，是限定小数点后显示多少个数位
# 对于[type]设置为'g’或'G'的浮点数来说，是限定小数点前后一共显示多少个数位
# 对于非数字类型来说，限定的是最大字段的大小
# 对于整数类型来说，则不允许使用[.precision]选项

# 限定小数点后显示多少个数位
print("{:.2f}".format(123.456)) # 123.46

# 限定小数点前后一共显示多少个数位
print("{:.2g}".format(123.456)) # 1.2e+02

# 限定字符串最大显示多少个字符
print("{:.6}".format("I love FishC")) # I love

# 精度不能运用在整数上 
# print("{:.2}".format(123)) # 报错。精度不能运用在整数上 


# 将整数转换为二进制
print("{:b}".format(80)) # 1010000
print("{:#b}".format(80)) # 0b1010000

# 将整数转换为Unicode字符
print("{:c}".format(80)) # P。 

# 将整数转换为十进制
print("{:d}".format(80)) # 80

# 将整数转换为八进制
print("{:o}".format(80)) # 120
print("{:#o}".format(80)) # 0o120

# 将整数转换为十六进制
print("{:x}".format(80)) # 50
print("{:#x}".format(80)) # 0x50

# 将整数转换为十六进制大写字母
print("{:X}".format(80)) # 50

# 跟'd'类似，不同之处在于它会使用当前语言环境设置的分隔符插入到恰当的位置
print("{:n}".format(80)) # 80



# 将浮点数转换为科学计数法
print("{:e}".format(3.1415926)) # 3.141593e+00
print("{:E}".format(3.1415926)) # 3.141593E+00

# 将参数以定点表示法的形式输出(“不是数”用'nan'标示，无穷用'inf标示，默认精度为6)
print("{:f}".format(3.1415)) # 3.141500

# 通用格式，小数以f形式输出，大数以'e的形式输出
print("{:g}".format(31415926)) # 3.141593e+07
print("{:g}".format(3.1415926)) # 3.14159

# 将参数转换为百分比形式(默认显示小数点后6位)
print("{:%}".format(0.98)) # 98.000000%

print("{:.2%}".format(0.98)) # 98.00%

# prec: 精度，ty: 类型
print("{:.{prec}f}".format(3.1415, prec=2)) # 3.14

# fill: 填充字符，align: 对齐方式，width: 宽度，prec: 精度，ty: 类型
print("{:{fill}{align}{width}.{prec}{ty}}".format(3.1415, fill='+', align='^', width=10, prec=3, ty='g')) # +++3.14+++

# 语法糖：f-string
year = 2010
print(f"鱼C工作室成立于{year}年") # 鱼C工作室成立于2010年

print(f"1+2={1+2}. 2的平方是{2*2}. 3的立方是{3*3*3}") # 1+2=3. 2的平方是4. 3的立方是27

print("{-520:010}") # {-520:010}
print(f"{-520:010}") # -000000520

print(f"{123456789:,}") # 123,456,789

print(f"{123.456:.2f}") # 123.46


# 练习题：
print(f"{{1 + 2}}") # {1 + 2}
print(f"{{{1 + 2}}}")
# print(f"{520:.2}") 

# 动动手0：利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。比如，字符串 FFiiiisshCCCCCC 压缩后变成 FFi4sshC6。
# 对于重复次数小于 3 的字符，我们的程序应该选择不对其进行压缩。

dds0_input = input("请输入待压缩字符串：")

result = ""
i = 0
while i < len(dds0_input):
    ch = dds0_input[i]
    count = 1
    # 统计当前字符连续出现的次数
    while i + count < len(dds0_input) and dds0_input[i + count] == ch:
        count += 1
    # 重复次数小于 3：不压缩，原样输出
    if count < 3:
        result += ch * count
    else:
        result += ch + str(count)
    i += count

# i = 0
# while i < 长度:
#     取出起点元素
#     用内循环/计数，找出这一段有多长
#     根据这段长度做处理（拼结果 / 判断）
#     i 跳到这段之后

print(f"压缩后：{result}")
if len(dds0_input) > 0:
    rate = len(result) / len(dds0_input) * 100
    print(f"压缩率为：{rate:.0f}%")

# 动动手1：请大家编写一个解压程序，将上一题压缩后的字符串进行解压缩。
# 字符串 FFi4sshC6 解压缩后变成 FFiiiisshCCCCCC 
dds1_input = input("请输入待解压字符串：")

result = ""
i = 0
while i < len(dds1_input):
    ch = dds1_input[i]
    # 统计当前字符连续出现的次数
    if i + 1 < len(dds1_input) and dds1_input[i + 1].isnumeric():
        count = int(dds1_input[i + 1])
        result += ch * count
        i += 2
    else:
        result += ch
        i += 1

print(f"解压后的字符串：{result}")
