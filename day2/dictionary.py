# coding: utf-8
# Author: Mingjun Lei

# key-value 键-值
info = {
    'stu1101': 'Messi',
    'stu1102': 'Christiano Ronaldo',
    'stu1103': 'Neymar',
}

# dict是无序的
# key必须是唯一的,so 天生去重

print(info.get('stu1104'))  # 获取查找，如无该值会返回none

# print(info)  # 输出字典所有的值
# print(info['stu1101'])  # 通过键输出值
# info['stu1101'] = '梅西'  # 修改值
# print(info)
# info['stu1104'] = 'Ronaldo'  # 如键-值不存在，则会新增创建一条
# print(info)
# del info['stu1101']  # 删除键值方法1
# print(info)
# info.pop('stu1104')  # 删除键值方法2
# print(info)
# info.popitem()  # 随机删一个
# print(info)
