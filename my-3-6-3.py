# -*- coding:utf-8 -*-
# 如何在一个for语句中迭代多个可迭代对象？
# 实际案例：
# 1、某班学生期末考试成绩，语文、数学、英语分别存储在
# 3个列表中，同时迭代三个列表，计算每个学生的总分（并行）
# 2、某年级四个班，某次考试每班英语成绩分别存储在4个列表
# 中，依次迭代每个列表，统计全年级学生高于90分的人数（串行）
#
# 串行，使用内置函数zip，他能将多个可迭代对象合并，每次迭代返回一个元组
# 使用标准库中的itertools.chain,他能将多个可迭代对象连接
from random import randint
from itertools import chain

math  = [randint(60,100) for _ in range(20)]
chinese  = [randint(60,100) for _ in range(20)]
english  = [randint(60,100) for _ in range(20)]
x=0
plus = []
for m in chain(math,chinese,english):
    if m>90:
        plus.append(m)
print plus







