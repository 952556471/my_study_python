# -*- coding:utf-8 -*-
#实际案例
# 如何统计序列中元素的出现频度
# 1、某随机序列[12,5,6,4,5,5,7]找出出现次数最高的3个元素，他们出现的次数是多少？
# 2、对某英文文章的单词进行词频统计，找到出现次数最高的10个单词，它们出现的次数是多少

# 解决方案
# 使用collections.Counter
# 将序列传入Counter的构造器，得到Counter对象是元素频度的字典
# Counter.most_common(n)方法得到频度最高的n个元素的列表
from random import randint
# 例子1方法一
my_data = [randint(1, 20) for _ in xrange(30)]
print my_data

my_d = dict.fromkeys(my_data, 0)
print my_d
for x in my_data:
    my_d[x] += 1
print my_d

my_d1 = sorted(my_d.iteritems(), key=lambda asd: asd[1], reverse=True)
my_d2 = sorted(my_d.iteritems(), key=lambda asd: asd[0], reverse=True)
print my_d1
print my_d2















