"""多态"""
# 数字相加
print(3 + 5) # 8

# 字符串相加
print("Py" + "FishC") # PyFishC

# len的多态
print(len("FishC")) # 5
print(len(["FishC", "Python", "Java"])) # 3
print(len({"name": "FishC", "age": 18})) # 2

# 多态的体现
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("三角形")
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2

s = Square(5)
c = Circle(6)
t = Triangle(3, 4)

print(s.name, s.area())
print(c.name, c.area())
print(t.name, t.area())


# 实现多态接口
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只沙雕猫咪，我叫{self.name}，今年{self.age}岁~")
    def say(self):
        print("mua~")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只小狗，我叫{self.name}，今年{self.age}岁~")
    def say(self):
        print("呦吼~")

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只小猪，我叫{self.name}，今年{self.age}岁~")
    def say(self):
        print("oink~")

c = Cat("web", 4)
d = Dog("布布", 7)
p = Pig("大肠", 5)

def animal(x):
    x.intro()
    x.say()

animal(c)
animal(d)
animal(p)


"""鸭子类型"""
class Bicycle:
    def intro(self):
        print("我曾经跨过山和大海，也穿过人山人海~")
    def say(self):
        print("都有自行车了，要什么兰博基尼？")
    
b = Bicycle()
animal(b)



# 动动手0：请按要求编写一个企业员工管理程序。
# 需要实现的要求：
# a. 员工分类：普通员工（Employee）、组长（Teamleader）、经理（Manager）
# b. 员工属性：姓名（name）、职位（job）、级别（grade）、工龄（year）、工号（uid）
# c. 员工方法：
# - get_uid() -- 获取工号
# - get_name() -- 获取姓名
# - get_job() -- 获取职位
# - get_grade() -- 获取级别
# - get_year() -- 获取工龄
# - salary() -- 统计并返回工资（计算方法如下）
# d. 员工工资计算方法：
# - 普通员工：3000 + 500 * 级别 + 50 * 工龄
# - 组长：4000 + 800 * 级别 + 100 * 工龄
# - 经理：5000 + 1000 * (级别 + 工龄)
# e. 程序功能：
# - 录入员工数据功能（工号自动分配，由 10000 开始）
# - 查询功能，分为员工查询和职位查询（见程序实现截图）
# - 各类员工级别数量如下：
# -- 普通员工：10 级
# -- 组长：6 级
# -- 经理：3 级
# - 升级功能：支持增加多级；当超过当前职位最高级别时，进行升职操作（无论增加多少个级别，只要发生升职，级别一律初始化为 1 级，见程序实现截图）."~b$e
# - 降级功能：支持减少多级；当超过当前职位最高级别时，进行升职操作（无论减少多少个级别，只要发生降职，级别一律初始化为当前职位最高级别，见程序实现截图）

