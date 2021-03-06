# coding: utf-8
# Author: Mingjun Lei


def test(x, y):
    print(x)
    print(y)

test(1, 2)  # 位置参数调用,与形参一一对应
test(x=1, y=2)  # 关键字调用，与形参顺序无关

# 形参——位置参数，形式参数，不是实际存在，是虚拟变量，在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参
# 实参：实际参数，调用函数时传给函数的参数，可以是常量，变量，表达式，函数，传给形参
# 区别：形参是虚拟的，不占用内存空间，形参变量只有在被调用时才会分配内存单元；实参是一个变量，占用内存空间，数据传送单向，实参传给形参，不能形参传给实参
# 关键参数不能写在位置参数前面
