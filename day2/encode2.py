
import sys
print(sys.getdefaultencoding())
Author = "Mingjun Lei"

s = "你好呀"
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s)
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))