# -*- coding:utf-8 -*-
# 如何使用生成器函数实现可迭代对象
# 实现一个可迭代对象的类，他能迭代出给定范围内的所以素数
# 将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
# 生成器函数

class PrimeNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def primenumber(self,k):
        if k<2:
            return False
        for i in xrange(2,k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for n in xrange(self.start,self.end):
            if self.primenumber(n):
                yield n
for tn in PrimeNumbers(1,30):
    print tn










