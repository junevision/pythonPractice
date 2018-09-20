# coding: utf-8
# Author: Mingjun Lei

# data = open("yesterday", encoding="utf-8").read()  # 由于Windows系统默认是gbk编码打开，所以要转换为python的编码打开

# f = open("yesterday2", 'r', encoding="utf-8")  # 文件句柄，只读
# print(f.tell())  # 打印光标
# print(f.readline()) # 打印一行
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(15)
# print(f.readline())
# print(f.tell())
# print(f.encoding)  # 打印编码格式

# f = open("yesterday", 'a', encoding="utf-8")  # 文件句柄，在原文信息后，继续追加信息
# f.truncate(10)  # 从头开始截取第N位
# f.close()

# f = open("yesterday", 'w', encoding="utf-8")  # 文件句柄，只写，且会刷掉原来的内容，重新创建内容
# f.write("Hello 1\n")
# f.flush()  # 实时刷到硬盘上，而不会先放到缓存，等缓存满了再放到内存
# f.write("Hello 2\n")
# f.flush()
# f.write("Hello 3\n")
# f.flush()
# f.close()

# f = open("yesterday2", 'r+', encoding="utf-8")  # 文件句柄，读写，先读取文件，然后在最末尾处写入内容
# f = open("yesterday2", 'w+', encoding="utf-8")  # 文件句柄，写读，先创建一个文件再写，然后再读（没什么用）
# f = open("yesterday2", 'a+', encoding="utf-8")  # 文件句柄，追加读写
# f = open("yesterday2", 'rb', encoding="utf-8")  # 文件句柄，二进制读文件
f = open("yesterday2", 'wb')  # 文件句柄，二进制写文件
f.write("Hello binary\n".encode())
f.close()

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.write("-------------well done-------------------")

# f.write("-------------well done-------------------\n")
# f.write("-------------well done-------------------\n")
# f.write("-------------well done-------------------\n")
# f.write("-------------well done-------------------\n")
# print(f.tell())
# f.seek(10)
# print(f.tell())
# print(f.readline())
# f.write("should be at the beginning of the second line")
# f.close()


