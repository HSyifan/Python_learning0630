"""路径处理"""
from pathlib import Path
p = Path.cwd()
print(p) # D:\Python_learning_260630

# 路径拼接
q = p / "54永久储存II.py"
print(q) # D:\Python_learning_260630\54永久储存II.py

# 判断路径是否文件夹
print(p.is_dir()) # True
print(q.is_dir()) # False

# 判断路径是否为文件
print(p.is_file()) # False
print(q.is_file()) # True

# 判断路径是否存在
print(p.exists()) # True
print(q.exists()) # True

print(p.name) # Python_learning_260630
print(q.name) # 54永久储存II.py

# 获取文件后缀
print(q.suffix) # .py

# 获取父路径
print(p.parent) # D:\

# 获取逻辑祖先构成的不可变序列
qs = q.parents
for each in qs:
    print(each) 
# D:\Python_learning_260630
# D:\
print(qs[0]) # D:\Python_learning_260630
print(qs[1]) # D:\

# 将路径各个部分拼接成元组
print(q.parts) # ('D:', 'Python_learning_260630', '54永久储存II.py')

# 查询文件或者文件夹的状态信息（尺寸、修改时间、创建时间等）
print(p.stat()) # os.stat_result(st_mode=16895, st_ino=2533274790734960, st_dev=6121126946959814220, st_nlink=1, st_uid=0, st_gid=0, st_size=28672, st_atime=1788089016, st_mtime=1788087926, st_ctime=1782756950)
print(p.stat().st_size) # 28672

# 相对路径转换为绝对路径
print(Path("./doc")) # doc
print(Path("./doc").resolve()) # D:\Python_learning_260630\doc

# 遍历目录下的文件和文件夹
# print(p.iterdir())
# for each in p.iterdir():
#     print(each)

# 将当前目录下的文件建一个列表
# print(list(x for x in p.iterdir() if x.is_file()))

# mkdir()创建文件夹
# n = p / "FishC"
# n.mkdir()
# print(n.exists()) # True
# # n.mkdir() # FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'FishC'
# n.mkdir(exist_ok=True)

n = p / "FishC/A/B/C"
# 创建多级文件夹
n.mkdir(parents=True, exist_ok=True) # FileNotFoundError: [WinError 3] 系统找不到指定的路径

# 创建文件
n = n / "test.txt"
print(n) # D:\Python_learning_260630\FishC\A\B\C\test.txt 
f = n.open("w")
f.write("I love FishC.")
f.close()

# 给文件或者文件夹修改名字
# n.rename("NewFishC.txt")

m = Path("NewFishC.txt")
print(m) # NewFishC.txt
print(n)
n.replace(m)

# 删除文件夹
# n.parent.rmdir()
# n.unlink() # 不然会报错文件夹不为空

# glob() 查找当前目录下的文件
p = Path('.')
p.glob("*txt")
# print(list(p.glob("*txt"))) # [WindowsPath('NewFishC.txt'), WindowsPath('课后作业+FishC.txt'), WindowsPath('课后作业+FishD.txt')]

# 查找当前目录下的下一级目录中的某类文件
# print(list(p.glob("*/*.py")))

# 查找当前目录下的所有子目录
# print(list(p.glob("**/*.py")))


# 动动手2：请编写代码，使用 pathlib 模块，在判断当前路径是否为文件夹类型，如果是则在路径末尾追加一个 FishC.txt（比如当前路径是 C:/Users，追加后的路径是 C：/Users/FishC.txt）
dds2 = Path('.')
if dds2.is_dir():
    dds2 = dds2 / "FishC.txt"
    print(dds2.resolve()) # D:\Python_learning_260630\FishC.txt

# 动动手4：请编写代码，使用 pathlib 模块，列举出当前目录下的所有文件的尺寸。
# print("当前路径：", Path.cwd())
# for each in p.iterdir():
#     if each.is_file():
#         print("文件名：", each.name, "文件尺寸：", each.stat().st_size, "字节")


# 动动手5：请编写代码，使用 pathlib 模块，列举出当前目录下的所有文件的修改时间。
# import time
# print("当前路径：", Path.cwd())
# for each in p.iterdir():
#     if each.is_file():
#         print("文件名：", each.name, "修改时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(each.stat().st_mtime)))


# 动动手6：请编写代码，使用 pathlib 模块，获取指定路径（文件夹）中所有的文件名，并按文件尺寸按从小到大进行排序。
# dds6_list = []
# for each in p.iterdir():
#     if each.is_file():
#         dds6_list.append((each.name, each.stat().st_size))
#         dds6_list.sort(key=lambda x: x[1])
        
# for each in dds6_list:
#             print(each[0], "(", each[1], "字节)")


# 动动手7：将上一题的代码转换成一句话代码（不包含模块导入语句）。
print(sorted([x for x in p.iterdir() if x.is_file()], key=lambda x: x.stat().st_size))

# 地狱模式答案：
print('\n'.join([f"{g.name} ({g.stat().st_size}字节)" for g in sorted([f for f in Path.cwd().iterdir() if f.is_file()], key=lambda t:t.stat().st_size)]))

# 动动手8：请编写代码，使用 pathlib 模块，找出指定路径（文件夹）中最后被修改的文件。
import time
dds8_list = []
for each in p.iterdir():
    if each.is_file():
        dds8_list.append((each.name, each.stat().st_mtime))
        dds8_list.sort(key=lambda x: x[1])

print("修改时间 ->", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(dds8_list[-1][1])), "文件名", dds8_list[-1][0])


# 动动手9：将上一题的代码转换成一句话代码实现（不包含模块导入语句），要求实现结果一致。
print("修改时间 ->", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sorted([x for x in p.iterdir() if x.is_file()], key=lambda x: x.stat().st_mtime)[-1].stat().st_mtime)), "文件名", sorted([x for x in p.iterdir() if x.is_file()], key=lambda x: x.stat().st_mtime)[-1].name)
# 更简洁写法：
# f = max((x for x in p.iterdir() if x.is_file()), key=lambda x: x.stat().st_mtime)
# print("修改时间 ->", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f.stat().st_mtime)), "文件名", f.name)




















 