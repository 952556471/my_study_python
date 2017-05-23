# -*- coding:utf-8 -*-
# 如何根据字典中值的大小对字典中的项排序
# 实际案例
# 某班英语成绩以字典的形式存储为：{'':'','':'',''}
# 根据成绩高低，计算学生排名
# 解决方案
# 使用内置函数sorted
# 1、利用zip将字典转化为元组
# 2、传递sorted函数的key参数

# 方法二
from random import randint

grade1 = {x: randint(60, 100) for x in "abcxyz"}
print grade1
my_item = grade1.items()
print sorted(grade1.items(), key=lambda x: x[1],reverse=False)
print sorted(grade1.items(), key=lambda x: x[1],reverse=True)