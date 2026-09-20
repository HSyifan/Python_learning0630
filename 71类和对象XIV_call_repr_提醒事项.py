"""魔术方法：__call__、str/repr、__add__"""
"""这节课讲三件事：对象怎么当函数用、打印时显示什么、对象能不能用 +。"""

# ========== 1. __call__：让对象能被 obj() 这样调用 ==========
# 只要写了 __call__，实例就能像函数一样加括号
# c() 其实就是在调用 c.__call__()

class C:
    def __call__(self):
        print("嗨~")

c = C()
c() # 嗨~


# __call__ 也可以收参数，和普通函数一样（包括 *args / **kwargs）
class C:
    def __call__(self, *args, **kwargs):
        print(f"位置参数 -> {args}\n关键字参数 -> {kwargs}")

c = C()
c(1, 2, 3, x = 250, y = 520)
# 位置参数 -> (1, 2, 3)
# 关键字参数 -> {'x': 250, 'y': 520}


# ========== 2. 用类代替闭包：先记住配置，再反复调用 ==========
# __init__ 里存「固定设置」（这里是指数 exp）
# __call__ 里做「每次要用的计算」（这里是底数 base ** exp）
# 好处：配置和计算分开，square / cube 可以各做一个对象反复用

class Power:
    def __init__(self, exp):
        self.exp = exp          # 创建时记住：算几次方
    def __call__(self, base):
        return base ** self.exp # 调用时：传入底数，算出来

square = Power(2)   # 造一个「平方器」，记住 exp=2
print(square(5))    # 25  ← 等价于 5 ** 2
# cube = Power(3)   # 同理可以再做一个立方器：cube(5) → 125


# ========== 3. str 和 repr：两种「把对象变成字符串」的方式 ==========
# str(对象)  → 给人看的，友好一点（print 优先用这个）
# repr(对象) → 给开发者看的，尽量能看出「这是什么对象」
# 内置类型两者常常一样；自己的类默认只有难懂的 <C object at 0x...>

print(str(123))  # 123
print(repr(123)) # 123

# eval(字符串) 会把字符串当代码执行；repr 有时设计成 eval(repr(x)) 能还原
print(eval("1 + 2"))       # 3
print(eval(repr(123)))     # 123


# 只写 __repr__：str() 找不到 __str__ 时，会退回去用 __repr__
class C:
    def __repr__(self):
        return "I love FishC"

c = C()
print(repr(c)) # I love FishC
print(str(c))  # I love FishC  ← 没写 __str__，借用了 __repr__


# 只写 __str__：print / str() 好看了，但 repr() 仍是默认地址串
class C:
    def __str__(self):
        return "I love FishC"

c = C()
print(str(c))  # I love FishC
print(repr(c)) # <__main__.C object at 0x...>  ← 仍是默认样子


# 容器（列表）里打印元素时，用的是 repr，不是 str
# 所以只写 __str__ 时：一个个 print(each) 好看，print(整张列表) 仍是地址
cs = [C(), C(), C()]
for each in cs:
    print(each)  # 每个都是 I love FishC（走 __str__）

print(cs)  # 列表整体用 repr，所以还是一堆 <C object at ...>


# 写了 __repr__ 之后：列表里也能看到你想要的样子
class C:
    def __repr__(self):
        return "I love FishC"

cs = [C(), C(), C()]
for each in cs:
    print(each)
print(cs) # ['I love FishC', 'I love FishC', 'I love FishC']


# ========== 4. 同时写 str / repr，再加 __add__ 支持 + ==========
# 习惯：
#   __str__  → 给人看：data = 250
#   __repr__ → 像创建代码：C(250)，调试列表时更清楚
#   __add__  → 定义 c + 数字 时发生什么
#
# 注意：__add__ 最好 return 结果；不 return 的话，c + 520 的值是 None
# 下面写成 return self，这样 print(c + 520) 才能继续走 __str__/__repr__

class C:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f"data = {self.data}"   # 给人看
    def __repr__(self):
        return f"C({self.data})"       # 给调试 / 列表看
    def __add__(self, other):
        self.data += other
        return self                    # 把算完的自己交回去

c = C(250)
print(c)        # data = 250          ← print 优先用 __str__
print(c + 520)  # data = 770          ← 先 __add__，再 print 结果
# 若只看 repr：repr(c) → C(770)


# --- 这节课记什么 ---
# 1. 想 obj()          → 写 __call__
# 2. 想 print 好看     → 写 __str__；想列表/调试也好看 → 写 __repr__
# 3. 想 obj + 别的东西 → 写 __add__（记得 return）


# 练习题：
# 5. 定义一个 Inverse 类，该类的目的是根据给定的数值返回其倒数。

class Inverse:
    def __call__(self, input_data):
        if input_data == 0:
            return "参数不能为0！"
        return 1 / input_data
    
