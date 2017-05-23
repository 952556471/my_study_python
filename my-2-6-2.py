# -*- coding:utf-8 -*-
# 如何保持字典有序
from collections import OrderedDict
from time import time
from random import randint
d = OrderedDict()
players = list("ABCDEFGH")
start = time()
for i in xrange(8):
    raw_input("qingshuru")
    p = players.pop(randint(0, 7-i))
    end = time()
    print i+1, p, end-start
    d[p] = (i+1, end-start)

for k in d:
    print k, d[k]