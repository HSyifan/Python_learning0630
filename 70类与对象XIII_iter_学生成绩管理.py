"""成员判断、真假、比较"""
"""这节课讲三件事：in 怎么判断「里面有没有」、对象在 if 里算不算真、< > == 怎么比。"""

# ========== 1. __contains__：x in 对象 会调用它 ==========
# 3 in c 就是去问 c.__contains__(3)，由你返回 True 或 False
# 这里 data 是 [1, 2, 3, 4, 5]：3 在里面，6 不在
# 工作里写它，是为了让自己的对象能用 in，并且自己规定「有」是什么意思

class C:
    def __init__(self, data):
        self.data = data
    def __contains__(self, item):
        print("嗨~")
        return item in self.data

c = C([1, 2, 3, 4, 5])

print(3 in c)
print(6 in c)


# ========== 2. 没写 __contains__，但写了 __iter__：in 会一个个翻 ==========
# 从第 1 个元素开始比，找到就停，不用自己再写 __contains__
# 3 在第 3 个位置，所以 Next 三次就停，结果 True
# 6 不在里面：5 个都比完，再取一次发现没了，所以 Next 六次，结果 False
# 缺点：每次 in 都要从头扫，数据多了就慢

class C:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        print("Iter", end=" -> ")
        self.i = 0
        return self
    def __next__(self):
        print("Next", end=" -> ")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item

c = C([1, 2, 3, 4, 5])
print(3 in c) # Iter -> Next -> Next -> Next -> True 

print(6 in c) # Iter -> Next -> Next -> Next -> Next -> Next -> Next -> False


# ========== 3. 迭代器也没有，只有 __getitem__：in 会按下标 0、1、2… 去取 ==========
# 取到越界就停。找 3：下标 0、1、2，三次就找到
# 找 6：下标 0 到 5，第 6 次越界，结果 False（不是 7 次）
# 查找顺序：先 __contains__，没有再 __iter__，再没有才 __getitem__
# 自己写容器时，优先自己写 __contains__，避免每次 in 都从头扫

class C:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        print("Getitem", end=" -> ")
        return self.data[index]

c = C([1, 2, 3, 4, 5])
print(3 in c) # Getitem -> Getitem -> Getitem -> True
print(6 in c) # Getitem -> Getitem -> Getitem -> Getitem -> Getitem -> Getitem -> False


# ========== 4. __bool__：bool(对象) 和 if 对象 都会调用它 ==========
# 返回什么，这个对象在 if 里就是什么

class D:
    def __bool__(self):
        print("Bool")
        return True

d = D()
print(bool(d)) # Bool True


# ========== 5. 没写 __bool__，就看 __len__：长度为 0 就是假 ==========
# "FishC" 长度 5，是真；空字符串长度 0，是假
# 两个都没写时，对象永远是真（和普通自定义对象一样）

class D:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        print("Len")
        return len(self.data)

d = D("FishC")
print(bool(d)) # Len True

d = D("")
print(bool(d)) # Len False


# ========== 6. 比较：< 是 __lt__，> 是 __gt__，== 是 __eq__ ==========
# 这里改成按长度比，不按字母
# "FishC" 和 "fishc" 都是 5 个字符：< 和 > 都是 False，== 是 True
# != 没有重写。父类 str 自己有 __ne__，所以还按字母比：大小写不同，结果是 True
# 也就是说，这里的 != 没有反过来用上面的 __eq__

"""和比较相关的魔法方法"""
class S(str):
    def __lt__(self, other):
        return len(self) < len(other)
    def __gt__(self, other):
        return len(self) > len(other)
    def __eq__(self, other):
        return len(self) == len(other)

s1 = S("FishC")
s2 = S("fishc")
print(s1 < s2) # False
print(s1 > s2) # False
print(s1 == s2) # True
print(s1 != s2) # True # 因为没有写，所以走的还是父类


# ========== 7. 把方法设成 None，等于把这个运算关掉 ==========
# __ne__ = None 之后，!= 不再走父类，直接报 TypeError
# __le__、__ge__ 同理，<= 和 >= 也不能用

