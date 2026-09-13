from pathlib import Path

class FileManager:
    def __init__(self, path="."):
        self.path = Path(path)

    def __getattr__(self, attr):
        if attr == 'size':
            return self.get_size()
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def __setattr__(self, attr, value):
        if attr == "path":
            object.__setattr__(self, attr, Path(value))
        else:
            object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        if hasattr(self, attr):
            object.__delattr__(self, attr)
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def get_size(self, file_name=None):
        if file_name:
            file_path = self.path / file_name
            if file_path.is_file():
                return file_path.stat().st_size
            else:
                raise FileNotFoundError(f"文件 '{file_name}' 未找到。")
        else:
            total_size = 0
            for entry in self.path.glob('**/*'):
                if entry.is_file():
                    total_size += entry.stat().st_size
            return total_size

    def browse(self, recursive=False, sort_by=None, reverse=False):
        try:
            if recursive:
                for entry in sorted(self.path.glob('**/*'), key=sort_by, reverse=reverse):
                    print(entry.relative_to(self.path))
            else:
                for entry in sorted(self.path.iterdir(), key=sort_by, reverse=reverse):
                    print(entry.name)
        except Exception as e:
            print(f"浏览文件时出错: {e}")

    def create_file(self, file_name):
        try:
            file_path = self.path / file_name
            if not file_path.exists():
                file_path.touch()
            else:
                print(f"文件 '{file_name}' 已存在。")
        except Exception as e:
            print(f"创建文件时出错: {e}")

    def create_directory(self, dir_name):
        try:
            dir_path = self.path / dir_name
            if not dir_path.exists():
                dir_path.mkdir(parents=True)
            else:
                print(f"文件夹 '{dir_name}' 已存在。")
        except Exception as e:
            print(f"创建文件夹时出错: {e}")

    def delete(self, file_name):
        try:
            file_path = self.path / file_name
            if file_path.is_file():
                file_path.unlink()
            elif file_path.is_dir():
                for child in file_path.glob('*'):
                    self.delete(child.relative_to(self.path))
                file_path.rmdir()
            else:
                print(f"文件 '{file_name}' 未找到。")
        except Exception as e:
            print(f"删除文件时出错: {e}")

    def rename(self, old_name, new_name):
        try:
            old_path = self.path / old_name
            new_path = self.path / new_name
            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)
            else:
                print(f"错误: '{old_name}' 未找到 或 '{new_name}' 已存在。")
        except Exception as e:
            print(f"重命名文件时时出错: {e}")

    def search(self, pattern):
        try:
            for entry in self.path.glob(f"**/{pattern}"):
                print(entry.relative_to(self.path))
        except Exception as e:
            print(f"搜索文件时出错: {e}")


def main():
    fm = FileManager()
    while True:
        try:
            command = input("输入命令（1.浏览/2.创建文件/3.创建文件夹/4.删除/5.重命名/6.搜索/7.退出）：")
            if command == "1":
                recursive = input("递归浏览? (y/n): ").lower() == "y"
                fm.browse(recursive=recursive)
            elif command == "2":
                file_name = input("输入文件名: ")
                fm.create_file(file_name)
            elif command == "3":
                dir_name = input("输入文件夹名: ")
                fm.create_directory(dir_name)
            elif command == "4":
                file_name = input("输入文件或文件夹名: ")
                fm.delete(file_name)
            elif command == "5":
                old_name = input("输入旧文件或文件夹名: ")
                new_name = input("输入新文件或文件夹名: ")
                fm.rename(old_name, new_name)
            elif command == "6":
                pattern = input("输入搜索模式: ")
                fm.search(pattern)
            elif command == "7":
                break
            else:
                print("无效命令，请重试。")
        except KeyboardInterrupt:
            print("中断。退出。")
            break
        except Exception as e:
            print(f"错误: {e}")

main()
