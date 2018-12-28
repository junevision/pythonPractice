# coding: utf-8
# Author: Mingjun Lei

# 默认参数特点：调用函数的时候，默认参数非必须传递
# def test(x, y=2):
#     print(x)
#     print(y)
#
# test(1)

# 用途：1.默认安装值
def setup(x, soft1=True, soft2=True):
    print(x)

setup(1)

# 2.数据库，设置端口号
# def conn(host, port=3306):
#     pass

# conn()

