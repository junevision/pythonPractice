# coding=utf-8
# Author: Mingjun Lei

a = 0
b = 1
while b < 1000:
    print(b, end=',')  # end 可以将print输出到同一行并以 ,号结尾
    a, b = b, a+b

