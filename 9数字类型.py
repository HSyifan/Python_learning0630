import decimal

"""浮点数"""
print(0.1+0.2) # 0.30000000000000004 因为float的精度有限，会导致精度丢失

# i = 0
# while i < 1:
#     i = i + 0.1
#     print(i)

print(0.3 == 0.1 + 0.2) # False 因为float的精度有限，会导致精度丢失

"""小数"""
# 小数只能用decimal模块来表示，不能用float来表示，因为float的精度有限，会导致精度丢失
a = decimal.Decimal('0.1') 
b = decimal.Decimal('0.2')
print(a + b)

c = decimal.Decimal('0.3')
print(c == a + b)

"""复数"""
x = 1 + 2j
print(x.real) # 打印x的实部
print(x.imag) # 打印x的虚部

"""函数"""
# x + y # x加y的结果
# x - y # x减y的结果
# x * y # x乘y的结果
# x / y # x除y的结果
# x // y # x除y的整数部分 取比目标结果小的最大整数 eg: -3 // 2 = -2
# x % y # x除y的余数 
#      x == y * (x // y) + (x % y)
# -x # x的负数
# +x # x本身
# abs(x) # x的绝对值 eg: abs(1 + 2j) = sqrt(1^2 + 2^2) = sqrt(5) = 2.236 复数的模
# int(x) # 把x转换为整数
# float(x) # 把x转换为浮点数
# complex(re, im) # 返回一个复数，re为实部，im为虚部 eg：complex("1+2j") = 1 + 2j, 不能写成complex("1 + 2j") 中间不能有空格，会报错
# c.conjugate() # 返回c的共轭复数
# divmod(x, y) # 返回x除以y的商和余数 (x//y, x%y)  eg: divmod(-3, 2) = (-2, 1)
# pow(x, y) # 返回x的y次方 pow可以有三个参数 eg： pow(2, 3, 5) = 2 ** 3 % 5 = 3
# x ** y # 返回x的y次方

