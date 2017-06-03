# -*- coding:utf-8 -*-
# 如何处理二进制文件
# open函数想以二进制模式打开文件，制定mode参数为‘b’
# 二进制数据可以用readinfo读入到提前分配好的buffer中，便于数据处理
# 解析二进制数据可以使用标准库中的struct模块的unpack方法

import struct
f = open('fukua.wav', 'rb')
info = f.read(44)
# print info
# print struct.unpack('h', '\x01\x02')   #小段字节序
# print struct.unpack('>h', '\x01\x02')  #大端字节序
#
# print struct.unpack('h', info[22:24])
# print struct.unpack('i', info[24:28])
# print struct.unpack('h', info[34:36])

import array
f.seek(0,2)   #文件末尾
print f.tell()   #文件长度

n = (f.tell() - 44) / 2
buff = array.array('h', (0 for _ in xrange(n)))
f.seek(44)
f.readinto(buff)
print buff[5]
f2 = open('demo.wav', 'wb')
for i in xrange(n):
    buff[i] /= 8

f2.write(info)
buff.tofile(f2)
f2.close()