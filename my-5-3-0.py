# -*- coding:utf-8 -*-
# 如何设置文件缓冲
# 全缓冲、行缓冲、无缓冲

# 全缓冲，open函数的buffering设置为大于1的整数n，n为缓冲区的大小
# 行缓冲，open函数的buffering设置为1
# 无缓冲，open函数的buffering设置为0
f = open("demotext.txt", 'w')
f.write("abd")
f.write('+' * 4093)

f = open('demo2.txt', 'w', buffering=2048)
f = open('demo3.txt', 'w', buffering=1)
f = open('demo4.txt', 'w', buffering=0)

