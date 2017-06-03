# -*- coding:utf-8 -*-
# 如何读写csv数据

# 使用标准库中的csv模块，可以使用其中的reader和writer完成csv文件读写
import csv
with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan_copy.csv', 'wb') as wf:
        writer = csv.writer(wf)
        header = reader.next()
        writer.writerow(header)


