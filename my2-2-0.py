# -*- coding:utf-8 -*-
# 如何为元组的每个元素命名，提高程序的可读性
students = ('Jim',16,'Male','jimerrr@123.com')
NAME,AGE,SEX,EMAIL = xrange(4) #列表拆包
print students[0]
print students[NAME]

from collections import namedtuple
student = namedtuple('Student',['name','age','sex','email'])
s= student('Jim',20,'male','jimerrr@123.com')
print s
print s.name




