class S(str):
    def __lt__(self, other):
        return len(self) < len(other)
    def __gt__(self, other):
        return len(self) > len(other)
    def __eq__(self, other):
        return len(self) == len(other)
    __le__ = None
    __ge__ = None
    __ne__ = None

s1 = S("FishC")
s2 = S("fishc")
# print(s1 != s2) # TypeError: 'NoneType' object is not callable


# ========== 8. __contains__ = None：退回扫描也关掉 ==========
# 第 2 段有 __iter__，in 本来还能一个个翻
# 设成 None 后，Python 认为你明确说「不支持 in」，直接报不是容器
# 不写 __contains__：可以退回去扫；写成 None：禁止 in

class C:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        print("Iter", end=" -> ")
        self.i = 0
        return self
    def __next__(self):
        print("Next", end=" -> ")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item
    __contains__ = None

c = C([1, 2, 3, 4, 5])
# print(3 in c) # TypeError: 'C' object is not a container
# print(6 not in c) # TypeError: 'C' object is not a container


# 动动手0：实现一个学生成绩管理系统。
# 大家只需要实现里面相关的方法，让程序成功运行，并获得期待输出即可。

# 期待输出：######################
# 添加成功，小甲鱼 -> ID：100
# 添加成功，不二如是 -> ID：101
# 添加成功，张三李四 -> ID：102
# 查找 -> 小甲鱼，成绩: 999
# 删除成功，张三李四 -> ID：103
# 迭代 -> 姓名：小甲鱼，成绩: 999
# 迭代 -> 姓名：不二如是，成绩: 888
# True
# 2
# True

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        # 成绩相等才算相等
        if isinstance(other, Student):
            return self.score == other.score
        return False

    def __ne__(self, other):
        # 不相等就是相等的反面，避免只改 == 时 != 还走别的规则
        return not self.__eq__(other)

    def __lt__(self, other):
        # self < other：自己的成绩更低
        if isinstance(other, Student):
            return self.score < other.score
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.score <= other.score
        return False

    def __gt__(self, other):
        # s1 > s2 会调用这里。999 > 888，所以是 True
        if isinstance(other, Student):
            return self.score > other.score
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.score >= other.score
        return False


class StudentManager:
    def __init__(self, init_id=100):
        self.students = {}
        self.stu_id = init_id

    def add_student(self, student):
        # 用当前学号当字典的键，存好后再加 1，下一个学生用新学号
        self.students[self.stu_id] = student
        print(f"添加成功，{student.name} -> ID：{self.stu_id}")
        self.stu_id += 1

    def update_score(self, stu_id, new_score):
        # 按学号找到学生，只改成绩
        self.students[stu_id].score = new_score

    def find_student(self, name):
        # 按姓名查找，找到就返回这个学生对象
        for student in self.students.values():
            if student.name == name:
                return student

    def delete_student(self, stu_id):
        # pop 会把这个学号对应的学生取出来并删掉
        student = self.students.pop(stu_id)
        print(f"删除成功，{student.name} -> ID：{stu_id}")

    def __iter__(self):
        # for 开始时调用。先把现有学号记下来，自己当迭代器
        self._ids = list(self.students.keys())
        self._index = 0
        return self

    # 也可以用 iter(self.students.values()) 来实现
    # def __iter__(self):
    #     return iter(self.students.values())

    def __next__(self):
        # for 每次来取下一个学生，取完就停
        if self._index >= len(self._ids):
            raise StopIteration
        student = self.students[self._ids[self._index]]
        self._index += 1
        return student

    def __contains__(self, name):
        # "小甲鱼" in manager 会来这里，按姓名判断在不在
        for student in self.students.values():
            if student.name == name:
                return True
        return False

    def __len__(self):
        # len(manager) 返回还剩几个学生
        return len(self.students)

