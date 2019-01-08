# coding=utf-8
# Author: Mingjun Lei

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
    return sum

calc(1, 2, 3)