"""私有变量"""
# 使对象中的属性或方法无法被外部所访问的机制

class C:
    def __init__(self, x):
        self.__x = x # 表示__x是私有变量，不能被外部访问
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x

c = C(250)
# print(c.__x) # 报错，因为__x是私有变量，不能被外部访问

print(c.get_x()) # 250
c.set_x(520)
print(c.get_x()) # 520

print(c.__dict__) # {'__x': 520}

print(c._C__x) # 520

class D:
    def __fun(self):
        print("Hello FishC.")

d = D()
d._D__fun() # Hello FishC.

# 名字改变发生在类实例化对象的时候
c.__y = 250
print(c.__dict__) # {'_C__x': 520, '__y': 250}

# _单个下横线开头的变量：表示保护变量，只能被类内部访问，不能被外部访问
# 单个下横线结尾的变量_：

# 动态创建属性
class C:
    def __init__(self, x):
        self._x = x

c = C(250)
print(c._x) # 250
print(c.__dict__) # {'_x': 250}

c.y = 520
print(c.__dict__) # {'_x': 250, 'y': 520}

c.__dict__['z'] = 666
print(c.__dict__) # {'_x': 250, 'y': 520, 'z': 666}
print(c.z) # 666

"""__slots__, 限制类实例化对象的属性"""

class C:
    __slots__ = ['x', 'y']
    def __init__(self, x):
        self.x = x

c = C(250)
print(c.x) # 250
c.y = 520
print(c.y) # 520

# c.z = 666 # 报错，因为__slots__中没有z

class D:
    __slots__ = ['x', 'y']
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# d = D(3, 4, 5) # 报错，因为__slots__中没有z


# 继承自父类的__slots__属性是不会在子类中起作用的
class E(C):
    pass

e = E(520)
print(e.x) # 520
e.y = 520
e.z = 666
print(e.__slots__) # ('x', 'y')
print(e.__dict__) # {'z': 666}

 
# 练习题：
# class C:
#     __slots__ = ['x']
       
# c = C()
# c.x = 520
# print(c.__dict__) # {'x': 520}
# # 请问这里会打印什么内容？


class C:
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
class D(C):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
       
d = D(3, 4, 5)
print(d.__dict__) # {'z': 5}
# 请问这里会打印什么内容？


class C:
    pass
class D(C):
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y
d = D(3, 4)
d.z = 5
print(d.__dict__) # {'z': 5}
# D继承了父类C的__dict__属性，所以可以动态创建属性


# 动动手0：请按要求编写一个汽车租赁系统。
# 汽车类：
# a. 车型分类：经济车型（EconomyCar）、豪华车（LuxuryCar）、跑车（SportCar）、SUV（SUV）
# b. 车辆通用属性：品牌（brand）、星号（model）、车牌（platenum）、每天租金（dayrent）、车辆编号（carid）
# c. 车辆通用方法：
# - get_brand() -- 获取品牌
# - get_model() -- 获取型号
# - get_platenum() -- 获取车牌
# - get_dayrent() -- 获取每天租金
# - get_carid() -- 获取车辆编号
# - calc_rent() -- 通过租赁天数和折扣计算一共需要多少租金
# d. 不同车型的特殊属性和方法：
# - 经济车型享有额外的补贴优惠
# - 豪华车需要增加保险费用
# - 跑车需要增加损耗费用
# - SUV 如果租车时间大于 7 天，原有折扣的基础上再打 7 折
# 业务类：
# a. 属性：
# - cars -- 字典类型，用于绑定车辆编号和相应的对象
# - stocks -- 字典类型，用于存放每一种车型的库存
# b. 方法：
# - operate() -- 程序入口，获取并分发指令
# - register() -- 录入汽车
# - get_stock() -- 获取库存
# - rent_car() -- 租车服务
# - return_car() -- 还车服务


class Car:
    """车辆公共父类：四种车型平级继承"""
    def __init__(self, brand, model, platenum, dayrent, carid):
        self.brand = brand
        self.model = model
        self.platenum = platenum
        self.dayrent = dayrent
        self.carid = carid

    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model
    def get_platenum(self):
        return self.platenum
    def get_dayrent(self):
        return self.dayrent
    def get_carid(self):
        return self.carid
    def calc_rent(self, days):
        return self.dayrent * days

class EconomyCar(Car):
    def __init__(self, brand, model, platenum, dayrent, carid, bonus):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.__bonus = bonus  # 私有：日补贴
    def get_bonus(self):
        return self.__bonus
    def calc_rent(self, days):
        # (日租 - 日补贴) * 天数
        return (self.dayrent - self.__bonus) * days

class LuxuryCar(Car):
    def __init__(self, brand, model, platenum, dayrent, carid, insurance):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.__insurance = insurance
    def get_insurance(self):
        return self.__insurance
    def calc_rent(self, days):
        # (日租 + 保险) * 天数
        return (self.dayrent + self.__insurance) * days

class SportCar(Car):
    def __init__(self, brand, model, platenum, dayrent, carid, damage):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.__damage = damage
    def get_damage(self):
        return self.__damage
    def calc_rent(self, days):
        # (日租 + 损耗) * 天数
        return (self.dayrent + self.__damage) * days

