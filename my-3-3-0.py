# -*- coding:utf-8 -*-
# 如何使用生成器函数实现可迭代对象
# 实现一个可迭代对象的类，他能迭代出给定范围内的所以素数
# 将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
# 生成器函数
def f():
    print "1"
    yield
    print "2"
    yield
    print "3"
    yield

g = f()
for x in g :
    print x





