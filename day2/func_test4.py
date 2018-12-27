# coding: utf-8
# Author: Mingjun Lei


def test(x, y):
    print(x)
    print(y)

test(1, 2)  # 位置参数调用,与形参一一对应
test(x=1, y=2)  # 关键字调用，与形参顺序无关

# 形参——位置参数，实参