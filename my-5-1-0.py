# -*- coding:utf-8 -*-
# 如何额读写文本文件？
print ord('a')
s = u'你好'
se = s.encode("utf8")
print se.decode("utf8")


f = open('py2.txt','w')
sy = u'你好'
f.write(s.encode("utf8"))
f.close()

f = open('py2.txt','r')
t = f.read()
print t
print t.decode('utf8')

# python3的用法
# f =open('py3.txt','wt',encoding='utf8')
# f.write("你好我爱编程")
# f.close()
#
# f = open('py3.txt','rt',encoding='utf8')
# s = f.read()
# print s
