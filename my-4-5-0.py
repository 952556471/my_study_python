# -*- coding:utf-8 -*-
# 如何对字符串进行左右居中对齐
# 解决方案：方法一：使用字符串的str.ljust(),str.rjust(),str.center()进行左右居中对齐
# 方法二：使用format（）方法传递了类似'<20','>20','^20'参数完成对齐

str1 = "abc"
str2 = str1.ljust(20,"=")
str3 = str1.ljust(20)
print str2
print str3

s4 = "123"
s5 = s4.rjust(20)
s6 = s4.ljust(20,'=')

s7 = s4.center(20,'=')
s8 = s4.center(20)

s9 = format(s4,'<20')
s10 = format(s4,'>20')
s11 = format(s4,'^20')




