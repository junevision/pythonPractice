# coding: utf-8
# Author: Mingjun Lei
import getpass

_username = "alex"
_password = "abcd1234"
for count in range(1, 4):
    username = input("username:")
    password = input("password:")
    # password = getpass.getpass("password:")  # 密码为密文，用cmd命令行执行
    if _username == username and _password == password:
        print("Welcome user {name} login...".format(name=username))  # 格式化输出
        break
    else:
        print("Invalid username or password!")
else:
    print("You have entered wrong username or password three times, the account is locked.")
