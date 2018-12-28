# coding: utf-8
# Author: Mingjun Lei

# 参数组


def test(*args):
    print(args)

test(1, 2, 3, 4, 5, 6)
test(*[1, 2, 3, 4])   # 变成一个元组
