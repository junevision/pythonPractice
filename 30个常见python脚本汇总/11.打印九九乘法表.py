# coding=utf-8
# Author: Mingjun Lei

for i in range(1, 10):
    for j in range(1, i+1):
        # print('%d x %d = %d \t'%(j, i, i*j), end='') # 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行
        print('{}x{}={}\t'.format(j,i,i*j), end='')
    print()

