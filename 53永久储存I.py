# 写入文件
f = open("FishC.txt", "w")
f.write("I love Python.")

f.writelines(["I love FishC.\n", "I love my wife."])

f.close()

# 又可以写入，又可以读取
f = open("FishC.txt", "r+")
print(f.readable()) # True
print(f.writable()) # True

for each in f:
    print(each)

print(f.read()) 

# # 获取当前文件指针的位置
# print(f.tell()) # 44

# print(f.seek(0))
# print(f.readline()) # I love Python.I love FishC.
# print(f.read()) # I love my wife.

# f.write("I love my WIFI.")
# # 刷新缓冲区，将缓冲区中的数据写入文件
# f.flush()

# # 截断文件，只保留前29个字符
# f.truncate(29) 
# f.close()

# # 截断，删除文件内容
# # f = open("FishC.txt", "w")
# # f.close()

# f = open("FishC.txt", "a")
# f.write("add mode, choose a")
# f.close()

# # print(f.readline(size = 3))

# # 练习题：
# f = open("FishC.txt", "w")
# f.writelines(["FishA", "FishB", "FishC"])
# f.close()
# # FishAFishBFishC

# f = open("D:\Python_learning_260630\FishC.txt", "w")
# f.write("FishA\nFishB\nFishC")


# 动动手0：编写代码，截取其中第 10~15 个字符，并保存为新文件（FishD.txt）。
# FishAFishBFishCFishDFishE
# dds0 = open("D:\Python_learning_260630\课后作业\FishC.txt", "r")
# # for each in dds0:
# #     print(each)
# content = dds0.read()
# dds0.close()

# segment = content[9:15]
# fd = open("D:\Python_learning_260630\课后作业\FishD.txt", "w")
# fd.write(segment)
# fd.close()


# 动动手1：还是上一题的那个文件（FishC.txt），这次请编写代码，截取前面 15 个字符，并保存覆盖保存原文件。
dds0 = open("D:\Python_learning_260630\课后作业\FishC.txt", "r+")
dds0.truncate(15)
dds0.close()


# 动动手2：请编写一个源代码（open_myself.py），它的功能就是打开自己的源文件，然后打印出来。
# # 打开自己
# f = open(__file__, "r", encoding="utf-8")
# # 读取内容
# content = f.read()
# # 关闭文件
# f.close()
# # 打印
# print(content)


# 动动手3：在图片中隐藏文件（又叫图片隐写术）的原理及实现。
# 需求：在日常生活中，我们可能需要将一些小文件隐藏起来，比如将种子文件隐藏到封面图片中，这样只需要提供图片，通过解密就可以得到相应的种子文件。这项技术就叫做图片隐写术~
# 原理：很简单，只需直接将压缩文件的内容，追加写入到图片文件的尾部即可。
# 我们编写代码，将两个文件打开，并将压缩文件的所有内容追加到 test.jpg 文件的尾部。
# 得到的 test.jpg 图片就是两个文件合并的结果，此时图片依旧可以正常打开：
# 不过它已经被我们动过手脚了，只要将 test.jpg 的文件名修改为 test.zip，那么我们就得到了一个隐藏的压缩文件：

test = open(r"D:\Python_learning_260630\课后作业\test.jpg", "ab") # 追加写入
target = open(r"D:\Python_learning_260630\课后作业\test.zip", "rb") # 读取二进制文件

target_content = target.read()
test.write(target_content)
test.close()
target.close()
print("done")


































