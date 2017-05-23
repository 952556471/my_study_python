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
s1_keys = my_s1.viewkeys()
print s1_keys
s2_keys = my_s2.viewkeys()
print s2_keys
s3_keys = my_s3.viewkeys()
print s3_keys
print s1_keys & s2_keys & s3_keys
