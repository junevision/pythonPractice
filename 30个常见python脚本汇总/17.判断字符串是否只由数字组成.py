# coding=utf-8
# Author: Mingjun Lei

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# print(chri.isdigit())           # 检测字符串是否只由数字组成
# print(chri.isnumeric())         # 检测字符串是否只由数字组成，这种方法是只针对Unicode对象

