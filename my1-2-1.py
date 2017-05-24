# -*- coding:utf-8 -*-
# 如何在集合中根据条件筛选数据
# 1、集合解析
from random import randint
data1 = [randint(-10,10) for _ in xrange(10)]
print data1
data2 = set(data1)
print data2
set1 = {x for x in data2 if x%2==0}
print set1


















