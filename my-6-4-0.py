# -*- coding:utf-8 -*-

# 如何构建xml文档
# 使用标准库中的xml.etree.ElementTree,构建ElementTree，使用write方法写入文件
from xml.etree.ElementTree import Element,ElementTree
e = Element('Data')
e.set('name','abc')
from xml.etree.ElementTree import tostring
tostring(e)
e.text = '123'
print tostring(e)
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)
print tostring(e2)
e.text = None
e.append(e2)
print tostring(e)

et = ElementTree(e)
et.write('demo.xml')




