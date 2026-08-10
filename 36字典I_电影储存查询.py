"""字典：Python中唯一实现映射关系的内置类型"""
# 映射：键值对，键是唯一的，值可以不唯一

# 列表模仿字典
c_table = [
    "apple", "苹果",
    "banana", "香蕉",
    "cherry", "樱桃"]

code = ["apple"]

result = [c_table[c_table.index(each) + 1] for each in code]
print(result)

# 动动手0：请改进课堂中的代码，实现双重加密（先执行凯撒加密，再执行莫斯加密）
# 举个例子，比如明文 I love FishC，执行凯撒加密（正向位移 6 位）后的结果是 O rubk LoynI，接着再执行莫斯加密，结果就是 --- .-. ..- -... -.- .-.. --- -.-- -. ..

##########################################
# 请输入明文：I love FishC
# 请输入移动的位数：6
# 凯撒加密后的密文是： O rubk LoynI 
# 凯撒、摩斯混合加密后的密文是： --- .-. ..- -... -.- .-.. ----.-- -. ..

# dds0_word = input("请输入明文：")
# dds0_offset = int(input("请输入移动的位数："))
# result = []

# dds0_list = [x for x in dds0_word.split(" ")]

# for each in dds0_list:
#     for i in each:
#         if i.isalpha():
#             if i.isupper():
#                 result.append(chr((ord(i) - ord('A') + dds0_offset) % 26 + ord('A')))
#             else:
#                 result.append(chr((ord(i) - ord('a') + dds0_offset) % 26 + ord('a')))
#     result.append(" ") # 每个单词之间添加一个空格

# # 下面进行摩斯加密
# # 摩斯密文表
# c_table = [".-", "-...", "-.-.", "-..", ".", "..-.",
#            "--.", "....", "..", ".---", "-.-", ".-..",
#            "--", "-.", "---", ".--.", "--.-", ".-.",
#            "...", "-", "..-", "...-", ".--", "-..-",
#            "-.--", "--..", ".----", "..---", "...--", "....-",
#            ".....", "-....", "--...", "---..", "----.", "-----"]

# # 摩斯明文表
# d_table = ["A", "B", "C", "D", "E", "F",
#            "G", "H", "I", "J", "K", "L",
#            "M", "N", "O", "P", "Q", "R",
#            "S", "T", "U", "V", "W", "X",
#            "Y", "Z", "1", "2", "3", "4",
#            "5", "6", "7", "8", "9", "0"]

# kaisa_result = print("凯撒加密后的密文是：", "".join(result))
# morse_result = [c_table[d_table.index(each.upper())] for each in result if each != " "]
# print("凯撒、摩斯混合加密后的密文是：", " ".join(morse_result))

# 动动手1：请使用学过的知识，编写一个存储电影数据的小程序。
# 需要存放的数据如下：
# 电影名称
# 上映时间
# 导演（可能有多人）
# 主演（通常有多人）
# 电影评分

###################################
# 请输入想要的功能(1/2/3)：2
# 请输入想要查询的电影名称：无间道
# 电影名称： 无间道
# 上映时间： 1
# 导演： 1
# 主演： 1
# 电影评分： 1

movies = []
dates = []
directors = []
actors = []
scores = []

print("欢迎进入鱼C影评小程序")
print("1.数据录入")
print("2.查询数据")
print("3.退出程序")

while True:
    op = int(input("\n请输入想要的功能(1/2/3)："))

    if op == 1:
        go = True
        while go:
            movies.append(input("请输入电影名称："))
            dates.append(input("请输入上映日期："))
            directors.append([i.strip() for i in input("请输入导演名字（多人请用 / 分隔）：").split('/')])
            actors.append([i.strip() for i in input("请输入演员名字（多人请用 / 分隔）：").split('/')])
            scores.append(input("请输入电影评分："))
            print("电影数据录入成功")
            go = input("是否继续录入？(Y/N)：").upper() == "Y"
        # go 变成 False 后跳出内层 while，回到外层 while，重新问 op

    elif op == 2:
        name = input("请输入想要查询的电影名称：")
        for i, each in enumerate(movies):
            if each == name:
                # i 是下标；要用 movies[i]、dates[i] 取内容
                # 不要写 dates.index(name)：dates 里存的是日期，没有电影名
                print("电影名称：", movies[i])
                print("上映时间：", dates[i])
                print("导演：", directors[i])
                print("主演：", actors[i])
                print("电影评分：", scores[i])
                break
        else:
            print("电影不存在")

    elif op == 3:
        print("退出程序")
        break  # 跳出外层 while，结束程序


# 答案：
# movies = []
# dates = []
# directors = []
# actors = []
# scores = []
    
# print("欢迎进入鱼C影评小程序")
# print("1.数据录入")
# print("2.查询数据")
# print("3.退出程序")
# op = int(input("请输入想要的功能(1/2/3)："))
    
# while op != 3:
#     if op == 1:
#         go = True
#         while go:
#             movies.append(input("请输入电影名称："))
#             dates.append(input("请输入上映日期："))
#             directors.append([i.strip() for i in input("请输入导演名字（多人请用 / 分隔）：").split('/')])
#             actors.append([i.strip() for i in input("请输入演员名字（多人请用 / 分隔）：").split('/')])
#             scores.append(input("请输入电影评分："))
    
#             if 'N' == input("请问是否继续录入(Y/N):"):
#                 go = False
    
#     if op == 2:
#         name = input("请输入电影名称：")
#         for each in movies:
#             if each.find(name) != -1:
#                 print(f"电影名称：{each}")
#                 print(f"上映日期：{dates[movies.index(each)]}")
#                 print(f"导演名单：{directors[movies.index(each)]}")
#                 print(f"演员名单：{actors[movies.index(each)]}")
#                 print(f"当前评分：{scores[movies.index(each)]}")
#                 break
#         else:
#             print("查无此片！")
    
#     op = int(input("\n请输入想要的功能(1/2/3)："))
