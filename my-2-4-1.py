# -*- coding:utf-8 -*-
# 如何根据字典中值的大小对字典中的项排序
# 实际案例
# 某班英语成绩以字典的形式存储为：{'':'','':'',''}
# 根据成绩高低，计算学生排名
# 解决方案
# 使用内置函数sorted
# 1、利用zip将字典转化为元组
# 2、传递sorted函数的key参数

# 方法一
from random import randint

grade1 = {x: randint(60,100) for x in "abcxyz"}
print grade1
# print "ddd"+str(list(iter(grade1)))
# grade2 = sorted(grade1)
list_name = grade1.keys()
list_many = grade1.values()
print list_name
print list_many
my_tuple = zip(grade1.values(), grade1.keys())
print my_tuple
my_tuple1 = sorted(zip(grade1.itervalues(),grade1.iterkeys()))
print my_tuple1
# print grade2