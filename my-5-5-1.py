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

print os.path.isdir('test.txt')
print os.path.islink('test.txt')
print os.path.isfile('test.txt')

print os.path.getatime('test.txt')
print os.path.getsize('test.txt')

