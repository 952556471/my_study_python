# -*- coding:utf-8 -*-
# 如何对迭代器做切片操作？
# 实际案例：
# 有某个文本文件，我们想读取其中某范围的内容如100-300
# 行之间的内容，Python中文本文件是可迭代对象，我们是否
# 可以使用类似切片的方式得到一个100-300行文件内容的生
# 成器
# 解决方案
# 使用标准库中的itertools.islice,它能返回一个迭代对象切片的生成器
from itertools import islice
f = open('txtfile')
lines = islice(f, 20, 30)
print lines
for line in lines:
    print line

lines1 = islice(f,30)
print lines1
for line1 in lines1:
    print line1

lines2 = islice(f,30,None)
print lines2
for line2 in lines2:
    print line2









