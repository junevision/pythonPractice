# coding: utf-8
# Author: Mingjun Lei
import getpass

_username = "alex"
_password = "123456"
username = input("username:")
password = input("password:")
# password = getpass.getpass("password:")  # 密码为密文，用cmd命令行执行
if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))  # 格式化输出
else:
    print("Invalid username or password!")