inverse = Inverse()
print(inverse(2)) # 0.5
print(inverse(3)) # 0.3333333333333333
print(inverse(5)) # 0.0002
print(inverse(0)) # 参数不能为0！

# 6. 定义一个 Greeting 类，根据提供的时间段来向不同的人发出不同的问候。
# *names 收人名；time_period 用普通默认参数（不要用 **）
# 若写成 **time_period：
#   g("小甲鱼") → time_period 是 {}，不是 None，第一个 if 进不去
#   time_period="morning" → 变成 {"time_period": "morning"}，也不会 == "morning"
class Greeting:
    def __call__(self, *names, time_period=None):
        for name in names:
            if time_period is None:
                print(f"您好，{name}！")
            elif time_period == "morning":
                print(f"早上好，{name}！")
            elif time_period == "afternoon":
                print(f"下午好，{name}！")
            elif time_period == "evening":
                print(f"晚上好，{name}！")

g = Greeting()
g("小甲鱼")
# 您好，小甲鱼！
g("小甲鱼", "小鱿鱼", "小鲨鱼", time_period="morning")
# 早上好，小甲鱼！
# 早上好，小鱿鱼！
# 早上好，小鲨鱼！


# 动动手：编写一个类似 iPhone 提醒事项的程序。
# 要求：编写一个类，模拟类似 iPhone 的提醒事项功能。
# 该程序功能由 Reminder 类实现，其应具备以下功能：
# 使用文件（如：reminders.pkl）来存储提醒事项
# - 添加提醒事项
# - 查看提醒事项列表
# - 删除提醒事项
# - 标记提醒事项为已完成
# - 搜索提醒事项


import pickle
import time
from pathlib import Path

class Reminder:
    def __init__(self, file_name):
        self.file_name = file_name
        self.reminders = []
    def __call__(self, *args, **kwargs):
        if args[0] == "添加":
            self.add_reminder(args[1], args[2], args[3], args[4])
    # 想对外支持 reminder[i] 这样取提醒事项时，才写 __getitem__
    # def __getitem__(self, index):
    #     return self.reminders[index]
    def add_reminder(self, title, category, color, priority):
        self.reminders.append({
            "title": title,
            "category": category,
            "color": color,
            "priority": priority,
            "completed": False,  # 新建默认未完成
        })
        print(f"已添加提醒事项：{title}，分类：{category}，优先级：{priority}")
    def delete_reminder(self, index):
        # 外面传的是列表序号（从 1 开始），下标要 -1
        i = index - 1
        title = self.reminders[i]["title"]
        del self.reminders[i]
        print(f"已删除提醒事项：{title}")
    def list_reminders(self):
        print("提醒事项：")
        # enumerate 同时拿到下标和内容；显示给用户时 +1（从 1 开始）
        for index, reminder in enumerate(self.reminders):
            status = "已完成" if reminder["completed"] else "未完成"
            print(
                f"{index + 1}. {reminder['title']}，"
                f"（{reminder['category']}，{reminder['color']}）（{status}），"
                f"优先级：{reminder['priority']}"
            )
    def complete_reminder(self, index):
        # 同样按「第几条」传参，内部 -1
        i = index - 1
        self.reminders[i]["completed"] = True
        print(f"已完成提醒事项：{self.reminders[i]['title']} ")
    def search_reminders(self, keyword):
        print(f"搜索结果：")
        for index, reminder in enumerate(self.reminders):
            if keyword in reminder["title"]:
                status = "已完成" if reminder["completed"] else "未完成"
                print(
                    f"{reminder['title']}"
                    f"（{reminder['category']}，{reminder['color']}），（{status}）"
                    f"优先级：{reminder['priority']}"
                )


if __name__ == "__main__":
    # 测试阶段为了防止数据重复添加
    # 在每次启动时自动删除pickle文件
    p = Path.cwd() / "reminders.pkl"
    # unlink = 删除文件；missing_ok=True = 文件本来就不存在也不报错。
    # 每次跑 __main__ 都会先清掉旧的 reminders.pkl，避免上次数据叠进来。
    p.unlink(missing_ok=True)

    reminder = Reminder("reminders.pkl")
    
    # 添加提醒
    print("添加提醒 >>>")
    reminder('添加', '买牛奶', '购物', '黄色', 1)
    reminder('添加', '发邮件', '工作', '蓝色', 2)
    reminder('添加', '学编程', '学习', '红色', 1)
    reminder('添加', '打游戏', '娱乐', '紫色', 4)
    reminder('添加', '谈恋爱', '娱乐', '粉色', 1)
    reminder('添加', '打酱油', '购物', '黄色', 3)

    # 删除提醒
    print("\n删除提醒 >>>")
    reminder.delete_reminder(6)

    # 列举提醒
    print("\n列举提醒 >>>")
    reminder.list_reminders()

    # 完成提醒
    print("\n完成提醒 >>>")
    reminder.complete_reminder(5)

    print("\n列举提醒 >>>")
    reminder.list_reminders()

    # 搜索提醒
    print("\n搜索提醒 >>>")
    reminder.search_reminders("编程")


