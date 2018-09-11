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

print("-------------------------------")
list_3 = set([1, 5, 7])
# 子集
print(list_3.issubset(list_1))  # list_3是list_1的子集
# 父集
print(list_1.issuperset(list_3))  # list_1是list_3的父集

list_4 = set([2, 8])
print(list_1.isdisjoint(list_4))  # 如果两个集合没有交集，则返回true

print("-------------------------------")
# 交集
print(list_1 & list_2)
# 并集 union
print(list_2 | list_1)
# 差集 difference
print(list_1 - list_2)  # in list_1 but not in list_2
# 对称差集
print(list_1 ^ list_2)

list_1.add(999)  # 无序添加一项
print(list_1)
list_1.update([888, 777, 666])  # 无序添加多项
print(list_1)
list_1.remove(7)  # 删除一项（天生去重，不存在有重复的值）
print(list_1)
print(len(list_1))  # 集合的长度

print(list_1.pop())  # 随机删除一个集合的元素
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())

list_1.discard(999)  # 删除；删除一个不是集合的元素返回none，不会报错
print(list_1)
