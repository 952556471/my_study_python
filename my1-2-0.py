# -*- coding:utf-8 -*-
#如何在字典中根据条件筛选数据
# 1、字典解析
from random import randint
data1 = {x: randint(60,90) for x in xrange(1,21)}
print data1
data2 = {k:v for k,v in data1.iteritems() if v>80}
print data2

















