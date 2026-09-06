"""绑定"""
class C:
    def get_self(self):
        print(self)

c = C()

# 等同于
C.get_self(c) # <__main__.C object at 0x000001444C889E80>
c.get_self()  # <__main__.C object at 0x000001444C889E80>

# 绑定属性。
# 实例中，类的方法是共享的，类的属性是独立的。
d = C()
d.x = 250
print(d.x) # 250

# print(c.x) # 报错

c.x = 520
print(c.x) # 520


print(d.__dict__) # {'x': 250}
print(c.__dict__) # {'x': 520}

d.y = 660
print(d.__dict__) # {'x': 250, 'y': 660}

# 绑定方法
class C:
    def set_x(self, v):
       self.x = v

c = C()
print(c.__dict__) # {}

c.set_x(250)
print(c.__dict__) # {'x': 250}

print(c.x) # 250


class C:
    x = 100
    def set_x(self, v):
        x = v # 因为这里不是self.x = v,所以x是局部变量，不是类属性

c = C()
c.set_x(250)
print(c.x) # 100
print(C.x) # 100

# 严重不建议使用，因为这样会影响所有实例的x属性
C.x = 250
print(c.x) # 250

# 对象没有属性，不代表对象的类没有，也不代表类的父类没有
# python找了对象的，类，父类的属性，都找不到才会报错。
print(c.__dict__) # {}
# print(c.y) # 报错

"""旁门左道"""
# 对象的属性机制，底层就是「名字 → 值」的映射，和字典很像
# 动态添加属性
class C:
    pass

C.x = 250
C.y = "小甲鱼"
C.z = [1, 2, 3]
print(C.x) # 250
print(C.y) # '小甲鱼'
print(C.z) # [1, 2, 3]

d = {}
d['x'] = 250
d['y'] = "小甲鱼"
d['z'] = [1, 2, 3]
print(d['x']) # 250
print(d['y']) # 小甲鱼
print(d['z']) # [1, 2, 3]

class C:
    pass

c = C()
c.x = 250
c.y = "小甲鱼"
c.z = [1, 2, 3]


# 练习题：
class C:
    x = 100
    def get_x(self):
        print(C.x)
c = C()
c.x = 250
c.get_x()
# 请问这里会打印什么内容？



class C:
    def f(self):
        print("Hello FishC.")
c = C()
print(type(C.f) == type(c.f)) # False
# 请问这里会打印什么内容？

class C:
    x = 100
    def set_x(self, x):
        self.x = x
c = C()
d = C()
c.set_x(250)
# d.set_x(520)
print(c.x) # 250
print(d.x) # 100
# 请问这里会打印什么内容？

class C:
    x = [1, 2, 3]
    def add_x(self, x):
        self.x.append(x)
c = C()
d = C()
c.add_x(250)
d.add_x(520)
print(c.x) # [250, 520]
# 请问这里会打印什么内容？


# 动动手0：请帮开餐馆的小花开发一个点餐程序，要求如下。
# 菜品种类如下：
#   洋葱炒牛肉（1 份洋葱、1 份牛肉）
#   洋葱炒羊肉（1 份洋葱、1 份羊肉）
#   煎蛋（2 份蛋）
#   番茄炒蛋（2 份番茄、3 份蛋）
#   土豆萝卜炖羊肉（2 份土豆、1份萝卜、2 份羊肉）
# 肉类价格：
#   鸡蛋：1 元 1 份
#   牛肉：25 元 1 份
#   羊肉：30 元 1 份
# 菜类价格：
#   洋葱：2 元 1 份
#   番茄：2 元 1 份
#   土豆：3 元 1 份
#   萝卜：3 元 1 份
# 题目要求：
#   1. Memu 类用于实例化菜单
#   2.Memu 类需要有 order() 方法，用于点菜
#   3.Memu 类需要有 pay() 方法，用于统计最终价格
#   4.需要考虑同时点多个菜品的需求
#   5.需要考虑一个菜品点多次的需求
# 程序实现如下（考虑同时点多个菜品的需求）：

class Meat:
    egg = 1
    beef = 25
    mutton = 30

class Vegetable:
    onion = 2
    tomato = 2
    potato = 3
    carrot = 3

class Menu:
    def __init__(self):
        self.dishes = {1: "洋葱炒牛肉", 2: "洋葱炒羊肉", 3: "煎蛋", 4: "番茄炒蛋", 5: "土豆萝卜炖羊肉"}
        self.recipes = {1: {"洋葱": 1, "牛肉": 1}, 2: {"洋葱": 1, "羊肉": 1}, 3: {"鸡蛋": 2}, 4: {"番茄": 2, "鸡蛋": 3}, 5: {"土豆": 2, "萝卜": 1, "羊肉": 2}}
        self.ordered = []

    def order(self):
        print("客官想要吃点什么？")
        choice = input("1.洋葱炒牛肉 2.洋葱炒羊肉 3.煎蛋 4.番茄炒蛋 5.土豆萝卜炖羊肉:")
        for each in choice.split(): # 将输入的字符串按空格分割成列表
            each = int(each)
            if each in self.dishes.keys():
                self.ordered.append(each)
            else:
                print(f"对不起，我们没有这个菜品：{each}")

    def pay(self):
        prices = {
        "鸡蛋": Meat.egg,      
        "牛肉": Meat.beef,     
        "羊肉": Meat.mutton,   
        "洋葱": Vegetable.onion,
        "番茄": Vegetable.tomato,
        "土豆": Vegetable.potato,
        "萝卜": Vegetable.carrot,
        }

        ingredients = {}
        for each in self.ordered: # 对于2层字典，先遍历外层，再遍历内层
            for key, value in self.recipes[each].items(): # 外层字典某一个元素的值，是内层字典，他的键值对
                if key in ingredients:
                    ingredients[key] += value # 如果key（鸡蛋）在ingredients中，则将value（2）加到ingredients[key]中
                else:
                    ingredients[key] = value
                    print("ingredients:", ingredients)
        
        total = 0
        for key, value in ingredients.items():
            price = prices[key]
            print(f"{key} = {price} * {value}")
            total += price * value
        print(f"感谢惠顾，您一共消费了{total}元，欢迎下次光临~")


menu = Menu()
menu.order()
menu.pay()

#################################################################
# 客官想要吃点什么？
# 1.洋葱炒牛肉 2.洋葱炒羊肉 3.煎蛋 4.番茄炒蛋 5.土豆萝卜炖羊肉:1 2 3 3 3
# 洋葱 = 2 * 2
# 牛肉 = 25 * 1
# 羊肉 = 30 * 1
# 鸡蛋 = 1 * 6
# 感谢惠顾，您一共消费了65元，欢迎下次光临~


