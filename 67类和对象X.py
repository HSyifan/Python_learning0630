"""按位运算符"""
print(3 & 2) # 2
print(3 & 4) # 0

# 按位与运算
# 3和2按位与运算结果为2，因为3的二进制表示为11，2的二进制表示为10，按位与运算结果为10，即2。
# 3和4按位与运算结果为0，因为3的二进制表示为11，4的二进制表示为100，按位与运算结果为000，即0。
print(bin(2)) # 0b10
print(bin(3)) # 0b11
print(bin(4)) # 0b100

# 按位或运算
# 3和2按位或运算结果为3，因为3的二进制表示为11，2的二进制表示为10，按位或运算结果为11，即3。
# 3和4按位或运算结果为7，因为3的二进制表示为11，4的二进制表示为100，按位或运算结果为111，即7。
print(3 | 2) # 3
print(3 | 4) # 7

# 按位取反运算
# 2按位取反运算结果为-3，因为2的二进制表示为10，按位取反运算结果为11，即-3。
# 3按位取反运算结果为-4，因为3的二进制表示为11，按位取反运算结果为100，即-4。
# 4按位取反运算结果为-5，因为4的二进制表示为100，按位取反运算结果为101，即-5。
print(~2) # -3
print(~3) # -4
print(~4) # -5

# 按位异或运算
# 3和2按位异或运算结果为1，因为3的二进制表示为11，2的二进制表示为10，按位异或运算结果为01，即1。
# 3和4按位异或运算结果为7，因为3的二进制表示为11，4的二进制表示为100，按位异或运算结果为111，即7。
print(3 ^ 2) # 1
print(3 ^ 4) # 7


# 按位左移运算
# 8按位右移2位运算结果为2，因为8的二进制表示为1000，按位右移运算结果为010，即2。
# 8按位右移3位运算结果为1，因为8的二进制表示为1000，按位右移运算结果为001，即1。
# 8按位左移2位运算结果为32，因为8的二进制表示为1000，按位左移运算结果为100000，即32。
print(bin(8)) # 0b1000
print(8 >> 2) # 2
print(8 >> 3) # 1
print(8 << 2) # 32

