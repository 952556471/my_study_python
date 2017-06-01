# -*- coding:utf-8 -*-
# 如何将多个小字符串拼接成一个大的字符串
# 解决方案：方法一：迭代列表，连续使用'+'操作依次拼接每一个字符串
# 方法二：使用str.join()方法，更加快速的拼接列表中所以的字符串
s1 = "djjfh"
s2 = "387676"
s3 = s1+s2
print s3
print ';'.join(["er","56","ddfr","7909"])
print ''.join(["er","56","ddfr","7909"])

l = ["er","56","ddfr","7909"]
print ''.join([str(s) for s in l])  #列表解析，不建议
print ''.join(str(s) for s in l)  #生成器表达式，建议







