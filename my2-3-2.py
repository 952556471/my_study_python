# -*- coding:utf-8 -*-
#实际案例
# 如何统计序列中元素的出现频度
# 1、某随机序列[12,5,6,4,5,5,7]找出出现次数最高的3个元素，他们出现的次数是多少？
# 2、对某英文文章的单词进行词频统计，找到出现次数最高的10个单词，它们出现的次数是多少

# 解决方案
# 使用collections.Counter
# 将序列传入Counter的构造器，得到Counter对象是元素频度的字典
# Counter.most_common(n)方法得到频度最高的n个元素的列表

# 例子2方法一
import re
from collections import Counter

txt = open("ccccc.txt").read()

my_list = re.split('\w+', txt)
my_d = Counter(my_list)
my_d.most_common(3)















