# coding=utf-8
# Author: Mingjun Lei


# num = int(input("输入一个数字："))
# if (num % 2) == 0:
#     print("{0} 是偶数".format(num))
# else:
#     print("{0} 是奇数".format(num))

######################################################################

while True:
    try:
        num = int(input("请输入一个整数："))        # 判断输入是否为整数
    except ValueError:                           # 不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
    break


