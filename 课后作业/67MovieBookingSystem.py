# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-215530-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

# 定义电影院类
class Cinema:
    def __init__(self, name):
        self.name = name
        self.movies = {}

    # 添加电影和播放时间
    def add_movie(self, movie_name, schedule):
        self.movies[movie_name] = schedule

    # 显示所有电影及其播放时间
    def show_movies(self):
        for movie_name, schedule in self.movies.items():
            print(f"{movie_name}")
            for date, times in schedule.items():
                print(f"  {date}: {', '.join(times)}")
        print()

# 定义座位类
class Seat:
    def __init__(self, row, number):
        self.row = row          # 座位所在的排数
        self.number = number    # 座位号
        self.reserved = False   # 标志一个座位是否被预定

    # 预定座位
    def reserve(self):
        if not self.reserved:
            self.reserved = True
        else:
            raise ValueError("该座位已被预定。")

# 定义电影预订系统类
class MovieBookingSystem:
    def __init__(self, cinema, rows, seats_per_row):
        self.cinema = cinema
        self.reservations = {}  # 存储预订信息的字典
        
        # 创建座位实例并存储到字典中
        self.seats = {f"{row+1}-{seat+1}": Seat(row+1, seat+1) for row in range(rows) for seat in range(seats_per_row)}

    # 预定座位
    def reserve_seat(self, movie_name, date, time, seat_id):
        key = (movie_name, date, time)  # 创建预订信息键值
        seat = self.seats.get(seat_id)  # 获取座位实例

        # 如果座位不存在，抛出异常
        if not seat:
            raise ValueError("无效的座位号。")

        # 如果预订信息不存在，创建新的预订信息
        if key not in self.reservations:
            self.reservations[key] = []

        # 如果座位未被预定，预定座位并添加到预订信息
        if seat not in self.reservations[key]:
            seat.reserve()
            self.reservations[key].append(seat)
        else:
            raise ValueError("该座位已被预定。")

    # 查看预订信息
    def view_reservation(self, movie_name, date, time):
        key = (movie_name, date, time)
        return self.reservations.get(key, [])

# 显示菜单
def display_menu():
    print("欢迎来到电影票订购系统")
    print("1. 查看电影")
    print("2. 预订座位")
    print("3. 查看预订")
    print("4. 退出系统")

# 获取用户输入
def user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n谢谢使用！")
        exit(0)

def main():
    # 创建电影院实例并添加电影
    cinema = Cinema("鱼C影院")
    cinema.add_movie("《小甲鱼的救赎》", {"2023-07-20": ["14:00", "18:00"]})
    cinema.add_movie("《不二如是的假日》", {"2023-07-20": ["16:00", "20:00"]})

    # 创建预订系统实例
    booking_system = MovieBookingSystem(cinema, 10, 10)

    while True:
        display_menu()
        choice = user_input("请输入操作指令：")

        # 查看电影
        if choice == "1":
            print("\n电影时间表 >>>")
            cinema.show_movies()

        # 预订座位
        elif choice == "2":
            movie_name = user_input("请输入电影名称：")
            date = user_input("请输入日期（年-月-日）：")
            time = user_input("请输入时间（时:分）：")
            seat_id = user_input("请输入座位号（排数-座位号）：")

            try:
                booking_system.reserve_seat(movie_name, date, time, seat_id)
                print("预订成功！\n")
            except ValueError as e:
                print(f"预订失败：{e}\n")

        # 查看预订
        elif choice == "3":
            movie_name = user_input("请输入电影名称：")
            date = user_input("请输入日期（年-月-日）：")
            time = user_input("请输入时间（时:分）：")

            reserved_seats = booking_system.view_reservation(movie_name, date, time)
            if reserved_seats:
                print("预订的座位：")
                for seat in reserved_seats:
                    print(f"{seat.row}排，{seat.number}号")
            else:
                print("没有预订的座位。")
            print()

        # 退出系统
        elif choice == "4":
            print("谢谢使用！")
            break

        # 无效选择处理
        else:
            print("无效选择，请输入1~4之间的数字。\n")

if __name__ == "__main__":
    main()
