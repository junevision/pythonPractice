# coding: utf-8
# Author: Mingjun Lei

name = "my name is {name} ALEX.com"

print(name.capitalize())  # 将字符串的第一个字母变成大写,其他字母变小写
print(name.count('a'))  # 统计字符串里某个字符出现的次数
print(name.center(50, '-'))  # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
print(name.endswith('.com'))  # 判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False.例如可以判断邮箱是否以".com"结尾
print(name[name.find('name'):])  # 检测字符串中是否包含子字符串str,找到的话返回索引，找不到返回-1；字符串也可以切片
print(name.format(name='john'))  # 格式化
print(name.format_map({'name': 'tom'}))  # 字典类型的格式化，很少用

# 可用作判断，断言

print("ab12".isalnum())  # 是否阿拉伯字母或数字
print("abA".isalpha())  # 检测字符串是否只由字母组成
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
print(name.lower())  # 大写转换成小写
print(name.upper())  # 小写转换成大写
print('\nAlex\n'.lstrip())  # 截掉字符串左边的空格或指定字符
print('-----------')
print('\nAlex\n'.rstrip())  # 截掉字符串右边的空格或指定字符
print('-----------')
print('       Alex\n'.strip())  # 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

# Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 注：两个字符串的长度必须相同，为一一对应的关系。
p = str.maketrans("abcdefg", '123456#')
print('I am a dog'.translate(p))


