# coding: utf-8
# Author: Mingjun Lei

# 列表用法
names = ["ZhangYang", "GuYun", "XiangPeng", "XuLiangChen"]

# 插入数据的方法
names.append("LeiHaiDong")  # 在列表最后追加一条数据
names.insert(1, "ChenRongHua")  # 在列表第二个数据前插入数据

# 修改数据的方法
names[2] = "XieDi"  # 把列表的第三个数据替换
print(names)

# 查询数据的方法
# print(names[0])   # 把列表第一个元素取出
# print(names[1:3])   # 范围切片 (顾头不顾尾，起始包含、结束不包含)
# print(names[-1])   # 切片（把倒数第一个元素取出）
# print(names[-2])   # 切片 （把倒数第二个元素取出）
# print(names[-2:])  # 切片 （把最后两个元素取出）
# print(names[:3])  # 切片 （把开头三个元素取出）

#delete 删除数据的方法
# names.remove("ChenRongHua")   # 指定删除某一个值
# del names[1]   # 删除列表某个位置的值
# names.pop()  # 删除列表最后一个位置的值
# names.pop(1)  # 删除列表某个位置的值
# print(names)

# 通过索引找到目标数据的位置
# print(names.index("XieDi"))
# print(names[names.index("XieDi")])  # 找到位置后输出目标数据的值

# 统计有重复的目标数据的数量
# print(names.count("ChenRongHua"))

# 清空列表
# names.clear()

#  将列表的值反转（倒序）
# names.reverse()

#  将列表按照ASCLL码排序（优先级高到低：特殊符号、数字、大写、小写）
# names.sort()

# 合并两个列表
names2 = [1, 2, 3, 4]
names.extend(names2)
del names2  # 删除列表names2
print(names, names2)
