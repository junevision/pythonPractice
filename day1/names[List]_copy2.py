# coding: utf-8
# Author: Mingjun Lei

import copy

person = ["name", ["a", 100]]
# copy的三种用法
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)

print(p1)
print(p2)
print(p3)