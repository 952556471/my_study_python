# -*- coding:utf-8 -*-
# 如何拆分含有多种分隔符的字符串
# 我们要把某个字符串依据分割符号拆分成不同的字段
# 该字符串包含多种不同的分隔符
# 实际案例
# s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# 其中<,><;><\><|>都是分隔符，如何处理
strs = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"

def mySplit(s,ds):
    res = [s]
    for d in ds:
        t=[]
        map(lambda x : t.extend(x.split(d)) ,res)
        res = t
    return [y for y in res if y ]

print mySplit(strs,',:;\t|')
