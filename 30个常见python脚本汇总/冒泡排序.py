# coding=utf-8
# Author: Mingjun Lei

list = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]

def sortport():
    for i in range(len(list)-1):   # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(list)-1-i):      # j为列表下标
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)
    return list

sortport()