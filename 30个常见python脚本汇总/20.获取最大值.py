# coding=utf-8
# Author: Mingjun Lei

N = int(input('输入需要对比大小数字的个数：'))
print("请输入需要对比的数字：")
num = []
for i in range(1,N+1):                          # 循环体里往集合里存放或追加所输入的数字
    temp = int(input('输入第 %d 个数字：' % i))
    num.append(temp)

print('您输入的数字为：',num)                     # 输出数字集合
print('最大值为：',max(num))                     # 输出数字群里的最大值