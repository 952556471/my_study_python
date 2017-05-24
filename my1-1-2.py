# -*- coding:utf-8 -*-
#如何在列表中根据条件筛选数据
# 3、列表解析

from random import randint
data = [randint(-10,10) for _ in range(10)]
print data
data1 = [x for x in data if x>0]
print data1













