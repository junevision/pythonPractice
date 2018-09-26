# coding: utf-8
# Author: Mingjun Lei

# f = open("yesterday2", "r", encoding="utf-8")
with open("yesterday2", "r", encoding="utf-8") as f, \
     open("yesterday2", "r", encoding="utf-8") as f2:
    # print(f.readline())
    for line in f:
        print(line)
    for line2 in f2:
        print(line2)