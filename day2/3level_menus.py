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

#  这里需要注意的是，代码行的对齐，否则逻辑容易报错

exit_flag = False
while not exit_flag:
    for i in menu:
        print(i)            # 打印一级菜单的所有选项，例如“北京”等
    choice = input("选择进入1>>：")     # 选择其中一个进入
    if choice in menu:
        while not exit_flag:
            for i2 in menu[choice]:
                print("\t", i2)             # 打印二级菜单的所有选项，例如“海淀”等
            choice2 = input("选择进入2>>：")     # 选择其中一个进入
            if choice2 in menu[choice]:
                while not exit_flag:
                    for i3 in menu[choice][choice2]:
                        print("\t\t", i3)                   # 打印三级菜单的所有选项，如“五道口”等
                    choice3 = input("选择进入3>>：")     # 选择其中一个进入
                    if choice3 in menu[choice][choice2]:
                        for i4 in menu[choice][choice2][choice3]:
                            print("\t\t", i4)               # 打印三级菜单的内容，如“五道口”
                        choice4 = input("最后一层，按b返回，按q退出>>：")
                        if choice4 == 'b':
                            pass                            # 返回上一级
                        elif choice4 == 'q':
                            exit_flag = True                # 退出循环，程序结束
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True

