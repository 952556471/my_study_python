# -*- coding:utf-8 -*-
# 如何调整字符串中文本的格式、、
# 使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组
# 捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
import re
log = open('test.log').read()
re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
re.sub('(?P<year>\d{4})-(?P<day>\d{2})-(?P<month>\d{2})',r'\g<month>/\g<day>/\g<month>',log)