# 左移2位相当于除以2的2次方
# 左移3位相当于除以2的3次方
print(8 // pow(2, 2)) # 2
print(8 // pow(2, 3)) # 1


# 练习题：
print(2 & 3 | 4) # 6
print(2 & 3 | 4 & 1) # 2
print(2 & 3 & 1 | 4) # 4

print(2 << 3) # 16
print(2 >> 3) # 0
# print(2 << -2) # 0
# print(2 >> 0.5) # 1


# 动动手0：定义一个实现一进制的类，要求重载加（+）、减（-）、乘（*）、除（/）、地板除（//）
# 五个运算符（为了简化实现逻辑，我们约定无论除法还是地板除，都统一采用地板除，即不考虑小数位）。

class UnaryNumber:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        result = ""
        if self.value < 0:
            result += "-"
        for i in range(abs(self.value)):
            result += "1"
        return result

    def __add__(self, other):
        return UnaryNumber(self.value + other.value)

    def __sub__(self, other):
        return UnaryNumber(self.value - other.value)

    def __mul__(self, other):
        return UnaryNumber(self.value * other.value)

    def _div(self, other):
        # 作业约定 / 和 // 都用整除；商为 0 时一进制里一个 1 都没有
        result = self.value // other.value
        if result == 0:
            return "没有"
        return UnaryNumber(result)

    def __truediv__(self, other):
        return self._div(other)

    def __floordiv__(self, other):
        return self._div(other)

    def __int__(self):
        return int(self.value)


x = UnaryNumber(3)
y = UnaryNumber(5)

print("动动手0：")
print(x + y)   # 11111111   3+5=8
print(x - y)   # -11        3-5=-2
print(y - x)   # 11         5-3=2
print(x * y)   # 15 个 1
print(x / y)   # 没有       3//5=0
print(y / x)   # 1          5//3=1
print(y // x)  # 1
print(int(x))  # 3
print(int(y))  # 5



# 动动手1：编写一个电影票订购系统。
# 需要实现的功能：
# 查看信息
# 预订座位
# 查看预订
# a. 电影院（Cinema）：用于管理电影的添加和信息呈现
# 添加电影和播放时间（add_movie）
# 显示所有电影及其播放时间（show_movies）
# b. 座位（Seat）：用于管理座位
# 管理座位是否被预定（reserve）
# c. 预订系统（MovieBookingSystem）：用于管理预定信息
# 预定座位操作（reserve_seat）
# 查看预订信息（view_reservation）

import datetime

# 判断：这个类的名字是单数的一件东西，还是一个容器？
# 单数 → __init__ 里用 self.xxx。
# 容器 → __init__ 里用空字典/空列表，再 add_xxx。

# 开写前五条（可以抄在作业纸上）
# 1. 名词有哪些？哪个是东西，哪个是盒子？
# 2. 每份数据挂在谁的 self 上？
# 3. 这个对象启动时就要有，还是用到再造？
# 4. 这个动词改的是谁的数据？跨两个就写系统。
# 5. 查找用字典，还是记账用列表？

# 1. 名词有哪些？哪个是东西，哪个是盒子？
# 电影院：盒子
# 电影：东西
# 座位：东西
# 预订：动词，跨两个就写系统。
# 2. 每份数据挂在谁的 self 上？
# 电影院：self.movies
# 电影：self.movies
# 座位：self.seats
# 预订：self.reservations
# 3. 这个对象启动时就要有，还是用到再造？
# 电影院：启动时就要有
# 电影：用到再造
# 座位：用到再造
# 预订：用到再造
# 4. 这个动词改的是谁的数据？跨两个就写系统。
# 电影院：self.movies
# 电影：self.movies
# 座位：self.seats
# 预订：self.reservations
# 5. 查找用字典，还是记账用列表？
# 电影院：字典
# 电影：字典
# 座位：字典
# 预订：列表

class Cinema:
    def __init__(self):
        # {片名: [日期, [场次1, 场次2, ...]]}  后面是开场时间，不是开始~结束
        self.movies = {
            "秋天的狸狸": ["2026-09-12", ["14:00", "18:00"]],
            "小珍珠的迷宫": ["2026-09-12", ["16:00", "20:00"]],
        }

    def add_movie(self, movie, day, *times):
        date = datetime.date.fromisoformat(day)
        self.movies[movie] = [str(date), list(times)]

    def show_movies(self):
        print("\n电影时间表 >>>")
        for movie, info in self.movies.items():
            date, times = info
            print(f"《{movie}》")
            print(f"{date}：{'，'.join(times)}")


class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id   # 例如 "6-8"
        self.reserved = False    # 还没被订

    def reserve(self):
        if self.reserved is False:
            self.reserved = True
            return True
        else:
            return False


class MovieBookingSystem:
    def __init__(self):
        self.cinema = Cinema()
        # 一场戏的一把椅子：{(电影, 日期, 时间, 座位号): Seat}
        self.seats = {}
        self.reservations = []   # 订成功的记录，给「查看预订」用

    def reserve_seat(self):
        movie = input("\n请输入电影名称：").strip("《》")
        day = input("请输入日期（年-月-日）：")
        time = input("请输入时间（时:分）：")
        seat_id = input("请输入座位号（排数-座位号）：")

        # self.cinema                         系统里的那个 Cinema 对象
        # self.cinema.movies                  电影表字典
        # self.cinema.movies[movie]           这部电影的那一条，例如
        #                                     ["2026-09-12", ["14:00", "18:00"]]
        # self.cinema.movies[movie][0]        这条的第 0 个：日期字符串 "2026-09-12"

        if movie not in self.cinema.movies:
            print("没有这部电影")
            return
        if day not in self.cinema.movies[movie][0]:
            print("没有这个日期")
            return
        if time not in self.cinema.movies[movie][1]:
            print("没有这个时间")
            return

        key = (movie, day, time, seat_id)
        if key not in self.seats:
            self.seats[key] = Seat(seat_id)
        else:
            print("座位已被预订")
            return

        self.seats[key].reserve()
        self.reservations.append(key)
        print("预订成功!")

    def view_reservation(self):
        movie = input("\n请输入电影名称：").strip("《》")
        day = input("请输入日期（年-月-日）：")
        time = input("请输入时间（时:分）：")
        if movie not in self.cinema.movies:
            print("没有这部电影")
            return
        if day not in self.cinema.movies[movie][0]:
            print("没有这个日期")
            return
        if time not in self.cinema.movies[movie][1]:
            print("没有这个时间")
            return

        print("预订的座位：")
        found = False
        for rec_movie, rec_day, rec_time, seat_id in self.reservations:
            # 判断：(rec_movie, rec_day, rec_time) 和 (movie, day, time) 是否相等
            if (rec_movie, rec_day, rec_time) == (movie, day, time):
                row, col = seat_id.split("-")
                print(f"{row}排，{col}号")
                found = True
        if not found:
            print("暂无预订。")

    def welcome(self):
        print("欢迎来到电影票订购系统")
        ins = ""
        while ins != "4":
            print("\n1. 查看电影")
            print("2. 预订座位")
            print("3. 查看预订")
            print("4. 退出系统")
            ins = input("请输入操作指令：")
            if ins == "1":
                self.cinema.show_movies()
            elif ins == "2":
                self.reserve_seat()
            elif ins == "3":
                self.view_reservation()
            elif ins == "4":
                print("感谢使用，再见。")
            else:
                print("输入无效，请重新选择。")


MovieBookingSystem().welcome()
 

#########################################
# 欢迎来到电影票订购系统
# 1. 查看电影
# 2. 预订座位
# 3. 查看预订
# 4. 退出系统
# 请输入操作指令：1

# 电影时间表 >>>
# 《秋天的狸狸》
# 2026-09-12：14:00，18:00
# 《小珍珠的迷宫》
# 2026-09-12：16:00，20:00
# 1. 查看电影
# 2. 预订座位
# 3. 查看预订
# 4. 退出系统
# 请输入操作指令：2

# 请输入电影名称：秋天的狸狸
# 请输入日期（年-月-日）：2026-09-12
# 请输入时间（时:分）：18:00
# 请输入座位号（排数-座位号）：6-8
# 预订成功!
# 1. 查看电影
# 2. 预订座位
# 3. 查看预订
# 4. 退出系统
# 请输入操作指令：2

# 请输入电影名称：秋天的狸狸
# 请输入日期（年-月-日）：2026-09-12
# 请输入时间（时:分）：18:00
# 请输入座位号（排数-座位号）：6-9
# 预订成功!
# 1. 查看电影
# 2. 预订座位
# 3. 查看预订
# 4. 退出系统
# 请输入操作指令：3

# 请输入电影名称：秋天的狸狸
# 请输入日期（年-月-日）：2026-09-12
# 请输入时间（时:分）：18:00
# 预订的座位：
# 6排，8号
# 6排，9号
# 1. 查看电影
# 2. 预订座位
# 3. 查看预订
# 4. 退出系统
# 请输入操作指令：4
# 感谢使用，再见。






































