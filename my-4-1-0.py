# -*- coding:utf-8 -*-
# 如何拆分含有多种分隔符的字符串
# 我们要把某个字符串依据分割符号拆分成不同的字段
# 该字符串包含多种不同的分隔符
# 实际案例
# s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# 其中<,><;><\><|>都是分隔符，如何处理
strs = r"ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"

str1 = "hsjhd hjjh jlkj wii asa dasa s "
list1 =  str1.split()
print list1

res = strs.split(";")
print map(lambda x:x.split("|"),res)
t = []
print map(lambda x:t.extend(x.split(",")),res)
print t
