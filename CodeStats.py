# -*- coding: utf-8 -*-

__author__ = "苦叶子"


"""

公众号: 开源优测

Email: lymking@foxmail.com

function: 简单统计AutoHub工程代码量

"""

import os
import time
basedir = os.getcwd()
filelists = []

# 指定想要统计的文件类型
whitelist = ['py', 'js']

filelists = []


# 遍历文件, 递归遍历文件夹中的所有
def get_file(base_dir):
    for parent, dirnames, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename in ("CodeStats.py"):
                continue

            ext = filename.split('.')[-1]

            # 只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent, filename))


# 统计一个文件的行数
def count_line(fname):
    count = 0
    for file_line in open(fname).readlines():
        # 过滤掉空行
        if file_line != '' and file_line != '\n':
            count += 1

    print('%s ---- %s' % (fname, count))
    return count


if __name__ == '__main__':
    startTime = time.clock()

    get_file(basedir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + count_line(filelist)

    # 代码总行数
    print('total lines: %s' % totalline)

    # 统计过程总耗时
    print('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
