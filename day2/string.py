# coding: utf-8
# Author: Mingjun Lei

name = "my name is {name} alex.com"

print(name.capitalize())  # 首字母大写
print(name.count('a'))  # 统计name里面的a出现的次数
print(name.center(50, '-'))  # 打印50个字符串，把name的内容放到中间，其余的用'-'补全
print(name.endswith('.com'))  # 判断是否以XXX结尾，例如可以判断邮箱是否以".com"结尾，返回true或false
print(name[name.find('name'):])  # find,找到的话返回索引，找不到返回-1；字符串也可以切片
print(name.format(name='john'))  # 格式化
print(name.format_map({'name': 'tom'}))  # 字典类型的格式化，很少用

# 可用作判断，断言

print("ab12".isalnum())  # 是否阿拉伯字母或数字
print("abA".isalpha())  # 是否纯数字
print("14444".isdecimal())  # 是否十进制数字
print("333".isdigit())  # 是否是整数
print("A1a".isidentifier())  # 是否是一个合法的标识符（变量）
print("a".islower())  # 是否小写
print(" ".isspace())  # 是否空格
print("This Is Me".istitle())  # 是否标题（每个首字母大写）
print("AAABCD".isupper())  # 是否大写
print('+'.join(['1', '2', '3']))  # 用‘+’来连接串起列表里的每一个元素
print(name.ljust(50, '*'))  # 保证有50个字符串，从左边开始填充，不足的用*补齐
print(name.rjust(50, '-'))  # 保证有50个字符串，从右边开始填充，不足的用-补齐



