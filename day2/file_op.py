# coding: utf-8
# Author: Mingjun Lei

# data = open("yesterday", encoding="utf-8").read()  # 由于Windows系统默认是gbk编码打开，所以要转换为python的编码打开
# f = open("yesterday2", 'w', encoding="utf-8")  # 文件句柄，只写，且会刷掉原来的内容，重新创建内容
# f = open("yesterday2", 'r', encoding="utf-8")  # 文件句柄，只读
f = open("yesterday2", 'a', encoding="utf-8")  # 文件句柄，在原文信息后，继续追加信息

f.write("\n天安门上太阳升，\n")
f.write("东方升起西边落。\n")

f.close()


