"""with语句和上下文管理器"""
# 传统打开文件方式：
# f = open("FishC.txt", "w")
# f.write("I love FishC.")
# f.close()

# with语句打开文件：
# with open("FishC.txt", "w") as f:
#     f.write("I love FishC.")
    # 1/0 # 报错，with语句还是能执行写入

# pickle() 允许将字符串，列表，字典保存为文件的形式   
import pickle
# x, y, z = 1, 2, 3
# s = "FishC"
# l = ["小甲鱼", 520, 3.14]
# d = {"one":1, "two":2}

# with open("data.pkl", "wb") as f:
#     pickle.dump(x, f)
#     pickle.dump(y, f)
#     pickle.dump(z, f)
#     pickle.dump(s, f)
#     pickle.dump(l, f)
#     pickle.dump(d, f)

# 打包成元组
# with open("data.pkl", "wb") as f:
#     pickle.dump((x, y, z, s, l, d), f)
# with open("data.pkl", "rb") as f:
#     x, y, z, s, l, d = pickle.load(f)

# with open("data.pkl", "rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)
#     z = pickle.load(f)
#     s = pickle.load(f)
#     l = pickle.load(f)
#     d = pickle.load(f)

# print(x, y, z, s, l, d, sep="\n")


# 动动手0：在 pathlib 模块中，Path 对象有一个 glob() 方法，它提供了向下递归搜索的能力（如下），请自己编写一个递归函数，实现相同的搜索功能？
from pathlib import Path

def dds0_glob(p, result=None):
    if result is None:
        result = []

    for each in p.iterdir():
        if each.is_file():
            if each.suffix == ".py":
                result.append(each)
        elif each.is_dir():
            dds0_glob(each)
    return result

p = Path.cwd()
# print(dds0_glob(p))


# 动动手1：请下载附件（target.zip，自动统计该文件夹中的 Python 总代码行数。
# A. 其中包含的子文件夹，也需要一并统计入内
# B. 空行不能算
# C. 本题的源代码不统计入内
# 提示2：如果是 windows 系统，打开带中文文件，可能会引发编码错误，此时在 open() 函数中使用 errors="ignore" 参数来避免该问题

dds1_p = Path(r"D:\Python_learning_260630\课后作业\target")

def dds1_glob_lines(p, count=None):
    if count is None:
        count = 0

    for each in p.iterdir():
        if each.is_file():
            if each.suffix == ".py":
                with open(each, "r", errors="ignore") as f:
                    r = f.read().splitlines()
                    for line in r:
                        if line.strip() != "":
                            count += 1
        elif each.is_dir():
            count = dds1_glob_lines(each, count)
    return count

# print(dds1_glob_lines(dds1_p)) # 88


# 动动手2：请编写一个源代码文件，其功能就是在当前文件夹下创建 10 个子文件夹，每个子文件夹下又放入自身的 10 个拷贝。
# 在文件夹 p 里，递归创建 n 个「本文件」的拷贝：0.py ~ (n-1).py
def dds2_create_files(p, n):
    if n == 0:
        return # 递归结束
    # __file__：当前这个 .py 自己的路径；一次 with 打开两个文件（读自己 + 写拷贝）
    with open(__file__, "r", encoding="utf-8") as f1, open(p / f"{n-1}.py", "w", encoding="utf-8") as f2:
        f2.write(f1.read())
    dds2_create_files(p, n - 1)  # 还剩 n-1 个，继续创建

# 在当前目录下，递归创建 n 个子文件夹：0 ~ (n-1)，每个里面放 10 份拷贝
def dds2_create_dirs(p, n):
    if n == 0:
        return # 递归结束
    each = p / str(n - 1)       # 新文件夹路径，如 .../9、.../8 ...
    each.mkdir(exist_ok=True)   # 已存在也不报错
    dds2_create_files(each, 10) # 这个文件夹里放 10 个拷贝
    dds2_create_dirs(p, n - 1)  # 再去建下一个文件夹

# dds2_create_dirs(Path.cwd(), 10)  # 需要运行时再取消注释（会在当前目录生成 0~9 共 10 个文件夹）

































































