# -*- coding:utf-8 -*-
# 如何将文件映射到内存？
# 1、在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问
# 2、某些嵌入式设备，寄存器被编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器
# 3、如果多个进程映射同一个文件，还能实现进程间通信
# 使用标准库中的mmap模块的mmap()函数，他需要一个打开的文件描述符作为参数
import mmap
import os

f = open('vgabios-cirrus.bin', 'r+b')
fo = f.fileno()
print fo

# m = mmap.mmap(fo,0,access=mmap.ACCESS_WRITE)
# print type(m)
# print m[0]
m = mmap.mmap(fo, mmap.PAGESIZE*8, access=mmap.ACCESS_WRITE, offset=mmap.PAGESIZE*4)
print m[0]