class Employee:
    def __init__(self, name, job, grade, year, uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid
    def get_uid(self):
        return self.uid
    def get_name(self):
        return self.name
    def get_job(self):
        return self.job
    def get_grade(self):
        return self.grade
    def get_year(self):
        return self.year
    def salary(self):
        return 3000 + 500 * self.grade + 50 * self.year
    max_grade = 10

class Teamleader(Employee):
    # 与父类构造相同，只重写工资和最高级别即可
    def salary(self):
        return 4000 + 800 * self.grade + 100 * self.year
    max_grade = 6

class Manager(Employee):
    def salary(self):
        return 5000 + 1000 * (self.grade + self.year)
    max_grade = 3


class ManageSystem:
    def __init__(self):
        self.employees = {}       # {工号: Employee对象}
        self.next_uid = 10000     # 下一张待发放的工号

    job_map = {
        'E': "普通员工",
        'T': "组长",
        'M': "经理"
    }
    class_map = {
        'E': Employee,
        'T': Teamleader,
        'M': Manager,
    }

    def enter_system(self):
        while True:
            ins = input("1.录入;2.查询;3.升级;4.降级;5.退出：")
            if ins == '1':
                self.add_employee()
            elif ins == '2':
                self.query_employee()
            elif ins == '3':
                self.upgrade_employee()
            elif ins == '4':
                self.downgrade_employee()
            elif ins == '5':
                break
            else:
                print("输入不合法，请重新输入")

    def add_employee(self):
        name = input("姓名：")
        job = input("职位（E.普通员工,T.组长,M.经理）：")
        if job not in self.class_map:
            print("职位输入有误！")
            return
        year = int(input("工龄："))
        grade = int(input("级别："))
        cls = self.class_map[job]
        while grade < 1 or grade > cls.max_grade:
            grade = int(input(f"该职位最高级别为{cls.max_grade}，请重新录入级别："))
        employee = cls(name, job, grade, year, self.next_uid)
        self.employees[self.next_uid] = employee
        print(f"录入成功！姓名：{name}，工号：{self.next_uid}，薪资：{employee.salary()}")
        self.next_uid += 1

    def query_employee(self):
        ins = input("1.员工查询;2.职位查询：")
        if ins == '1':
            uid = int(input("请输入工号："))
            if uid in self.employees:
                e = self.employees[uid]
                print(e.get_name())
                print(e.get_job())
                print(e.get_grade())
                print(e.get_year())
                print(e.salary())
            else:
                print("该工号不存在！")
        elif ins == '2':
            job = input("职位（E.普通员工；T.组长；M.经理）：")
            if job not in self.job_map:
                print("职位输入有误！")
                return
            matched = [(uid, emp) for uid, emp in self.employees.items()
                       if emp.get_job() == job]
            if not matched:
                print(f"目前公司没有{self.job_map[job]}!")
            else:
                print(f"目前{self.job_map[job]}共有{len(matched)}人")
                for uid, emp in matched:
                    print(f"{uid} - {emp.get_name()}")

    def upgrade_employee(self):
        uid = int(input("请输入工号："))
        if uid not in self.employees:
            print("该工号不存在！")
            return
        e = self.employees[uid]
        old_salary = e.salary()
        print(f"{e.get_name()}，工号：{uid}，当前职位：{e.get_job()}{e.get_grade()}，当前薪资：{old_salary}")
        up = int(input("请输入需要增加的级数："))
        new_grade = e.get_grade() + up
        if new_grade <= e.max_grade:
            e.grade = new_grade
        else:
            if e.get_job() == 'M':
                print("经理无法再升职！")
                return
            elif e.get_job() == 'T':
                self.employees[uid] = Manager(e.get_name(), 'M', 1, e.get_year(), uid)
            elif e.get_job() == 'E':
                self.employees[uid] = Teamleader(e.get_name(), 'T', 1, e.get_year(), uid)
        e = self.employees[uid]  # 升职换类后重新取对象
        new_salary = e.salary()
        print("升级成功!")
        print(f"{e.get_name()}，工号：{uid}，升级后职位：{e.get_job()}{e.get_grade()}，升级后薪资：{new_salary}(+{new_salary - old_salary})")

    def downgrade_employee(self):
        uid = int(input("请输入工号："))
        if uid not in self.employees:
            print("该工号不存在！")
            return
        e = self.employees[uid]
        old_salary = e.salary()
        print(f"{e.get_name()}，工号：{uid}，当前职位：{e.get_job()}{e.get_grade()}，当前薪资：{old_salary}")
        down = int(input("请输入需要减少的级数："))
        new_grade = e.get_grade() - down
        if new_grade >= 1:
            e.grade = new_grade
        else:
            if e.get_job() == 'E':
                print("普通员工无法再降职！")
                return
            elif e.get_job() == 'T':
                self.employees[uid] = Employee(e.get_name(), 'E', Employee.max_grade, e.get_year(), uid)
            elif e.get_job() == 'M':
                self.employees[uid] = Teamleader(e.get_name(), 'T', Teamleader.max_grade, e.get_year(), uid)
        e = self.employees[uid]  # 降职换类后重新取对象
        new_salary = e.salary()
        delta = new_salary - old_salary  # 自带正负号，避免写成 (-{负数}) 变成 --
        print("降级成功!")
        print(f"{e.get_name()}，工号：{uid}，降级后职位：{e.get_job()}{e.get_grade()}，降级后薪资：{new_salary}({delta})")


def main():
    manage = ManageSystem()
    manage.enter_system()

main()

#####################################################
# 录入功能实现如下：
# 1.录入;2.查询;3.升级;4.降级;5.退出：1
# 姓名：粟云云
# 职位（E.普通员工,T.组长,M.经理）：M
# 工龄：12
# 级别：3
# 录入成功！姓名：粟云云，工号：10000，薪资：20000
# 1.录入;2.查询;3.升级;4.降级;5.退出：1
# 姓名：粟凡凡
# 职位（E.普通员工,T.组长,M.经理）：T
# 工龄：10
# 级别：8
# 该职位最高级别为6，请重新录入级别：6
# 录入成功！姓名：粟凡凡，工号：10001，薪资：9800
# 1.录入;2.查询;3.升级;4.降级;5.退出：1
# 姓名：粟福安
# 职位（E.普通员工,T.组长,M.经理）：E
# 工龄：5
# 级别：5
# 录入成功！姓名：粟福安，工号：10002，薪资：5750

####################################################
# 查询功能实现如下：
# 1.录入;2.查询;3.升级;4.降级;5.退出：2
# 1.员工查询;2.职位查询：1
# 请输入工号：10001
# 粟凡凡
# T
# 6
# 10
# 9800
# 1.录入;2.查询;3.升级;4.降级;5.退出：2
# 1.员工查询;2.职位查询：1
# 请输入工号：10086
# 该工号不存在！
# 1.录入;2.查询;3.升级;4.降级;5.退出：2
# 1.员工查询;2.职位查询：2
# 职位（E.普通员工；T.组长；M.经理）：E
# 目前普通员工共有1人
# 10002 - 粟福安
# 1.录入;2.查询;3.升级;4.降级;5.退出：2
# 1.员工查询;2.职位查询：2
# 职位（E.普通员工；T.组长；M.经理）：M
# 目前经理共有1人
# 10000 - 粟云云

############################################################
# 程序升降级功能实现如下：
# 1.录入;2.查询;3.升级;4.降级;5.退出：3
# 请输入工号：10001
# 粟凡凡，工号：10001，当前职位：T6，当前薪资：9800
# 请输入需要增加的级数：1
# 升级成功!
# 粟凡凡，工号：10001，升级后职位：M1，升级后薪资：16000(+6200)      
# 1.录入;2.查询;3.升级;4.降级;5.退出：2
# 1.员工查询;2.职位查询：2
# 职位（E.普通员工；T.组长；M.经理）：T
# 目前公司没有组长!
# 1.录入;2.查询;3.升级;4.降级;5.退出：4
# 请输入工号：10000
# 粟云云，工号：10000，当前职位：M3，当前薪资：20000
# 请输入需要减少的级数：5
# 降级成功!
# 粟云云，工号：10000，降级后职位：T6，降级后薪资：10000(-10000)     
# 1.录入;2.查询;3.升级;4.降级;5.退出：5











