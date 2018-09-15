# coding: utf-8
# Author: Mingjun Lei

import sys, time

for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()  # 实时刷到硬盘上，而不会先放到缓存，等缓存满了再放到内存
    time.sleep(0.1)
