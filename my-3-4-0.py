# -*- coding:utf-8 -*-
# 如何进行反向迭代以及如何实现反向迭代
# 实现一个连续浮点数发生器FloatRange（和xrange类似）
# 根据给定范围（start,end）和步进值（step）产生一些列
# 连续浮点数，如迭代FloarRange(3.0,4.0,0.2)可产生序列

class FloatRange:
    def __init__(self,start,end,step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t < self.end:
            t += self.step
            yield t

    def __reversed__(self):
        e = self.end
        while e > self.start:
            e -= self.step
            yield e

for x in  FloatRange(1.0,4.0,0.5):
    print x

for y in reversed(FloatRange(1.0,4.0,0.5)):
    print y











