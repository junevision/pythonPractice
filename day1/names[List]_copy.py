# coding: utf-8
# Author: Mingjun Lei
import copy

# 列表中copy的用法
names = ["ZhangYang", "GuYun", "ChenRonghua", "XiangPeng", ["alex", "jack"], "XuLiangChen"]
# 跳着间隔切片
print(names[0:-1:2])
# 列表循环
for i in names:
    print(i)

# names2 = copy.copy(names)  # 浅copy，只copy第一层
names2 = copy.deepcopy(names)  # 深copy, 完全克隆，完全独立（谨慎使用，占两份内存空间）

print(names)
print(names2)

names[3] = "向鹏"
names[4][0] = "ALEX"
print(names)
print(names2)

# 直接赋值：其实就是对象的引用（别名）。
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

