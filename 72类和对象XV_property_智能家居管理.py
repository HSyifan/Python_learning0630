"""property：把 get/set/del 按固定顺序绑上，让方法能写成属性样子"""
# property(读, 写, 删) → 顺序固定
# c.x / c.x=.. / del c.x 分别走第1、2、3个函数
# 外面叫什么：看左边名字（x = property(...)）或 @property 下的函数名
# return / 函数体：只决定「被叫到之后干什么」，不决定外面叫什么
# 数据通常放 _x；只传读 = 只读；工作里用这个，少用 __setattr__/__getattr__


# ========== 1. property(读, 写, 删) ==========
class C:
    def __init__(self):
         self._x = 250
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx)  # 左：外面名；右：读、写、删

c = C()
print(c.x) # 250
c.x = 520
print(c.__dict__) # {'_x': 520}
del c.x
print(c.__dict__) # {}


# ========== 2. __getattr__/__setattr__/__delattr__：也能做，但会管所有赋值，易递归 ==========
# 赋值必须 super().__setattr__，不能 self._x = ...
class D:
    def __init__(self):
        self._x = 250
    def __getattr__(self, name):
        if name == "x":
            return self._x
        else:
            super().__getattr__(name)
    def __setattr__(self, name, value):
        if name == "x":
            super().__setattr__('_x', value)
        else:
            super().__setattr__(name, value)
    def __delattr__(self, name):
        if name == "x":
            super().__delattr__('_x')
        else:
            super().__delattr__(name)

d = D()
print(d.x) # 250
d.x = 520
print(d.__dict__) # {'_x': 520}
del d.x
print(d.__dict__) # {}


# ========== 3. @property = 只绑读 → 只读；等同 x = property(x) ==========
class E:
    def __init__(self):
        self._x = 250
    @property
    def x(self):
        return self._x

e = E()
print(e.x) # 250
# e.x = 520 # 报错：没 setter


class E:
    def __init__(self):
        self._x = 250
    def x(self):
        return self._x
    x = property(x)  # 同上，只传了读

e = E()
# e.x = 520 / del e.x 都会报错


# ========== 4. @property + setter + deleter = 和 class C 一样 ==========
class E:
    def __init__(self):
        self._x = 250
    @property
    def bbby(self):          # 外面名跟函数名走 → e.bbby
        return self._x
    @bbby.setter
    def bbby(self, value):
        self._x = value
    @bbby.deleter
    def bbby(self):
        del self._x

e = E()
e.bbby = 520
print(e.__dict__) # {'_x': 520}


# 验证：del 走的是第3个参数位置，不是看函数里写了啥
class T:
    def __init__(self):
         self._x = 250
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def dddd(self):
        print("巴巴博一")
    x = property(getx, setx, dddd)

t = T()
del t.x # 巴巴博一



# 动动手0：编写一个基于智能家居系统的设备管理程序。
# 需要实现一个智能家居系统（SmartHomeSystem），该系统能够管理多种类型的设备，
# 包括灯（Light）、空调（AirConditioner）和安全摄像头（SecurityCamera）。
# 每种设备都有特定的属性和方法，用于控制和查询设备状态。
# 设备类（Device）：
# - 每个设备都有一个名称（name）和一个状态（status），状态表示设备是否开启。
# - 状态属性是可读写的，修改状态时应输出设备的当前状态。
# 灯类（Light）继承自 Device：
# - 具有亮度属性（brightness），亮度是一个整数值。
# - 设置亮度时，自动将设备状态设为开启，并输出当前亮度值。
# 空调类（AirConditioner）继承自Device：
# - 具有温度属性（temperature），温度是一个整数值。
# - 设置温度时，自动将设备状态设为开启，并输出当前温度值。
# 安全摄像头类（SecurityCamera）继承自 Device：
# - 具有录制状态属性（recording），表示摄像头是否开启录制。
# - 设置录制状态时，如果检测到设备未开启，则无法录制并抛出 DeviceNotOnError 异常。
# 智能家居系统类（SmartHomeSystem）：
# - 能够添加设备（add_device）。
# - 能够删除设备（remove_device），如果设备不存在，抛出 DeviceNotFoundError 异常。
# - 能够获取设备（get_device），如果设备不存在，抛出 DeviceNotFoundError 异常。


class DeviceNotOnError(Exception):
    pass

class DeviceNotFoundError(Exception):
    pass

class Device:
    def __init__(self, name, status=False):
        self.name = name
        self._status = status          # 要 init；用 _status 避免走 setter 打印
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
        print(f"[{self.name}] 的开启状态为：{self._status}")

class Light(Device):
    def __init__(self, name, status=False, brightness=0):
        super().__init__(name, status)
        self._brightness = brightness  # 要 init；不走 setter
    @property
    def brightness(self):
        return self._brightness
    @brightness.setter
    def brightness(self, value):
        if not isinstance(value, int):
            raise TypeError("亮度必须是整数")
        self._brightness = value
        self.status = True
        print(f"[{self.name}] 的亮度设置为：{self._brightness}")

class AirConditioner(Device):
    def __init__(self, name, status=False, temperature=0):
        super().__init__(name, status)
        self._temperature = temperature
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if not isinstance(value, int):
            raise TypeError("温度必须是整数")
        self._temperature = value
        self.status = True
        print(f"[{self.name}] 的温度设置为：{self._temperature}")

class SecurityCamera(Device):
    def __init__(self, name, status=False, recording=False):
        super().__init__(name, status)
        self._recording = recording
    @property
    def recording(self):
        return self._recording
    @recording.setter
    def recording(self, value):
        if not self.status:
            raise DeviceNotOnError(f"[{self.name}] 未开启，无法录制")
        self._recording = value
        print(f"[{self.name}] 的录制状态设置为：{self._recording}")

class SmartHomeSystem:
    def __init__(self):
        self.devices = []
    def add_device(self, device):
        self.devices.append(device)
        print(f"设备 [{device.name}] 已添加。")
    def remove_device(self, name):
        for device in self.devices:
            if device.name == name:
                self.devices.remove(device)
                return
        raise DeviceNotFoundError(f"没有找到设备 [{name}]")
    def get_device(self, name):
        for device in self.devices:
            if device.name == name:
                return device
        raise DeviceNotFoundError(f"没有找到设备 [{name}]")



home_system = SmartHomeSystem()
light = Light("客厅灯光", brightness=50)
airconditioner = AirConditioner("客厅空调", temperature=22)
camera = SecurityCamera("前门摄像头", recording=True)

home_system.add_device(light)
home_system.add_device(airconditioner)
home_system.add_device(camera)

light.brightness = 75
airconditioner.temperature = 24
camera.status = True  # 没有这一句的话应该抛出异常
camera.recording = True
light.status = False

try:
    home_system.remove_device("厨房灯光")
except DeviceNotFoundError as e:
    print(e)


###################################
# 设备 [客厅灯光] 已添加。
# 设备 [客厅空调] 已添加。
# 设备 [前门摄像头] 已添加。
# [客厅灯光] 的开启状态为：True
# [客厅灯光] 的亮度设置为：75
# [客厅空调] 的开启状态为：True
# [客厅空调] 的温度设置为：24
# [前门摄像头] 的开启状态为：True
# [前门摄像头] 的录制状态设置为：True
# [客厅灯光] 的开启状态为：False
# 没有找到设备 [厨房灯光]







