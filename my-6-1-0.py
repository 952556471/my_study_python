# -*- coding:utf-8 -*-
# 如何读写csv数据

# 使用标准库中的csv模块，可以使用其中的reader和writer完成csv文件读写
from urllib import urlretrieve

urlretrieve('https://shimo-exports.oss-cn-shanghai.aliyuncs.com/sheet/hq3vCjTgSP0I4QdQ/%E7%8E%B0%E5%9C%BA%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB_%E6%97%B6%E6%97%B6%E6%9B%B4%E6%96%B0_2017%E5%B9%B4.xlsx','pingan.csv')
import csv
rf = open('pingan.csv','rb')
reader = csv.reader(rf)
print reader.next()


wf = open('pingan_copy.csv', 'wb')
writer1 = csv.writer(wf)
writer1.writerow(reader.next())


with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan_copy.csv', 'wb') as wf:
        writer = csv.writer(wf)
        writer.wrirow('')


