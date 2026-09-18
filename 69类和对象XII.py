"""切片"""
"""让自定义对象也能像列表、字典那样用 [] 取值、切片，以及用 for 遍历。"""
class C:
    def __getitem__(self, index):
        print(index)

c = C()
c[2] # 2
c[2:8] # slice(2, 8, None)

# 切片是 slice() 函数的语法糖
s = "I love FishC" 
print(s[2:6]) # "love"
print(s[slice(2, 6)]) # love

print(s[7:]) # "FishC"
print(s[slice(7, None)]) # FishC

class D:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value

d = D([1, 2, 3, 4, 5])
print(d[1]) # 2, 获取索引为1的元素

d[1] = 1
print(d[1]) # 1, 设置索引为1的元素为1
d[2:4] = [2, 3]
print(d[:]) # [1, 1, 2, 3, 5]

# for 语句访问__getitem__
class D:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index] * 2

d = D([1, 2, 3, 4, 5])
for i in d:
    print(i, end=" ") # 2 4 6 8 10


# 如果一个对象定义了iter方法，那这个对象就是一个可迭代对象
# 如果一个可迭代对象定义了next方法，那这个对象就是一个迭代器
# 列表是可迭代对象，但不是迭代器

X = [1, 1, 2, 3, 5]
# next(X) # TypeError: 'list' object is not an iterator

for i in X:
    print(i, end=" ") # 1 1 2 3 5

_ = iter(X)
while True:
    try:
        i = _.__next__()
    except StopIteration:
        break
    print(i, end=" ") # 1 1 2 3 5


class Double:
    def __init__(self, start, stop):
        self.value = start -1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value * 2

d = Double(1, 5)
for i in d:
    print(i, end=" ") # 2 4 6 8 10

print()
print(s[slice(2, 6, 2)]) # FishC
print(s[slice(None, None, -1)]) # FishC
print(s[slice(None, None, None)]) # C h s e v o l I


# 动动手0: 现在我们尝试来制作一个短链接生成工具
# （短链接让长 URL 变得更易分享、易记、易管理，并且能提供有关链接点击次数和其他有用的统计信息）。
# 要求实现的功能：
# a. 生成短链接（你可以用任意方法，只要确保不冲突即可）
# b. 存储 URL 映射（通过 __setitem__() 方法实现）
# c. 通过短链接获取长 URL（通过 __getitem__() 方法实现）
# d. 统计每个短链接被访问的次数
# e. 注意预防冲突的发生（即不同的 URL 恰巧生成了同一个短链接）
import random
import string

class ShortURL:
    def __init__(self):
        self.url_dict = {}      # 存储短链接和长链接的对应关系
        self.click_dict = {}    # 存储短链接的点击次数
        self.long_to_short = {} # 存储长链接到短链接的映射

    def __getitem__(self, short_url):
        # 当短链接被访问时，增加其点击次数，并返回对应的长链接
        if short_url in self.url_dict:
            self.click_dict[short_url] = self.click_dict.get(short_url, 0) + 1
            return self.url_dict[short_url]
        raise KeyError(f"短链接（{short_url}）不存在")

    def __setitem__(self, short_url, long_url):
        # 存储长链接和短链接的对应关系
        self.url_dict[short_url] = long_url

    def generate_short_url(self, long_url):
        # 如果长链接已存在，直接返回对应的短链接；否则，生成新的短链接
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]

        while True:
            # 生成一个随机的短链接，长度为8
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if short_url not in self.url_dict:
                break
        
        self.long_to_short[long_url] = short_url  # 存储长链接和新的短链接的对应关系
        return short_url

    def get_clicks(self, short_url):
        # 返回短链接的点击次数，如果短链接不存在，返回0
        return self.click_dict.get(short_url, 0)

