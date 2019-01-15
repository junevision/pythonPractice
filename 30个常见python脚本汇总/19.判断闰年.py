# coding=utf-8
# Author: Mingjun Lei


# year = int(input("输入一个年份："))
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
#         else:
#             print("{0} 不是闰年".format(year))
#     else:
#         print("{0} 是闰年".format(year))   # 非整百年能被4整除的为闰年
# else:
#     print("{0} 不是闰年".format(year))


###############################################################################


# year = int(input("请输入一个年份："))
# if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
#     print("{0} 是闰年".format(year))
# else:
#     print("{0} 不是闰年".format(year))


###############################################################################


import calendar

year = int(input("请输入一个年份："))
check_year = calendar.isleap(year)
if check_year == True:
    print("%d是闰年"% year)
else:
    print("%d是平年"% year)