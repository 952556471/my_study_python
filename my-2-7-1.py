# -*- coding:utf-8 -*-
# 如何实现用户的历史记录功（最多n条）

from random import randint
from collections import deque
import pickle
num = randint(1,100)
print num
q = deque([],5)
def guess(k):
    if k > num:
        print "k is big than num"
    if k < num:
        print "k is little than num"
    if k==num :
        print "congration to you input in right"
        return True
    return False

while True:
    inum = raw_input(u"请输入:")
    if inum.isdigit():
        inum = int(inum)
        q.append(inum)
        if guess(inum):
            break
    if inum=="h?":
        mq = list(q)
        print mq
    if inum =="end":
        break


pickle.dump(q,open("history",'w'))
q2 = pickle.load(open('history'))
print "q2:",list(q2)
