# coding=utf-8
# Author: Mingjun Lei

import os


def print_dir(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath, i)
        if os.path.isdir(path):
            print_dir(path)
        if path.endswith(".html"):
            print(path)

filepath = "D:/UploadedDirectory"
print_dir(filepath)