###############################################
# 添加提醒 >>>
# 已添加提醒事项：买牛奶，分类：购物，优先级：1
# 已添加提醒事项：发邮件，分类：工作，优先级：2
# 已添加提醒事项：学编程，分类：学习，优先级：1
# 已添加提醒事项：打游戏，分类：娱乐，优先级：4
# 已添加提醒事项：谈恋爱，分类：娱乐，优先级：1
# 已添加提醒事项：打酱油，分类：购物，优先级：3

# 删除提醒 >>>
# 已删除提醒事项：打酱油

# 列举提醒 >>>
# 提醒事项：
# 1. 买牛奶，（购物，黄色）（未完成），优先级：1
# 2. 发邮件，（工作，蓝色）（未完成），优先级：2
# 3. 学编程，（学习，红色）（未完成），优先级：1
# 4. 打游戏，（娱乐，紫色）（未完成），优先级：4
# 5. 谈恋爱，（娱乐，粉色）（未完成），优先级：1

# 完成提醒 >>>
# 已完成提醒事项：谈恋爱

# 列举提醒 >>>
# 提醒事项：
# 1. 买牛奶，（购物，黄色）（未完成），优先级：1
# 2. 发邮件，（工作，蓝色）（未完成），优先级：2
# 3. 学编程，（学习，红色）（未完成），优先级：1
# 4. 打游戏，（娱乐，紫色）（未完成），优先级：4
# 5. 谈恋爱，（娱乐，粉色）（已完成），优先级：1

# 搜索提醒 >>>
# 搜索结果：
# 学编程（学习，红色），（未完成）优先级：1


###########################################################
# 答案：
# 列表在内存里负责「这次运行能用」；pkl 负责「下次打开还在」。 
# class Reminder:
#     def __init__(self, storage_file='reminders.pkl'):
#         self.storage_file = Path(storage_file)
#         self.reminders = self.load_reminders()

#     def __call__(self, action, *args, **kwargs):
#         actions = {
#             '添加': self.add_reminder,
#             '查看': self.list_reminders,
#             '删除': self.delete_reminder,
#             '完成': self.complete_reminder,
#             '搜索': self.search_reminders,
#         }

#         if action in actions:
#             actions[action](*args, **kwargs)
#         else:
#             print("无效操作，请使用'添加'、'查看'、'删除'、'完成'或'搜索'。")
            
#     def __getitem__(self, index):
#         return self.reminders[index]

#     def __repr__(self):
#         return f'Reminder(reminders={self.reminders})'

#     def __str__(self):
#         return f'提醒事项共有 {len(self.reminders)} 条'

#     def load_reminders(self):
#         if self.storage_file.exists():
#             with self.storage_file.open('rb') as file:
#                 return pickle.load(file)
#         return []

#     def save_reminders(self):
#         with self.storage_file.open('wb') as file:
#             pickle.dump(self.reminders, file)

#     def add_reminder(self, reminder, category, color, priority=0, delay=None):
#         reminder_item = {'text': reminder, 'category': category, 'color': color,
#                          'completed': False, 'priority': priority}
#         self.reminders.append(reminder_item)
#         self.save_reminders()
#         print(f'已添加提醒事项：{reminder}，分类：{category}，优先级：{priority}')

#         if delay is not None:
#             time.sleep(delay)
#             self.show_reminder(reminder)

#     def show_reminder(self, reminder):
#         print(f'提醒：{reminder}')

#     def list_reminders(self):
#         print('提醒事项：')
#         for i, reminder in enumerate(self.reminders):
#             status = '已完成' if reminder['completed'] else '未完成'
#             print(f'{i + 1}. {reminder["text"]} ({reminder["category"]}, {reminder["color"]})'
#                   f' ({status})，优先级：{reminder["priority"]}')

#     def delete_reminder(self, index):
#         try:
#             removed = self.reminders.pop(index - 1)
#             self.save_reminders()
#             print(f'已删除提醒事项：{removed["text"]}')
#         except IndexError:
#             print('索引无效，请检查提醒事项列表。')

#     def complete_reminder(self, index):
#         try:
#             self.reminders[index - 1]['completed'] = True
#             self.save_reminders()
#             print(f'已完成提醒事项：{self.reminders[index - 1]["text"]}')
#         except IndexError:
#             print('索引无效，请检查提醒事项列表。')

#     def search_reminders(self, keyword):
#         results = [r for r in self.reminders if keyword.lower() in r['text'].lower()]
#         if results:
#             print('搜索结果：')
#             for reminder in results:
#                 status = '已完成' if reminder['completed'] else '未完成'
#                 print(f'{reminder["text"]} ({reminder["category"]}, {reminder["color"]})'
#                       f' ({status})，优先级：{reminder["priority"]}')
#         else:
#             print('未找到与关键词匹配的提醒事项。')













