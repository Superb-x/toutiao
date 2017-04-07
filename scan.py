#coding:utf-8
import os

fileArr = []
def search(path, f):
    for x in os.listdir(path):
        fp = os.path.join(path, x)
        if os.path.isfile(fp) and f in x:
            print(fp)
        elif os.path.isdir(fp):
            search(fp, f)

search('.', '')