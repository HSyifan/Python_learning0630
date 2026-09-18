# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-216103-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

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
