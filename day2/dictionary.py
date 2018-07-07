# coding: utf-8
# Author: Mingjun Lei

# dict是无序的
# key必须是唯一的,so 天生去重
# key尽量不要写中文，可能导致编码取不出来

# tv_catalog = {
#     "欧美": {
#         "www.google.com": ["很多免费的,世界最大的", "质量一般"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
#         "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
#     },
#     "日韩": {
#         "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
#     },
#     "大陆": {
#         "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
#     }
# }
# tv_catalog["大陆"]["1024"][1] = "可以在国内做镜像"  # 把字典里的值替换
# tv_catalog.setdefault("台湾", {"www.taiwan.com": ["钓鱼岛是中国的"]})  # 和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
# print(tv_catalog)

################################################################################
# key-value 键-值
info = {
    'stu1101': 'Messi',
    'stu1102': 'Christiano Ronaldo',
    'stu1103': 'Neymar',
}
info1 = {
    'stu1102': 'Alex',
    1: 2,
    3: 4,
}
info.update(info1)  # update() 函数把字典dict2的键/值对更新到dict里。
print(info)
print(info.items())  # items() 函数以列表返回可遍历的(键, 值) 元组数组。

for i in info:                 # 通过索引方式，循环打印出字典里的键-值，更高效（推荐）
    print(i, info[i])

for k, v in info.items():      # 用字典转换成列表的方式，耗时费内存（不推荐）
    print(k, v)

# print(info.get('stu1104'))  # 获取查找，如无该值会返回none（比较稳妥的写法）
# print('stu1104' in info)  # 查找值，如果有就返回true，没有就返回false

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
