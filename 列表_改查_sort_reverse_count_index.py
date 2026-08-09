"""列表的替换"""
heros = ['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[4] = "钢铁侠"
print(heros) # ['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '钢铁侠', '雷神']

# 切片替换
heros[3:] = ["武松", "林冲", "李逵"] 
# 把索引3及之后的元素替换为["武松", "林冲", "李逵"]
print(heros) # ['蜘蛛侠', '绿巨人', '黑寡妇', '武松', '林冲', '李逵']

"""列表的排序"""
nums = [3, 1, 9, 6, 8, 3, 5, 3]
nums.sort()
print(nums) # [1, 3, 3, 3, 5, 6, 8, 9]
nums.reverse()
print(nums) # [9, 8, 6, 5, 3, 3, 3, 1]

# 反转列表
heros.reverse() 
print(heros) # ['李逵', '林冲', '武松', '鹰眼', '黑寡妇', '绿巨人', '蜘蛛侠']

nums = [3, 1, 9, 6, 8, 3, 5, 3]
# 降序排序
nums.sort(reverse=True) 
print(nums) # [9, 8, 6, 5, 3, 3, 3, 1]

"""列表的查找"""
nums.count(3) # 统计3出现的次数
print(nums) # 3

heros.index("绿巨人") # 查找绿巨人的索引
print(heros.index("绿巨人")) # 4

# 不知道索引，可以先查找索引，再替换
heros[heros.index("绿巨人")] = "神奇女侠"
print(heros) # ['蜘蛛侠', '神奇女侠', '黑寡妇', '鹰眼', '钢铁侠', '雷神']

nums = [3, 1, 9, 6, 8, 3, 5, 3]
print(nums.index(3, 1, 7)) # 在索引1到7之间查找值3的索引

"""列表的复制"""
nums_copy1 = nums.copy()
print(nums_copy1) # [3, 1, 9, 6, 8, 3, 5, 3]

nums_copy2 = nums[:]
print(nums_copy2) # [3, 1, 9, 6, 8, 3, 5, 3]

# 练习题：
heros = ['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[2] = '神奇女侠'
# heros[heros.index("黑寡妇")] = "神奇女侠"
print(heros) # ['蜘蛛侠', '绿巨人', '神奇女侠', '鹰眼', '灭霸', '雷神']

heros = ['蜘蛛侠', '绿巨人', '神奇女侠', '鹰眼', '灭霸', '雷神']
heros[0:2] = ["猪猪侠", "女巨人"]
print(heros) # ['猪猪侠', '女巨人', '神奇女侠', '鹰眼', '灭霸', '雷神']

s = [1, 2, 3, 4, 5]
s[:] = "FishC" 
# 先删除再替换，不过这回我们删除的是整个列表，然后再将赋值号（=）右边的可迭代对象（字符串）的每个元素插入到列表里面。
print(s) 

s = [1, 2, 3, 4, 5]
t = s
s[2] = 1
print(t) # [1, 2, 1, 4, 5]

# 练习题: 列表的 index() 方法可以找到第一个匹配元素的下标，那么你有没有办法在不改变原列表的情况下，找到最后一个匹配元素的下标呢？
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 5, 6, 3, 2, 1, 2]
nums_copy = nums.copy()
nums_copy.reverse()
print(len(nums_copy) - 1 - nums_copy.index(1)) # 15

x = 1
count = nums.count(x)
length = len(nums)
for each in range(length):
    if nums[each] == x:
        count -= 1
    if count == 0: # 如果count为0，则打印each
        print(each)
        break

# 练习题：0. 如果有一个列表，其中占比超过一半的元素称之为主要元素，那么如何获取一个列表的主要元素呢？
# 根据主要元素的定义，对列表进行排序操作之后，主要元素必然会出现在列表长度一半之后的一个位置上。
# 1. 摩尔投票法有时候也被称为“多数投票法”，该算法解决的问题是如何在任意多的候选人中（选票无序），找到获得票数最多的那个。
# 摩尔投票法分为两个阶段：
#   1. 对抗阶段：分属两个候选人的票数进行两两对抗抵消
#   2. 计数阶段：计算对抗结果中最后留下的候选人票数是否有效

# 0. 暴力法
nums = [2, 2, 4, 2, 3, 6, 2]
for each in nums:
    if nums.count(each) > len(nums) / 2:
        print(each)
        break

# 1. 摩尔投票法
nums = [2, 2, 4, 2, 3, 6, 2]
    
# 对抗阶段
major = nums[0]
count = 0
for each in nums:
    if count == 0:
        major = each
    if each == major:
        count += 1
    else:
        count -= 1
    
# 统计阶段
if nums.count(major) > len(nums) / 2:
    print("主要元素是：", major)
else:
    print("不存在主要元素。")