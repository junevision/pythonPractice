# coding: utf-8
# Author: Mingjun Lei

s = "你好"
print(s)
s_gbk = s.encode("gbk")
print(s_gbk)
print(s.encode())

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("utf-8", gbk_to_utf8)