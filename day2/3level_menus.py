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
    for i in menu:       # 打印一级菜单，例如“北京”
        print(i)

    choice = input("选择进入1>>：")     # 选择其中一个进入
    if choice in menu:
        while True:
            for i2 in menu[choice]:         # 打印二级菜单，例如“海淀”
                print("\t", i2)
                choice2 = input("选择进入2>>：")     # 选择其中一个进入
                if choice2 in menu[choice]:
                    while True:
                        for i3 in menu[choice][choice2]:       # 打印三级菜单，如“五道口”
                            print("\t\t", i3)
                            choice3 = input("选择进入3>>：")     # 选择其中一个进入
                            if choice3 in menu[choice][choice2]:
                                for i4 in menu[choice][choice2][choice3]:       # 打印三级菜单，如“五道口”
                                    print("\t\t", i4)
                                choice4 = input("最后一层，按b返回>>：")
                                if choice4 == 'b':
                                    pass
                            if choice3 == 'b':
                                break
                if choice2 == 'b':
                    break

