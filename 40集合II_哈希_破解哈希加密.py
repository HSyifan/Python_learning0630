"""可变集合和不可变集合"""

t = frozenset("FishC")
print(t) # frozenset({'C', 'F', 'h', 'i', 's'})

s = set("FishC")
print(s) # {'C', 'F', 'h', 'i', 's'}

# union_update, 交集
s.update([1, 1], "23")
print(s) # {1, '2', '3', 'C', 'F', 'h', 'i', 's'}

# t.update([1, 1], "23")
# print(t) #  报错 'frozenset' object has no attribute 'update'

# intersection_update, 交集
s.intersection_update("FishC")
print(s) # {'C', 'F', 'h', 'i', 's'}

# difference_update, 差集
s.difference_update("Php", "Python")
print(s) # {'i', 'F', 's', 'C'}

# symmetric_difference_update, 对称差集
s.symmetric_difference_update("Python")
print(s) # {'C', 'i', 'o', 't', 'h', 'y', 'n', 'P', 's', 'F'}


"""删除元素"""
# s.remove("瓦迈") # 报错，因为"瓦迈"不在集合中

# 静默处理，不报错
s.discard("瓦迈") # 不报错，因为"瓦迈"不在集合中

# 随机删除一个元素
s.pop() 
print(s) # {'C', 'i', 'o', 't', 'h', 'y', 'n', 'P', 's', 'F'}

# 清空集合
s.clear()
print(s) # set()

"""可哈西：哈希值在其整个生命周期内保持不变"""
print(hash(1)) # 1
print(hash(1.0)) # 1
print(hash(1.001)) # 2305843009213441

# 不可变对象，可哈西
print(hash("FishC")) # 5781661258072144159
print(hash((1, 2, 3))) # 529344067295497451
print(hash(frozenset({1, 2, 3}))) # -272375401224217160

# 可变对象，不可哈西
# print(hash([1, 2, 3])) # 报错，因为列表[1, 2, 3]是可变对象
# print(hash({1, 2, 3})) # 报错，因为集合{1, 2, 3}是可变对象

# 只有可哈西的，才能作为字典的键和集合的元素
print({"Python": 520, "FishC": 1314}) 

# print({[1, 2, 3]: "FishC"}) # 报错，因为[1, 2, 3]是可变对象

# 集合中只能是不可变对象
x = {1, 2, 3}
# y = {x, 4, 5} # 报错，因为x是可变对象

# 用frozenset创建不可变集合
x = frozenset({1, 2, 3})
y = {x, 4, 5} # 不报错，因为x是不可变对象
print(y) # {frozenset({1, 2, 3}), 4, 5}


# 练习题：
s1 = set([1, 1, 2, 3, 5])
s2 = frozenset([1, 1, 2, 3, 5])
print(s1 == s2) # True

print({x for x in 'FishCChsiF' if x not in 'ish'})


# 动动手0：最开始的时候，Python 是没有 set() 的，那么当时伟大的程序猿是如何实现 “集合” 这个的概念呢？
# 大家没有 set() 可用了，只能利用 dict() 来实现交集和并集
#　生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
# 生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
# 利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）

import random
x = [random.randint(1, 100) for _ in range(100)]
y = [random.randint(50, 150) for _ in range(100)]
# print(x)
# print(y)

z = dict.fromkeys(z for z in x if z in y)
print(len(z.keys()))
print(z.keys())

# 动动手1：破解 MD5 哈希加密！！
# 我们提到过通常服务器是不会保存用户的明文密码的（那样就太不安全了），取而代之的是存储单向哈希加密后的密文。
# 虽然说单向哈希加密是无法逆向，但聪明的黑客们想出了彩虹表破解法：
# 彩虹表是一个用于加密散列函数逆运算的预先计算好的表，常用于破解加密过的密码散列。彩虹表常常用于破解长度固定且包含的字符范围固定的密码（如信用卡、数字等）。这是以空间换时间的典型实践，比暴力破解（Brute-force attack）使用的时间更少，空间更多；但与储存密码空间中的每一个密码及其对应的哈希值（Hash）实现的查找表相比，其花费的时间更多，空间更少。
# 密码及其对应的哈希值（Hash）实现的查找表相比，其花费的时间更多，空间更少。
# 说人话就是：所谓的彩虹表，其实就是将所有可能的字符串组合都给预先哈希一遍，然后将映射结果保存起来，当黑客拿到一个哈希值时，通过查表的方式获取密码明文。

# 题目要求：生成 0~999999 所有整数组成密码的哈希值
# 将上面生成的哈希值保存为映射类型
# 通过查表的方式，计算下面 3 个哈希值对应的明文密码
# 021bbc7ee20b71134d53e20206bd6feb
# e10adc3949ba59abbe56e057f20f883e
# 655d03ed12927aada3d5bd1f90f06eb7
# hashlib.md5() 的参数是需要一个 b 字符串（即 bytes 类型的对象），这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"

import hashlib

hash_dict = {}
for i in range(1000000):  # 生成 0~999999 所有整数组成密码的哈希值
    bstr = bytes(str(i), "utf-8") # 将整数转换为字符串，并转换为bytes类型
    hash_passwd = hashlib.md5(bstr).hexdigest() # 计算哈希值
    hash_dict[hash_passwd] = i # 将哈希值和整数保存到字典中

print(hash_dict["021bbc7ee20b71134d53e20206bd6feb"]) # 1024
print(hash_dict["e10adc3949ba59abbe56e057f20f883e"]) # 123456
print(hash_dict["655d03ed12927aada3d5bd1f90f06eb7"]) # 960520











































