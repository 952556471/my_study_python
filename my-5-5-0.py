# -*- coding:utf-8 -*-
# 如何访问文件的状态？
# 在某些项目中，我们需要获得文件状态
# 1、文件的类型，（普通文件，目录，符号连接，设备文件）
# 2、文件的访问权限
# 3、文件的最后访问、修改、节点状态更改时间
# 4、普通文件的大小

# 系统调用：标准库中的os模块下的三个系统调用stat，fstat，lstat获取文件状态
# 快捷函数：标准库中的os.path下一些函数，使用起来更加简洁

import os
s = os.stat('test.txt')
os.lstat('test.txt')   #不跟随符号连接
f = open('test.txt')
os.fstat(f.fileno())  # 参数为文件描述符
print s
print s.st_mode
import stat
print stat.S_ISDIR(s.st_mode)  #文件夹
print stat.S_ISREG(s.st_mode)   #普通文件

print s.st_mode & stat.S_IREAD   #读权限
print s.st_mode & stat.S_IXUSR   #执行权限

print s.st_atime   #访问
print s.st_mtime  #修改
print  s.st_ctime  #状态更新

import time
print time.localtime(s.st_atime)

print s.st_size  #文件大小
