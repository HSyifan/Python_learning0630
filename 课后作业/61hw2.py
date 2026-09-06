# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-213950-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

from pathlib import Path
from time import strftime, localtime

class File:
    def __init__(self, name, size, folder, ctime, mtime, atime):
        self.name = name
        self.size = size
        self.folder = folder
        self.ctime = ctime
        self.mtime = mtime
        self.atime = atime

    def get_name(self):
        return self.name

    def get_size(self):
        return f"{self.size} 字节"

    def get_folder(self):
        return f"位置：{self.folder}"
        
    def get_ctime(self):
        return f"创建时间：{strftime('%Y-%m-%d %H:%M:%S', localtime(self.ctime))}"

    def get_mtime(self):
        return f"修改时间：{strftime('%Y-%m-%d %H:%M:%S', localtime(self.mtime))}"

    def get_atime(self):
        return f"访问时间：{strftime('%Y-%m-%d %H:%M:%S', localtime(self.atime))}"


def get_file_msg(path):
    p = Path(path)
    paths = []
    files = []
    
    # 利用glob()函数找出指定路径下的所有文件
    for each in p.glob("**/*"):
        paths.append(each)
        if each.is_file():
            name = each.name
            size = each.stat().st_size
            folder = each.parent.resolve()
            ctime = each.stat().st_ctime
            mtime = each.stat().st_mtime
            atime = each.stat().st_atime
            files.append(File(name, size, folder, ctime, mtime, atime))

    print("路径结构如下：")
    for each in paths:
        print(each)

    return files


def match_file(files):
    count = 0
    filename = input("\n请输入想要搜索的文件名：")
    for each in files:
        if filename in each.name:
            count += 1
            print(f"\n找到相关文件（{count}）-> {each.get_name()}（{each.get_size()}）")
            print(each.get_folder())
            print(each.get_ctime())
            print(each.get_mtime())
            print(each.get_atime())
    else:
        print("找不到相关文件！")
            

files = get_file_msg("target")
match_file(files)

