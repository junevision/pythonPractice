# coding: utf-8
# Author: Mingjun Lei

# 程序：购物车程序
#
# 需求:
#
# 1.启动程序后，让用户输入工资，然后打印商品列表
# 2.允许用户根据商品编号购买商品
# 3.用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4.可随时退出，退出时，打印已购买商品和余额

goodsLists = [
    ["Starbucks Coffee", 35],
    ["Bike", 320],
    ["iPad", 3050],
    ["iPhone", 6800],
    ["MacBook", 12800]
]                                   # 产品列表
shoppingLists = []                  # 放到购物车里的商品
salary = input("Please enter your salary:")     # 输入工资
if salary.isdigit():                # 如果输入的工资是整数，转换为整型
    salary = int(salary)
    while True:                     # 循环开始
        for index, item in enumerate(goodsLists):  # enumerate在for循环中得到计数的用法，enumerate参数为可遍历的变量
            # print(goodsLists.index(item), item)       # 利用列表的下标，打出产品编号
            print(index, item)
        user_choice = input("选择你要买的商品编号：")
        if user_choice.isdigit():                       # 如果输入的是数字编号，则转换为整型
            user_choice = int(user_choice)
            if user_choice < len(goodsLists) and user_choice >=0:    # 如果输入的数字编号在列表范围内
                p_item = goodsLists[user_choice]                      # 定位到当前产品
                if p_item[1] <= salary:             # 定位到产品的价格，工资大于产品价格，则买得起
                    salary -= p_item[1]                # 扣款
                    shoppingLists.append(p_item)    # 放入购物车
                    print("Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("\033[32;1m你的余额只剩%s了，还买个毛线！\033[0m" % salary)  # 高亮输出格式
            else:
                print("你选择的 \033[31;1m%s\033[0m 对应的商品不存在！" % user_choice)
        elif user_choice == "q" or "Q":                         # 输入q退出购物
            print("----------shopping list--------------")
            for p in shoppingLists:                         # 打印出购物车里所有的商品
                print(p)
            print("你的余额还剩 \033[31;1m%s\033[0m" % salary)
            exit()
        else:
            print("invalid option!")




