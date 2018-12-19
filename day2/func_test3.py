# coding: utf-8
# Author: Mingjun Lei

def test1():
    print('in the test1')
    return 0
    print('test end')

def test2():
    return 0

def test3():
    return 0, 'hello', ['a', 'b', 'c'], {'name': 'alex'}

x = test1()
y = test2()
z = test3()

print(x)
print(y)
print(z)