class SUV(Car):
    def __init__(self, brand, model, platenum, dayrent, carid, discount=0.7):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.__discount = discount
    def get_discount(self):
        return self.__discount
    def calc_rent(self, days):
        return super().calc_rent(days) * self.__discount if days > 7 else super().calc_rent(days)


class CarOperation:
    def __init__(self):
        self.cars = {}
        self.rented = {}  # 已租出的车：{编号: 车对象}，还车时再放回 cars
        # 各车型库存
        self.stocks = {'1': 0, '2': 0, '3': 0, '4': 0}
        # 各车型下一辆可用编号
        self.next_ids = {
            '1': 10000,  # 经济车
            '2': 20000,  # 豪华车
            '3': 30000,  # 跑车
            '4': 40000,  # SUV
        }

    def _input_int(self, tip):
        while True:
            try:
                return int(input(tip))
            except ValueError:
                print("输入不合法，请重新输入")

    def _input_float(self, tip):
        while True:
            try:
                return float(input(tip))
            except ValueError:
                print("输入不合法，请重新输入")

    def operate(self):
        print("欢迎使用鱼C汽车租赁系统")
        while True:
            ins = input("1.录入汽车;2.租车服务;3.还车服务;4.退出程序：")
            if ins == '1':
                self.register()
            elif ins == '2':
                self.rent_car()
            elif ins == '3':
                self.return_car()
            elif ins == '4':
                print("感谢使用鱼C汽车租赁系统")
                break
            else:
                print("输入不合法，请重新输入")

    car_type_map = {
        '1': EconomyCar,
        '2': LuxuryCar,
        '3': SportCar,
        '4': SUV
    }
    car_type_name = {
        '1': '经济车型',
        '2': '豪华车',
        '3': '跑车',
        '4': 'SUV'
    }

    def get_car_info(self, cls):
        for car in self.cars.values():
            if type(car) is not cls: # eg：如果当前实例car的类型不是economy这个类造出来的，则跳过
                continue
            base = (f"车辆编号：{car.get_carid()}，品牌：{car.get_brand()}，"
                    f"型号：{car.get_model()}，日租金：{car.get_dayrent()}")
            if cls is EconomyCar:
                extra = f" - {car.get_bonus()}(补贴)元"
            elif cls is LuxuryCar:
                extra = f" + {car.get_insurance()}(保险)元"
            elif cls is SportCar:
                extra = f" + {car.get_damage()}(损耗)元"
            else:  # SUV
                extra = f" * {car.get_discount()}(折扣)元"
            print(base + extra)

    def get_stock(self):
        print(f"1. 经济车型（享有补贴），共有{self.stocks['1']}辆")
        self.get_car_info(EconomyCar)
        print(f"2. 豪华车（需额外购买保险），共有{self.stocks['2']}辆")
        self.get_car_info(LuxuryCar)
        print(f"3. 跑车（需增加损耗费用），共有{self.stocks['3']}辆")
        self.get_car_info(SportCar)
        print(f"4. SUV（租赁超过7天，享有额外折上7折优惠），共有{self.stocks['4']}辆")
        self.get_car_info(SUV)

    def _type_key(self, car):
        """根据对象真实类型，反查 stocks 里的键 '1'/'2'/'3'/'4'"""
        for key, cls in self.car_type_map.items():
            if type(car) is cls:
                return key
        return None

    def register(self):
        ins = input("1.经济车型;2.豪华车;3.跑车;4.SUV：")
        if ins not in self.car_type_map:
            print("输入不合法，请重新输入")
            return
        car_num = self._input_int("请输入需要录入的数量：")
        cls = self.car_type_map[ins]
        for i in range(car_num):
            print(f"请输入第{i+1}辆车")
            brand = input("品牌：")
            model = input("型号：")
            platenum = input("车牌：")
            dayrent = self._input_float("租金：")
            carid = self.next_ids[ins]  # 自动分配编号，不用手动输入
            # 按车型录入特殊属性
            if ins == '1':
                bonus = self._input_float("补贴：")
                car = cls(brand, model, platenum, dayrent, carid, bonus)
            elif ins == '2':
                insurance = self._input_float("保险：")
                car = cls(brand, model, platenum, dayrent, carid, insurance)
            elif ins == '3':
                damage = self._input_float("损耗：")
                car = cls(brand, model, platenum, dayrent, carid, damage)
            else:  # SUV 无额外录入项
                car = cls(brand, model, platenum, dayrent, carid)

            self.cars[carid] = car
            self.stocks[ins] += 1          # 每录一辆，库存 +1
            self.next_ids[ins] += 1        # 每录一辆，该车型编号 +1
        print(f"成功录入{car_num}辆车！")

    def rent_car(self):
        self.get_stock()
        car_id = self._input_int("请输入需要租赁的车辆编号：")
        if car_id not in self.cars:
            print("输入不合法，请重新输入")
            return
        car = self.cars[car_id]
        days = self._input_int("请输入需要租赁的天数：")
        rent = car.calc_rent(days)
        print(f"租赁{days}天，总共需要花费：{rent}元")
        print("恭喜，租赁成功~")
        key = self._type_key(car)
        self.stocks[key] -= 1
        # 从可租字典里删掉，库存列表才会变少；还车时再放回来
        self.rented[car_id] = self.cars.pop(car_id)

    def return_car(self):
        car_id = self._input_int("请输入需要还车的车辆编号：")
        if car_id not in self.rented:
            print("输入不合法，请重新输入")
            return
        car = self.rented.pop(car_id)
        key = self._type_key(car)
        self.stocks[key] += 1
        self.cars[car_id] = car
        print("恭喜，还车成功~")
        self.get_stock()


