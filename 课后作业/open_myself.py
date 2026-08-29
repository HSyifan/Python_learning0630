# 打开自己
f = open(__file__, "r", encoding="utf-8")
# 读取内容
content = f.read()
# 关闭文件
f.close()
# 打印
print(content)
