# -*- coding:utf-8 -*-
#如何在列表中根据条件筛选数据
# 2、函数式编程
#过滤其中的负数(Python内建的filter()函数用于过滤序列)
from random import randint
data = [randint(-10,10) for _ in range(10)]
print data
data1 = filter(lambda a:a>0,data)
print data1













