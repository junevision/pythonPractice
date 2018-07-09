# coding: utf-8
# Author: Mingjun Lei

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

while True:
    for i in menu:
        print(i)

    choice = input("选择进入>>：")
    if choice in menu:
        while True:
            for i2 in menu[choice]:
                print("\t", i2)
                choice2 = input("选择进入>>：")
                if choice2 in menu[choice]:
                    while True:
                        for i3 in menu[choice2]:
                            print("\t", i3)
