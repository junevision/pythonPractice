# coding=utf-8
# Author: Mingjun Lei

def fac():
    num = int(input("请输入一个数字："))
    factorial = 1

# 查看数字是负数，0或正数
    if num < 0:
        print("抱歉，负数没有阶乘！")
    elif num == 0:
        print("0的阶乘是1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("%d 的阶乘是 %d" % (num, factorial))

fac()