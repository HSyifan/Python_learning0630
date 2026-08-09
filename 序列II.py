"""列表，元组，字符串的相互转化"""

# 列表转换为字符串和元组
print(list("FishC"))
print(list((1, 2, 3, 4, 5)))

# 元组转换为字符串和列表
print(tuple("FishC"))
print(tuple([1, 2, 3, 4, 5]))

# 字符串转换为列表和元组
print(str([1, 2, 3, 4, 5]))
print(str((1, 2, 3, 4, 5)))

# min和max函数

s = [1, 1, 2, 3, 5]
print(min(s)) # 1

# max比较数字大小和字母的编码值的大小
t = "FishC"
print(max(t)) # s

s = []
print(min(s, default = "屁，啥都没有，怎么找到最小？"))

# len()和sum()函数

# print(len(range(2**100))) # 报错，读取C语言结构体里的对象长度，长度太大了.

s = [1, 0, 0, 8, 6]
print(sum(s)) # 15

# start是起始值，sum是累加器
sum(s, start = 100) # 115


# sorted()可以对任何序列进行排序
# sort()只能对列表进行排序
s = [1, 2, 3, 0, 6]

# sorted()函数是排序函数，返回一个新的列表
print(sorted(s)) # [0, 1, 2, 3, 6]

# sort()函数是排序函数，直接修改原列表
print(s.sort())
print(s) # [0, 1, 2, 3, 6]

# reverse = True是反向排序
print(sorted(s, reverse = True)) # [6, 3, 2, 1, 0]

t = ["FishC", "Apple", "Book", "Banana", "Pen"]

# sorted()函数对比每一个字母的编码值
print(sorted(t)) # ['Apple', 'Banana', 'Book', 'FishC', 'Pen']

# key = len是按照长度排序
print(sorted(t, key = len)) # ['Pen', 'Book', 'FishC', 'Apple', 'Banana']

t.sort(key = len)
print(t) # ['Pen', 'Book', 'FishC', 'Apple', 'Banana']

print(sorted("FishC")) # ['C', 'F', 'h', 'i', 's']
print(sorted((1, 0, 0, 8, 6))) # [0, 0, 1, 6, 8]

# reversed()函数返回的是一个迭代器，不是列表
# reverse()函数直接修改原列表
# reversed()可以对任何序列进行反向排序，reverse()只能对列表进行反向排序
s = [1, 2, 5, 8, 0]
print(reversed(s)) # <list_reverseiterator object at 0x000001F9B1914370>
print(reversed("FishC")) # <reversed object at 0x000001B590DF4790>

print(list(reversed(s))) # [0, 8, 5, 2, 1]

s.reverse()
print(s) # [0, 8, 5, 2, 1]

print(list(reversed("FishC"))) # ['C', 'h', 's', 'i', 'F']
print(list(reversed((1, 2, 5, 9, 3)))) # [3, 9, 5, 2, 1]
print(list(reversed(range(10)))) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 练习题：
print(sorted(["PPAP", "ppap", "Ppap", "PPaP" ]))

print(max("FishC") and min("FishC"))

print(list(reversed(sorted("FishC520"))))


# 动动手0：给定一个整数列表，请编程来调整该列表中整数的顺序，使得所有奇数排好序后放在数组的前半部分，所有偶数排好序后放在数组的后半部分。
# 比如给定的整数列表是 [1, 8, 7, 3, 6, 5, 4, 2]，那么调整后的结果应该是 [1, 3, 5, 7, 2, 4, 6, 8]。

s = [1, 8, 7, 3, 6, 5, 4, 2]
odd = []
even = []

for ch in s:
    if ch % 2 == 0:
        even.append(ch)
    else:
        odd.append(ch)

print(sorted(odd) + sorted(even))

# 动动手1：用户输入一个英文句子，请编程翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串是 "I love FishC."，则输出 "FishC. love I"。
# 注意1：用户输入的字符串可能会在前面或者后面包含任意数量的空格，但是反转后的结果将会去除这些空格（例如输入字符串是 "   I love FishC.   "，结果依然输出 "FishC. love I"）。
# 注意2：用户输入的字符串中，单词之间可能不止一个空格，但是反转后的结果将统一使用一个空格作为单词之间的间隔（例如输入字符串是 "I   love        FishC."，结果依然输出 "FishC. love I"）

dds1_input = input("请输入一个英文句子：")

s = dds1_input.split()
s.reverse()

print(" ".join(s))








