# coding: utf-8
# Author: Mingjun Lei

def logger():
    with open('a.txt', 'a+') as f:
        f.write('end action')

def test1():
    print('test1 starting action...')
    logger()

def test2():
    print('test2 starting action...')
    logger()

def test3():
    print('test3 starting action...')
    logger()

test1()
test2()
test3()