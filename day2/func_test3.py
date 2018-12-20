# coding: utf-8
# Author: Mingjun Lei

def test1():
    print('in the test1')
    return 0
    print('test end')

def test2():
    print('in the test2')
    return 0

def test3():
    print('in the test3')
    return 0, 'hello', ['a', 'b', 'c'], {'name': 'alex'}

def test4():
    print('in the test4')
    return test3

x = test1()
y = test2()
z = test3()
a = test4()
print(x)
print(y)
print(z)
print(a)

# 1.返回值=0：返回none
# 2.返回值=1：返回object
# 3.返回值>1：返回tuple元组
# 4.返回值=函数/高阶函数：返回内存地址