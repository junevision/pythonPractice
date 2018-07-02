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

tv_catalog = {
    "欧美": {
        "www.google.com": ["很多免费的,世界最大的", "质量一般"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

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
