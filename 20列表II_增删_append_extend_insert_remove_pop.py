"""列表的增"""
heros = ["钢铁侠", "绿巨人"]
heros.append("黑寡妇")
# append每次只能添加一个元素
print(heros)

heros.extend(["鹰眼", "灭霸", "雷神"])
# extend每次可以添加多个元素，加在列表的后面
print(heros)

# 切片插入
s = [1, 2, 3, 4, 5]
s[len(s):] = [6]
# 相当于s.append(6)
print(s) # [1, 2, 3, 4, 5, 6]
s[len(s):] = [7, 8, 9]
print(s) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

s = [1, 3, 4, 5]
s.insert(1, 2) # 在索引1的位置插入2
print(s)
s.insert(len(s), 6) # 在末尾插入6

"""列表的删"""
# 如果列表中存在多个相同的元素，remove只会删除第一个
# remove需要指定要删除的元素的值，如果元素不存在，会报错
heros.remove("灭霸")
print(heros)

# heros.remove("金莲") # 报错
# print(heros)

heros.pop(2) # 删除索引为2的元素
heros.pop() # 删除最后一个元素
print(heros)

heros.clear() # 清空列表
print(heros)

s = [1, 2, 3, 4, 5]
s.extend(["FishC"])
print(s)

s = [1, 2, 3, 4, 5]
s[len(s)-2:] = [2, 1]
print(s)

# 练习题：请编写一个程序，判断给定的字符串 s 中括号的写法是否合法。
s = input("请输入测试字符串：")

# 创建一个特殊列表
stack = []

for c in s:
    if c == '(' or c == '[' or c == '{':
        # 那么添加到特殊列表中 #
        stack.append(c)
    else:
        if len(stack) == 0:
            print("非法T_T")
            break

        if c == ')':
            d = '('
        elif c == ']':
            d = '['
        elif c == '}':
            d = '{'

        if d != stack.pop(): # 如果d不等于从特殊列表尾部弹出的元素，则非法
            print("非法T_T")
            break # 如果非法，则跳出循环,不执行else
else: # 如果整段扫描都没出错（没 break），最后再做收尾检查。
    if len(stack) == 0:
        print("合法O_O")
    else:
        print("非法T_T")


