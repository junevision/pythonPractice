# coding: utf-8
# Author: Mingjun Lei

import copy

person = ["name", ["saving", 100]]
# copy的三种用法
# p1 = copy.copy(person)
# p2 = person[:]
# p3 = list(person)
# print(p1)
# print(p2)
# print(p3)

# 浅copy适用于联合账号
p1 = person[:]
p2 = person[:]

p1[0] = 'alex'
p2[0] = 'fengjie'

p1[1][1] = '50'

print(p1)
print(p2)