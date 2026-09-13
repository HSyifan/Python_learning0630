# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-215775-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) fishc.com.cn All rights reserved

from pathlib import Path

class FileManager:
    def __init__(self, path="."):
        self.path = Path(path)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def __setattr__(self, attr, value):
        if attr == "path":
            object.__setattr__(self, attr, value)
        else:
            setattr(self, attr, value)

    def __delattr__(self, attr):
        if hasattr(self, attr):
            object.__delattr__(self, attr)
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def browse(self):
        for entry in self.path.iterdir():
            print(entry.name)

    def create(self, file_name):
        file_path = self.path / file_name
        if not file_path.exists():
            file_path.touch()
        else:
            print(f"文件 '{file_name}' 已存在。")

    def delete(self, file_name):
        file_path = self.path / file_name
        if file_path.is_file():
            file_path.unlink()
        elif file_path.is_dir():
            for child in file_path.glob('*'):
                self.delete(child.relative_to(self.path))
            file_path.rmdir()
        else:
            print(f"文件 '{file_name}' 未找到。")

    def rename(self, old_name, new_name):
        old_path = self.path / old_name
        new_path = self.path / new_name
        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)
        else:
            print(f"错误：'{old_name}' 不存在或 '{new_name}' 已存在。")
