# -*- coding:utf-8 -*-
# 如何快速找到多个字典中的公共键
from random import randint, sample

my_sample1 = sample("abcdefg", randint(2, 6))
my_sample2 = sample("abcdefg", randint(2, 6))
my_sample3 = sample("abcdefg", randint(2, 6))
my_s1 = {x: randint(3, 6)for x in my_sample1}
print my_s1
my_s2 = {x: randint(3, 6)for x in my_sample2}
print my_s2
my_s3 = {x: randint(3, 6)for x in my_sample3}
print my_s3
print map(dict.viewkeys, [my_s1, my_s2, my_s3])
print reduce(lambda a, b:a & b, map(dict.viewkeys, [my_s1, my_s2, my_s3]))