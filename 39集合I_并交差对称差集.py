"""集合的定义"""
# 集合中的元素都是独一无二的，无序的，不可索引

print(type({})) # <class 'dict'>
print(type({"one"})) # <class 'set'>
print(type({"one":1})) # <class 'dict'>

print({"FishC", "Python"}) # {'FishC', 'Python'}

# 随机性
print({s for s in "FishC"}) # {'F', 'C', 'i', 's', 'h'}
# 每一次运行的结果可能不同
print(set("FishC")) # {'h', 's', 'i', 'F', 'C'}

# 集合不可索引
s = set("FishC")
# print(s[0]) # 报错

print('C' in s) # True
print('c' in s) # False

for each in s:
    print(each)

print(set([1, 1, 2, 3, 5])) # {1, 2, 3, 5}

# 通过集合set()函数，可以去除列表中的重复元素
s = [1, 1, 2, 3, 5]
print(len(s) == len(set(s))) # False

t = s.copy()
print(t) # [1, 1, 2, 3, 5]
s = set("FishC")
print(s) # {'C', 'F', 'h', 'i', 's'}

# 判断两个集合是否没有交集
# 说明两个集合有交集
print(s.isdisjoint(set("Python"))) # False

print(s.issubset(set("JAVA"))) # True

# 不加set()函数，则判断的是字符串是否与集合有交集
print(s.isdisjoint("JAVA")) # True

# 检测集合是否为另一个集合的子集
print(s) # {'C', 'F', 'h', 'i', 's'}
print(s.issubset(set("FishC.com.cn"))) # True

# 检测集合是否为另一个集合的超集
print(s.issuperset(set("Fish"))) # True

# 计算当前对象和其他集共同构建的并集，交集，差集，对称差集

# 并集，两个集合中所有的元素
print(s.union({1, 2, 3})) # {'F', 'h', 1, 'i', 2, 3, 'C', 's'}
print(s.union({1, 2, 3}, "Python")) # {1, 2, 'F', 3, 'h', 'o', 'P', 'n', 'y', 't', 'C', 's', 'i'}

# 交集，两个集合中共同的元素
print(s.intersection("Fish")) # {'h', 's', 'F', 'i'}
print(s.intersection("Php", "Python")) # {'h'}

# 差集，当前集合中不在另一个集合中的元素（排除掉s）
print(s.difference("Php", "Python")) # {'s', 'C', 'i', 'F'}

# 对称差集，两个集合中不在另一个集合中的元素
print(s.symmetric_difference("Python")) # {'o', 'F', 't', 'i', 'n', 's', 'P', 'y', 'C'}

# 用运算符实现集合的并集，交集，差集，对称差集
# 判断集合是否为另一个集合的子集
print(s <= set("FishC")) # True
print(s < set("FishC")) # False
print(s < set("FishC.com.cn")) # True

# 判断集合是否为另一个集合的超集
print(s >= set("FishC")) # True

# 并集
print(s | {1, 2, 3} | set("Python")) # {'C', 'F', 'h', 'i', 's', 'o', 1, 2, 3, 'P', 'n', 'y', 't'}

# 交集
print(s & set("Php") & set("Python")) # {'h'}

# 差集
print(s - set("Php") - set("Python")) # {'s', 'C', 'i', 'F'}

# 对称差集
print(s ^ set("Python")) # {'o', 'F', 't', 'i', 'n', 's', 'P', 'y', 'C'}

# 运算符只能作用于集合，不能作用于字符串
# print(s <= "FishC") # 报错


# 练习题：
print({})

print(len({s for s in "fishc.com.cn"})) # 10

s1 = set("fishc.com.cn")
s2 = set("ilovefishc.com")
print(s1 - s2) # {'n'}

# 动动手0：想办法优化源代码，使得程序的执行效率提高 10000 倍以上。

################################################
# 一共找到642个匹配。
# 查找过程一共消耗33.02590189999955秒。
# 一共找到642个匹配。
# 查找过程一共消耗0.0006186000000525382秒。
# print(33.02590189999955/0.0006186000000525382) # 53388.1375641685

# 为什么列表变成集合之后，效率竟然提高了这么多呢？
# 因为集合的背后是有散列表的支持，而列表则没有！
# 所以，列表的每次查找都需要从头到尾地扫描，而集合则只需要简单地查表操作。
# 打个比方，这就好比你在新华字典里面查找一个 “龟” 字，in 在列表上的查找方法是从头翻到尾，挨个对比是不是 “龟” 字；而 in 在集合上的查找方式是通过笔画的索引，直接就拿到了这个 “龟” 字所在的页码。


import random
import timeit

haystack = [random.randint(1, 10000000) for i in range(10000000)]
needles = [random.randint(1, 1000) for i in range(1000)]

# 请在此处添加一行代码，使得查找过程的执行效率提高 10000 倍以上。
haystack = set(haystack)  # 列表 in 是 O(n)，集合 in 是 O(1)

def find():
    found = 0
    for each in needles:
        if each in haystack:
            found += 1

    print(f"一共找到{found}个匹配。")

t = timeit.timeit("find()", setup="from __main__ import find", number=1)
print(f"查找过程一共消耗{t}秒。")
















































































