
x = {"吕布", "关羽"} # 集合，不是字典
print(type(x)) # <class 'set'>

y = {"吕布": "口口布", "关羽": "关习习"}
print(type(y)) # <class 'dict'>

print(y["吕布"]) # 口口布

y["刘备"] = "刘Baby"
print(y) # {'吕布': '口口布', '关羽': '关习习', '刘备': '刘Baby'}

"""字典的创建"""

# 直接创建
a = {"吕布": "口口布", "关羽": "关习习"}

# 使用 dict 函数创建，键上面不能加引号
b = dict(吕布="口口布", 关羽="关习习", 刘备="刘Baby")

# 使用列表创建，列表中的元素必须是元组
c = dict([("吕布", "口口布"), ("关羽", "关习习"), ("刘备", "刘Baby")])

# 使用字典创建（无病呻吟版本）
d = dict({"吕布": "口口布", "关羽": "关习习", "刘备": "刘Baby"})

# 混合方法创建
e = dict({"吕布": "口口布", "关羽": "关习习"}, 刘备="刘Baby")

# zip 函数创建，创建一个聚合可迭代对象的迭代器，可以作为参数传入 dict 函数
f = dict(zip(["吕布", "关羽", "刘备"], ["口口布", "关习习", "刘Baby"]))

print(a == b == c == d == e == f) # True

"""字典的增删改查"""

# 增
# fromkeys() 方法创建字典，对于初始化字典很有用
d = dict.fromkeys("Fish", 250)
print(d) # {'F': 250, 'i': 250, 's': 250, 'h': 250}

d["F"] = 70
print(d) # {'F': 70, 'i': 250, 's': 250, 'h': 250}

d["C"] = 67
print(d) # {'F': 70, 'i': 250, 's': 250, 'h': 250, 'C': 67}

# 删
d.pop("s")
print(d) # {'F': 70, 'i': 250, 'h': 250, 'C': 67}

# d.pop("狗") # 报错

d.pop("狗", "没有") # 没有

# popitem() 3.7版本之后新增的方法，删除字典中的最后一对键值对
print(d.popitem()) # ('C', 67)
print(d) # {'F': 70, 'i': 250, 'h': 250}

del d["i"]
print(d) # {'F': 70, 'h': 250}

# del d # 删除字典
# print(d) # 报错

d = dict.fromkeys("FishC", 250)

d.clear()
print(d) # {}


# 练习题：
d = {}.fromkeys("吕布", 999)
print(d) # 

a = {"小甲鱼":"You are my super star."}
b = a
a.clear()
print(b) # {}

# 动动手0：请利用字典类型，改进上一节课后作业的电影查询小程序。
# 上一节用 5 个平行列表靠下标对齐；这里改成：电影名作键，详情用内层字典作值。

# movies = {
#     "无间道": {
#         "date": "2002",
#         "directors": ["刘伟强", "麦兆辉"],
#         "actors": ["刘德华", "梁朝伟"],
#         "score": "9.2",
#     }
# }


# movies = {}  # {"无间道": {"date": ..., "directors": [...], "actors": [...], "score": ...}, ...}

# print("欢迎进入鱼C影评小程序")
# print("1.数据录入")
# print("2.查询数据")
# print("3.退出程序")

# while True:
#     op = int(input("\n请输入想要的功能(1/2/3)："))

#     if op == 1:
#         go = True
#         while go:
#             name = input("请输入电影名称：")
#             movies[name] = {
#                 "date": input("请输入上映日期："),
#                 "directors": [i.strip() for i in input("请输入导演名字（多人请用 / 分隔）：").split('/')],
#                 "actors": [i.strip() for i in input("请输入演员名字（多人请用 / 分隔）：").split('/')],
#                 "score": input("请输入电影评分："),
#             }
#             print("电影数据录入成功")
#             go = input("是否继续录入？(Y/N)：").upper() == "Y"

#     elif op == 2:
#         name = input("请输入想要查询的电影名称：")
#         if name in movies:  # 直接按键查找，不用再 for + 下标对齐
#             info = movies[name]
#             print("电影名称：", name)
#             print("上映时间：", info["date"])
#             print("导演：", info["directors"])
#             print("主演：", info["actors"])
#             print("电影评分：", info["score"])
#         else:
#             print("电影不存在")

#     elif op == 3:
#         print("退出程序")
#         break


# 动动手1：请编写一个电话簿程序。

print("欢迎进入鱼C电话簿")

phonebook = {}
while True:
    op = input("请输入命令（I：录入 / C：查询 / D：删除 / P：打印 / E：退出）：")

    if op == "I":
        go = True
        while go:
            name = input("请输入姓名：")
            if name in phonebook:  # 姓名已存在：打印原号码
                print("该姓名已录入，手机号码是：", phonebook[name])
                if input("请问是否修改（Y/N）：").upper() == "N":
                    go = input("是否继续录入(Y/N)：").upper() == "Y"
                    continue  # 不修改：回到 while go，问下一个姓名（或结束录入）

            # 号码不合法时只在这里循环重输，不要 continue 外层（否则会重新问姓名）
            phone = input("请输入手机号码：")
            while not (phone.isdigit() and len(phone) == 11):
                phone = input("输入不合法，请重新输入：")
            phonebook[name] = phone
            print("电话簿更新成功")
            go = input("是否继续录入(Y/N)：").upper() == "Y"

    elif op == "C":
        print("-- 查询模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phonebook:
                print(phonebook[name])
            else:
                print("电话簿中没有该姓名")
            if input("是否继续查询(Y/N)：") != 'Y':
                break

    elif op == "D":
        print("-- 删除模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phonebook:
                if input("是否确认删除（Y/N）：").upper() == "Y":
                    del phonebook[name]
                    print("电话簿更新成功")
                    continue
                else:
                    break
            else:
                print("电话簿中没有该姓名")
                continue

    elif op == "P":
        print("-- 打印模式 --")
        print(phonebook)
    
    elif op == "E":
        print("退出程序")
        break