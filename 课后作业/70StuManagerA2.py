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
        if not (1 <= len(self.name) <= 10):
            raise ValueError("姓名长度需要小于10个字符。")
        if not (1 <= self.age <= 120):
            raise ValueError("年龄需要在1~120之间。")
        if self.gender not in ('M', 'F'):
            raise ValueError("性别只能填写M或F")
        if not (1 <= len(self.class_name) <= 10):
            raise ValueError("班级长度需要小于10个字符。")

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


# 定义学生文件管理类，负责学生数据的加载和保存
class StudentFileManager:
    def __init__(self, data_file='students.txt'):
        self.data_file = Path(data_file)

    # 从文件加载学生数据
    def load_students(self):
        students = []
        if self.data_file.exists():
            with self.data_file.open('r', encoding='utf-8') as f:
                for line in f:
                    stu_id, name, score, age, gender, class_name = line.strip().split(',')
                    student = Student(int(stu_id), name, float(score), int(age), gender, class_name)
                    students.append(student)
        return students

    # 将学生数据保存到文件
    def save_students(self, students):
        with self.data_file.open('w', encoding='utf-8') as f:
            for student in students:
                f.write(f"{student.stu_id},{student.name},{student.score},{student.age},{student.gender},{student.class_name}\n")


class StudentManager:
    def __init__(self, student_file_manager):
        self.students = {}
        self.student_file_manager = student_file_manager
        self.load_students()

    # 从文件加载学生数据
    def load_students(self):
        students = self.student_file_manager.load_students()
        self.students = {student.stu_id: student for student in students}

    # 将学生数据保存到文件
    def save_students(self):
        self.student_file_manager.save_students(self.students.values())

    def add_student(self, student):
        student.validate_input()
        if student.stu_id not in self.students:
            self.students[student.stu_id] = student
            print(f"添加成功，{student.name} -> ID：{student.stu_id}")
        else:
            raise ValueError("ID重复")

    def update_score(self, stu_id, new_score):
        if stu_id in self.students:
            self.students[stu_id].score = new_score
        else:
            raise ValueError("ID未找到")

    # 根据姓名、性别或班级搜索学生，简单的列表推导式有时候确实非常香~
    def search_by_name(self, name):
        return [student for student in self.students.values() if student.name == name]

    def search_by_gender(self, gender):
        return [student for student in self.students.values() if student.gender == gender]

    def search_by_class(self, class_name):
        return [student for student in self.students.values() if student.class_name.lower() == class_name.lower()]

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

    # any -> https://fishc.com.cn/thread-191254-1-1.html
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
