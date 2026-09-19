class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

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


class StudentManager:
    def __init__(self, init_id=100):
        self.students = {}
        self.stu_id = init_id

    def add_student(self, student):
        if student not in self.students.values():
            self.students[self.stu_id] = student
            print(f"添加成功，{student.name} -> ID：{self.stu_id}")
            self.stu_id += 1

    def update_score(self, stu_id, new_score):
        if stu_id in self.students:
            self.students[stu_id].score = new_score

    def find_student(self, name):
        for student in self.students.values():
            if student.name == name:
                return student

    def delete_student(self, stu_id):
        if stu_id in self.students:
            student = self.students.pop(stu_id)
            print(f"删除成功，{student.name} -> ID：{self.stu_id}")
            del student

    # 这里应该会让很多鱼油意想不到，因为我们要构造一个迭代器
    # 为了方便地获取和使用迭代器中的每个元素，我们将字典的视图对象转换为列表
    # 下面__next__()就可以根据索引值来访问每一个元素了
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
        for student in self.students.values():
            if student.name == name:
                return student

    def __len__(self):
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
