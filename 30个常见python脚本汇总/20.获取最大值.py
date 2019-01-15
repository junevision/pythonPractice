# coding=utf-8
# Author: Mingjun Lei

# N = int(input('输入需要对比大小数字的个数：'))        # 列表的数目
# print("请输入需要对比的数字：")
# num = []                                         # 定义一个空列表
# for i in range(1, N+1):                          # 循环体里往列表里存放或追加所输入的数字
#     temp = int(input('输入第 %d 个数字：' % i))
#     num.append(temp)
#
# print('您输入的数字为：', num)                     # 输出数字列表
# print('最大值为：', max(num))                     # 输出数字列表里的最大值

################################################################################

N = int(input('输入需要对比大小数字的个数：\n'))

num = [int(input('请输入第 %d 个对比数字：\n'%i))for i in range(1, N+1)]

print('您输入的数字为：', num)
print('最大值为：', max(num))


