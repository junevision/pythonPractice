# coding: utf-8
# Author: Mingjun Lei

# 可通过调试（Debug）功能来看每一步的执行（点击最左一列加断点）
for i in range(0, 10, 2):
    if i < 7:
        print("Loop", i)
    else:
        continue
    print("hehe......")