if __name__ == "__main__":
    # 初始学号ID设置为100
    manager = StudentManager(100)

    # 添加学生
    s1 = Student("小甲鱼", 666)
    s2 = Student("不二如是", 888)
    s3 = Student("张三李四", 233)
    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)

    # 更新学生成绩
    manager.update_score(100, 999)

    # 查找学生
    target = manager.find_student("小甲鱼")
    print(f"查找 -> {target.name}，成绩: {target.score}")

    # 删除学生
    manager.delete_student(102)

    # 迭代学生列表
    for student in manager:
        print(f"迭代 -> 姓名：{student.name}，成绩: {student.score}")

    # 检查学生是否在列表中
    print("小甲鱼" in manager)

    # 获取学生数量
    print(len(manager))

    # 学生之间的成绩PK
    print(s1 > s2)




# 动动手1：升级上一题的学生成绩管理系统。
# 这次我们添加了更多的属性（年龄、性别、班级）、文件保存和加载、异常处理、录入合法性检测、分类搜索等。

# 期待输出：#########################################################
# 添加成功，鱼油A -> ID：100
# 添加成功，鱼油B -> ID：101
# 添加成功，鱼油C -> ID：102
# 添加成功，鱼油C -> ID：103
# 添加成功，鱼油E -> ID：104
# 添加成功，鱼油F -> ID：105
# 名字搜索结果：
# ID：102，姓名：鱼油C，成绩：484，年龄：19，性别：F，班级：Class3
# ID：103，姓名：鱼油C，成绩：666，年龄：21，性别：F，班级：Class1
# 性别搜索结果：
# ID：102，姓名：鱼油C，成绩：484，年龄：19，性别：F，班级：Class3
# ID：103，姓名：鱼油C，成绩：666，年龄：21，性别：F，班级：Class1
# ID：105，姓名：鱼油F，成绩：543，年龄：19，性别：F，班级：Class3
# 班级搜索结果:
# ID：101，姓名：鱼油B，成绩：653，年龄：22，性别：M，班级：Class2
# ID：104，姓名：鱼油E，成绩：547，年龄：18，性别：M，班级：Class2
# 删除成功，鱼油C -> ID：102
# 迭代 -> 姓名：鱼油A，成绩: 594
# 迭代 -> 姓名：鱼油B，成绩: 653
# 迭代 -> 姓名：鱼油C，成绩: 666
# 迭代 -> 姓名：鱼油E，成绩: 547
# 迭代 -> 姓名：鱼油F，成绩: 543
# 5
# False
# False
# True
# True


from pathlib import Path

class Student:
    def __init__(self, stu_id, name, score, age, gender, class_name):
        self.stu_id = stu_id
        self.name = name
        self.score = score
        self.age = age
        self.gender = gender
        self.class_name = class_name

    # 检查输入是否合法
    def validate_input(self):
        # 不合法就抛 ValueError，外面的 try/except 会接住
        if not isinstance(self.name, str) or len(self.name) >= 10:
            raise ValueError("姓名长度需要小于10个字符")
        if not isinstance(self.age, int) or not 1 <= self.age <= 120:
            raise ValueError("年龄需要在1~120之间")
        if self.gender not in ("M", "F"):
            raise ValueError("性别只能填写M或F")
        if not isinstance(self.class_name, str) or len(self.class_name) >= 10:
            raise ValueError("班级长度需要小于10个字符")

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.score == other.score
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.score < other.score
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.score <= other.score
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.score > other.score
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.score >= other.score
        return False


class StudentFileManager:
    def __init__(self, data_file='students.txt'):
        self.data_file = Path(data_file)

    def load_students(self):
        # 文件还不存在时，返回空字典，表示还没有学生
        students = {}
        if not self.data_file.exists():
            return students

        # 一行一个学生：学号,姓名,成绩,年龄,性别,班级
        for line in self.data_file.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            stu_id, name, score, age, gender, class_name = line.split(",")
            stu_id = int(stu_id)
            students[stu_id] = Student(stu_id, name, int(score), int(age), gender, class_name)
        return students

    def save_students(self, students):
        # 把字典里的学生写回文件，覆盖旧内容
        lines = []
        for student in students.values():
            lines.append(
                f"{student.stu_id},{student.name},{student.score},{student.age},{student.gender},{student.class_name}"
            )
        text = "\n".join(lines)
        if text:
            text += "\n"
        self.data_file.write_text(text, encoding="utf-8")
        

