# coding=utf-8
# Author: Mingjun Lei

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print(s)
    return s

power(2, 20)