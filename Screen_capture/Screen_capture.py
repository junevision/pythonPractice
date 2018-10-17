# coding: utf-8
# Author: Mingjun Lei

from time import sleep
from PIL import ImageGrab

m = int(input("请输入想抓屏几分钟："))
m = m * 30
n = 1
while n < m:
    sleep(0.1)
    im = ImageGrab.grab()
    local = (r"%s.jpg" % (n))
    im.save(local, 'jpeg')
    n = n + 1