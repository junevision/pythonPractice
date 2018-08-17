# coding: utf-8
# Author: Mingjun Lei

# 集合：无序、去重

list_1 = [1, 4, 5, 7, 3, 6, 7, 9]  # 需去重
list_1 = set(list_1)  # 设为集合

list_2 = set([66, 22, 4, 6, 88])
print(list_1, list_2)

# 关系测试，交集
print(list_1.intersection(list_2))
# 并集（合起来，然后去重）
print(list_1.union(list_2))
# 差集（list1有，而list2没有的）
print(list_1.difference(list_2))
# 对称差集（把list1和list2都没有的，取出来）
print(list_1.symmetric_difference(list_2))

list_3 = set([1, 5, 7])
# 子集
print(list_3.issubset(list_1))  # list_3是list_1的子集
# 父集
print(list_1.issuperset(list_3))  # list_1是list_3的父集

print("-------------------------------")
list_4 = set([2, 8])
print(list_1.isdisjoint(list_4))  # 如果两个集合没有交集，则返回true
