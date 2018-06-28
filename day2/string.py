# coding: utf-8
# Author: Mingjun Lei

name = "my name is {name} alex.com"

print(name.capitalize())  # 首字母大写
print(name.count('a'))  # 统计name里面的a出现的次数
print(name.center(50, '-'))  # 打印50个字符串，把name的内容放到中间，其余的用'-'补全
print(name.endswith('.com'))  # 判断是否以XXX结尾，例如可以判断邮箱是否以".com"结尾，返回true或false
print(name[name.find('name'):])  # find,找到的话返回索引，找不到返回-1；字符串也可以切片
print(name.format(name='john'))  # 格式化
print(name.format_map({'name': 'tom'}))  # 字典类型的格式化