class StudentManager:
    def __init__(self, student_file_manager):
        self.students = {}
        self.student_file_manager = student_file_manager
        self.load_students()

    def load_students(self):
        # 启动时把文件里的学生读进 self.students
        self.students = self.student_file_manager.load_students()

    def save_students(self):
        # 把当前字典交给文件管理器写回 students.txt
        self.student_file_manager.save_students(self.students)

    def add_student(self, student):
        # 先检查姓名、年龄、性别、班级，不合法会抛 ValueError
        student.validate_input()
        if student.stu_id in self.students:
            raise ValueError("ID已存在")
        self.students[student.stu_id] = student
        print(f"添加成功，{student.name} -> ID：{student.stu_id}")

    def update_score(self, stu_id, new_score):
        # 按学号改成绩。主程序把 103 从 655 改成 666
        if stu_id not in self.students:
            raise ValueError("ID未找到")
        self.students[stu_id].score = new_score

    def search_by_name(self, name):
        # 姓名可能重复，所以返回列表，不返回单个学生
        return [student for student in self.students.values() if student.name == name]

    def search_by_gender(self, gender):
        return [student for student in self.students.values() if student.gender == gender]

    def search_by_class(self, class_name):
        return [student for student in self.students.values() if student.class_name == class_name]
        
    def delete_student(self, stu_id):
        if stu_id in self.students:
            student = self.students.pop(stu_id)
            print(f"删除成功，{student.name} -> ID：{student.stu_id}")
            del student
        else:
            raise ValueError("ID未找到")

    def __iter__(self):
        self.values = list(self.students.values())
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.values):
            student = self.values[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

    def __contains__(self, name):
        return any(student.name == name for student in self.students.values())

    def __len__(self):
        return len(self.students)

if __name__ == "__main__":
    file_manager = StudentFileManager()
    manager = StudentManager(file_manager)

    try:
        # 添加学生
        s1 = Student(100, "鱼油A", 594, 20, 'M', 'Class1')
        s2 = Student(101, "鱼油B", 653, 22, 'M', 'Class2')
        s3 = Student(102, "鱼油C", 484, 19, 'F', 'Class3')
        s4 = Student(103, "鱼油C", 655, 21, 'F', 'Class1')
        s5 = Student(104, "鱼油E", 547, 18, 'M', 'Class2')
        s6 = Student(105, "鱼油F", 543, 19, 'F', 'Class3')
        manager.add_student(s1)
        manager.add_student(s2)
        manager.add_student(s3)
        manager.add_student(s4)
        manager.add_student(s5)
        manager.add_student(s6)

        # 更新学生成绩
        manager.update_score(103, 666)

        # 搜索学生
        students_by_name = manager.search_by_name("鱼油C")
        students_by_gender = manager.search_by_gender('F')
        students_by_class = manager.search_by_class("Class2")

        # 输出搜索结果
        print("名字搜索结果：")
        for student in students_by_name:
            print(f"ID：{student.stu_id}，姓名：{student.name}，成绩：{student.score}，年龄：{student.age}，性别：{student.gender}，班级：{student.class_name}")

        print("性别搜索结果：")
        for student in students_by_gender:
            print(f"ID：{student.stu_id}，姓名：{student.name}，成绩：{student.score}，年龄：{student.age}，性别：{student.gender}，班级：{student.class_name}")

        print("班级搜索结果:")
        for student in students_by_class:
            print(f"ID：{student.stu_id}，姓名：{student.name}，成绩：{student.score}，年龄：{student.age}，性别：{student.gender}，班级：{student.class_name}")

        # 删除学生
        manager.delete_student(102)

        # 迭代学生列表
        for student in manager:
            print(f"迭代 -> 姓名：{student.name}，成绩: {student.score}")

        # 获取学生数量
        print(len(manager))

        # 检查学生是否在列表中
        print("小甲鱼" in manager)


        # 学生之间的成绩PK
        print(s1 > s2)
        print(s3 < s4)
        print(s5 != s6)

        # 保存数据
        manager.save_students()
        
    except ValueError as e:
        print(f"出错啦：{e}")






