def main():
    url_gen = ShortURL()

    long_url = "https://fishc.com.cn/thread-216104-1-1.html"
    short_url = url_gen.generate_short_url(long_url)
    print(f"短链接 -> {short_url}")

    url_gen[short_url] = long_url       # 存储短链接和长链接的对应关系
    redirect_url = url_gen[short_url]   # 通过短链接获取长链接
    print(f"{short_url} 被重定向到 -> ", redirect_url)

    # 模拟10次点击
    for _ in range(10):
        redirect_url = url_gen[short_url]

    print(f"短链接（{short_url}）被点击的次数：", url_gen.get_clicks(short_url))

if __name__ == "__main__":
    main()



# 动动手1：在上一个代码的基础上，让我们的短链接生成工具具备迭代功能，从而可以使用 for 语句遍历其所存储的链接映射。
# 小甲鱼这里将映射存储放在外部实现，主要是为了考察大家对 __setitem__() 方法场景的应用是否熟悉。
# 实际开发的话建议把映射存储放在 generate_short_url() 函数中一并实现即可。
# 另外，使用随机数生成的方式来创建短链接存在一些无法预测的问题。
# 在实际的开发中，更常见的做法是使用一种能够生成唯一 ID 的算法（比如哈希算法），然后再将这个唯一 ID 转换为一个短字符串。
# 这样可以确保每个长链接都能得到一个唯一的短链接，并且可以按照一定的规则生成短链接（有兴趣的鱼油也可以进行尝试，原理掌握之后基本就是换汤不换药的勾当，不难的）。

import random
import string

class ShortURL:
    def __init__(self):
        self.url_dict = {}      # 存储短链接和长链接的对应关系
        self.click_dict = {}    # 存储短链接的点击次数
        self.long_to_short = {} # 存储长链接到短链接的映射

    def __getitem__(self, short_url):
        # 当短链接被访问时，增加其点击次数，并返回对应的长链接
        if short_url in self.url_dict:
            self.click_dict[short_url] = self.click_dict.get(short_url, 0) + 1
            return self.url_dict[short_url]
        raise KeyError(f"短链接（{short_url}）不存在")

    def __setitem__(self, short_url, long_url):
        # 存储长链接和短链接的对应关系
        self.url_dict[short_url] = long_url

    def __iter__(self):
        # 生成_keys和_current_key_index，为下方迭代器做准备
        self._keys = list(self.url_dict.keys())
        self._current_key_index = 0
        return self

    def __next__(self):
        # 实现迭代操作的细节，这样for语句就是找到怎么找到下一个元素了
        if self._current_key_index < len(self._keys):
            short_url = self._keys[self._current_key_index]
            long_url = self.url_dict[short_url]
            self._current_key_index += 1
            return (short_url, long_url)
        raise StopIteration

    def generate_short_url(self, long_url):
        # 如果长链接已存在，直接返回对应的短链接；否则，生成新的短链接
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]

        while True:
            # 生成一个随机的短链接，长度为8
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if short_url not in self.url_dict:
                break
        
        self.long_to_short[long_url] = short_url  # 存储长链接和新的短链接的对应关系
        return short_url

    def get_clicks(self, short_url):
        # 返回短链接的点击次数，如果短链接不存在，返回0
        return self.click_dict.get(short_url, 0)

def main():
    url_gen = ShortURL()

    long_url1 = "https://fishc.com.cn/forum-173-1.html"
    short_url1 = url_gen.generate_short_url(long_url1)
    url_gen[short_url1] = long_url1

    long_url2 = "https://fishc.com.cn/forum-360-1.html"
    short_url2 = url_gen.generate_short_url(long_url2)
    url_gen[short_url2] = long_url2

    long_url3 = "https://fishc.com.cn/thread-216104-1-1.html"
    short_url3 = url_gen.generate_short_url(long_url3)
    url_gen[short_url3] = long_url3

    for short_url, long_url in url_gen:
        print(f"短链接：{short_url} -> 长链接：{long_url}")

if __name__ == "__main__":
    main()

