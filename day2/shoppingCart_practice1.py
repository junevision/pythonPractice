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

productList = [
    ("Water", 5),
    ("Radio", 200),
    ("MP3", 480),
    ("Bike", 650),
    ("TV", 2500)
]

shoppingList = []

salary = input("请输入您的工资：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for item in productList:
            print(productList.index(item), item)
        user_choose = input("请输入你要购买的商品编号：")
        if user_choose.isdigit():
            user_choose = int(user_choose)
            if user_choose < len(productList) and user_choose >= 0:
                p_item = productList[user_choose]
                if p_item[1] <= salary:
                    salary -= p_item[1]
                    shoppingList.append(p_item)
                    print("您购买了%s号商品，现在还剩%s可消费" % (user_choose, salary))
                else:
                    print("您还剩%s可消费了，还买个锤子" % salary)
            else:
                print("无此商品！")
        elif user_choose == "q" or "Q":
            print("..........shoppint list............")
            for p in shoppingList:
                print(p)
            print("您的余额为\033[31;1m%s\033[0m" % salary)
            exit()
else:
    print("错误操作！")

