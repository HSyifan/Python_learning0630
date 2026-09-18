"""字典的改写"""
d = dict.fromkeys("FishC")

d['s'] = 115
print(d) #　{'F': None, 'i': None, 's': 115, 'h': None, 'C': None}

# 字典的 update() 方法
# 也可以直接给它传入一个字典
d.update({'i':105, 'h':104})
print(d) # {'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None}

# 也可以直接给它传入多个键值对
d.update(F = '70', C = '67')
print(d) # {'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}

# 也可以直接给它传入一个包含键值对的可迭代对象
d.update([('F',70), ('i',105), ('s',115), ('h',104), ('C',67)])
print(d) # {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

"""字典的查找"""
print(d['C']) # 67
# print(d['c']) # 报错

# 字典自带 .get(key, 默认值) 这个方法
# self.click_dict[short_url] = self.click_dict.get(short_url, 0) + 1
# 键存在就返回原来的次数，不存在就返回第二个参数 0
# get(), 如果key不存在，可返回自定义文本
print(d.get('c', "这里没有c")) # 这里没有c

# setdefault(), 如果key不存在，则添加key，并返回value
d.setdefault('C', "code")
d.setdefault('c', "code")
print(d) # {'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67', 'c': 'code'}

# keys(), values(), items(), 分别返回字典的key, value, key-value对的视图对象
keys = d.keys()
values = d.values()
items = d.items()

print(keys) # dict_keys(['F', 'i', 's', 'h', 'C', 'c'])
print(values) # dict_values(['70', 105, 115, 104, '67', 'code'])
print(items) # dict_items([('F', '70'), ('i', 105), ('s', 115), ('h', 104), ('C', '67'), ('c', 'code')])

d.pop('c')
print(d) # {'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}

print(keys) # dict_keys(['F', 'i', 's', 'h', 'C'])
print(values) # dict_values(['70', 105, 115, 104, '67'])
print(items) # dict_items([('F', '70'), ('i', 105), ('s', 115), ('h', 104), ('C', '67')])

"""字典的浅拷贝与深拷贝"""
e = d.copy()
print(e) # {'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}

print(len(e)) # 5

print('C' in d) # True
print('c' not in d) # True

print(list(d)) # ['F', 'i', 's', 'h', 'C']
print(list(d.values())) # ['70', 105, 115, 104, '67']

e = iter(d)
print(next(e)) # F
print(next(e)) # i
print(next(e)) # s
print(next(e)) # h
print(next(e)) # C
# print(next(e)) # 报错StopIteration

print(list(reversed(d.values()))) #　['67', 104, 115, 105, '70']

"""字典的嵌套"""
d = {"吕布": {"语文": 60, "数学": 70, "英语": 80}, "关羽": {"语文": 80, "数学": 90, "英语": 70}}
print(d["吕布"]["数学"]) # 70

d = {"吕布": [60, 70, 80], "关羽": [80, 90, 70]}
print(d["吕布"][1]) # 70


"""字典推导式"""
d = {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

b = {v:k for k, v in d.items()}
print(b) # {70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'C'}

c = {v:k for k, v in d.items() if v > 100}
print(c) # {115: 's', 104: 'h'}

d = {x:ord(x) for x in 'FishC'}
print(d) # {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

d = {x:y for x in [1, 3, 5] for y in [2, 4, 6]}
# 双重循环会反复给同一个键赋值，后面的会覆盖前面的
# 如果需要保留所有值，可以使用defaultdict
print(d) # {1: 6, 3: 6, 5: 6}


# 练习题：
d = dict.fromkeys("FishC")
d.update([('F',70), ('i',105), ('s',115), ('h',104), ('C',67)])
print(d) # {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

d = {"小甲鱼":"千年王八，万年龟。"}
e = d.copy()
d["小甲鱼"] = "666"
print(d) # {"小甲鱼":"666"}
print(e) # {"小甲鱼":"千年王八，万年龟。"}

d = {"小甲鱼":{"数学":99, "英语":88, "语文":101}}
e = d.copy()
d["小甲鱼"]["语文"] = 100
print(d) # {'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}}
print(e) # {'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}}

d = {}
d[1] = "千年王八"
d[1.0] = "万年龟"
print(d) # {1: '万年龟'}

# 动动手0：请按照要求编写一个网站的注册模块
# 用户名不允许重复
# 数据库需要保存用户名及密码
# 初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）

#######################
# 请输入用户名：小甲鱼
# 该用户名已被注册！
# 请重新输入用户名：鱼小二
# 请输入密码：222
# ----------
# 目前已注册的用户有：
# 小甲鱼
# 不二如是
# 鱼小二

database = {"小甲鱼":"I_love_FishC", "不二如是":"FishC5201314"}
name = input("请输入用户名：")

while name in database: # 用户名已存在就一直让用户重新输入，直到可用
    print("该用户名已被注册！")
    name = input("请重新输入用户名：")

password = input("请输入密码：")
database[name] = password
print("-" * 10)
print("目前已注册的用户有：")
for user in database:
    print(user)


# 动动手1：提升网站的安全性
# 使用 Python 将明文通过 MD5 加密算法生成密文

############################################
# 请输入用户名：鱼小二
# 请输入密码：123456
# ----------
# 目前已注册的用户有：
# 小甲鱼：063ab7775a97695bef7cad24835fae0d
# 不二如是：7f9b6131340da948d7863ae00cad8e91
# 鱼小二：e10adc3949ba59abbe56e057f20f883e

import hashlib
# result = hashlib.md5(b"FishC")
# print(result.hexdigest())
# 9d22182e926ca703cd0f5926e7d57782
# 注意：上面是 "FishC" 的 MD5；b"xxx" 表示字节串，普通字符串要用 .encode()

database = {
    "小甲鱼": {
        "password": "I_love_FishC",
        "md5_password": hashlib.md5("I_love_FishC".encode()).hexdigest()
    },
    "不二如是": {
        "password": "FishC5201314",
        "md5_password": hashlib.md5("FishC5201314".encode()).hexdigest()
    }
}

name = input("请输入用户名：")

while name in database:
    print("该用户名已被注册！")
    name = input("请重新输入用户名：")

password = input("请输入密码：")
database[name] = {
    "password": password,
    # 必须加密“用户输入的密码”，不能写 b"password"（那是字面量 password）
    "md5_password": hashlib.md5(password.encode()).hexdigest()
}
print("-" * 10)
print("目前已注册的用户有：")
for user in database:
    print(user + "：" + database[user]["md5_password"])


# 答案：
# import hashlib
    
# fc_db = {"小甲鱼":hashlib.md5(b"I_love_FishC"), "不二如是":hashlib.md5(b"FishC5201314")}
    
# name = input("请输入用户名：")
# while True:
#     if fc_db.get(name) != None:
#         print("该用户名已被注册！")
#         name = input("请重新输入用户名：")
#     else:
#         break
    
# passwd = input("请输入密码：")
# bstr = bytes(passwd, "utf-8")
# passwd = hashlib.md5(bstr)
# fc_db[name] = passwd
    
# print("------------------")
# print("目前已注册的用户有：")
# for each in fc_db.items():
#     print(each[0], each[1].hexdigest(), sep="：")