# coding=utf-8
# Author: Mingjun Lei

dict1 = {"A":"a","B":"b","C":"c"}
dict2 = {y:x for x,y in dict1.items()}

print(dict2)