main = CarOperation()
main.operate()


#######################################################
# 录入车辆测试：
# 欢迎使用鱼C汽车租赁系统
# 1.录入汽车;2.租车服务;3.还车服务;4.退出程序：1
# 1.经济车型;2.豪华车;3.跑车;4.SUV：1
# 请输入需要录入的数量：3
# 请输入第1辆车
# 品牌：大众
# 型号：宝来
# 车牌：A238279
# 租金：80
# 补贴：10
# 请输入第2辆车
# 品牌：丰田
# 型号：卡罗拉
# 车牌：A289172
# 租金：120
# 补贴：20
# 请输入第3辆车
# 品牌：本田
# 型号：飞度
# 车牌：A672891
# 租金：100
# 补贴：10
# 成功录入3辆车！
# 1.录入汽车;2.租车服务;3.还车服务;4.退出程序：1
# 1.经济车型;2.豪华车;3.跑车;4.SUV：2
# 请输入需要录入的数量：1
# 请输入第1辆车
# 品牌：2
# 型号：奥迪A6
# 车牌：A791028
# 租金：488
# 保险：20
# 成功录入1辆车！
# 1.录入汽车;2.租车服务;3.还车服务;4.退出程序：1
# 1.经济车型;2.豪华车;3.跑车;4.SUV：3
# 请输入需要录入的数量：1
# 请输入第1辆车
# 品牌：宝马
# 型号：Z4
# 车牌：A792843
# 租金：688
# 损耗：50
# 成功录入1辆车！

###################################################################
# 租车和还车测试：
# 1.录入汽车;2.租车服务;3.还车服务;4.退出程序：2
# 1. 经济车型（享有补贴），共有3辆
# 车辆编号：10000，品牌：大众，型号：宝来，日租金：80.0 - 10.0(补贴)元
# 车辆编号：10001，品牌：丰田，型号：卡罗拉，日租金：120.0 - 20.0(补贴)元
# 车辆编号：10002，品牌：本田，型号：飞度，日租金：100.0 - 10.0(补贴)元
# 2. 豪华车（需额外购买保险），共有1辆
# 车辆编号：20000，品牌：2，型号：奥迪A6，日租金：488.0 + 20.0(保险)元
# 3. 跑车（需增加损耗费用），共有1辆
# 车辆编号：30000，品牌：宝马，型号：Z4，日租金：688.0 + 50.0(损耗)元
# 4. SUV（租赁超过7天，享有额外折上7折优惠），共有0辆
# 请输入需要租赁的车辆编号：10001
# 请输入需要租赁的天数：3
# 租赁3天，总共需要花费：300.0元
# 恭喜，租赁成功~
# 1.录入汽车;2.租车服务;3.还车服务;4.退出程序：2
# 1. 经济车型（享有补贴），共有2辆
# 车辆编号：10000，品牌：大众，型号：宝来，日租金：80.0 - 10.0(补贴)元
# 车辆编号：10002，品牌：本田，型号：飞度，日租金：100.0 - 10.0(补贴)元
# 2. 豪华车（需额外购买保险），共有1辆
# 车辆编号：20000，品牌：2，型号：奥迪A6，日租金：488.0 + 20.0(保险)元
# 3. 跑车（需增加损耗费用），共有1辆
# 车辆编号：30000，品牌：宝马，型号：Z4，日租金：688.0 + 50.0(损耗)元
# 4. SUV（租赁超过7天，享有额外折上7折优惠），共有0辆
# 请输入需要租赁的车辆编号：20000
# 请输入需要租赁的天数：5
# 租赁5天，总共需要花费：2540.0元
# 恭喜，租赁成功~
# 1.录入汽车;2.租车服务;3.还车服务;4.退出程序：3
# 请输入需要还车的车辆编号：10001
# 恭喜，还车成功~
# 1. 经济车型（享有补贴），共有3辆
# 车辆编号：10000，品牌：大众，型号：宝来，日租金：80.0 - 10.0(补贴)元
# 车辆编号：10002，品牌：本田，型号：飞度，日租金：100.0 - 10.0(补贴)元
# 车辆编号：10001，品牌：丰田，型号：卡罗拉，日租金：120.0 - 20.0(补贴)元
# 2. 豪华车（需额外购买保险），共有0辆
# 3. 跑车（需增加损耗费用），共有1辆
# 车辆编号：30000，品牌：宝马，型号：Z4，日租金：688.0 + 50.0(损耗)元
# 4. SUV（租赁超过7天，享有额外折上7折优惠），共有0辆


































































































































