# -*- coding:utf-8 -*-
# 如何实现可迭代对象和迭代器对象
# 实现一个迭代器对象Weatheriterator,next方法每次返回一个城市气温
# 实现一个可迭代独享Weatheriterable,__iter__方法返回一个迭代器对象

import requests
def getweather(city):
    r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
    data = r.json()['data']['forecast'][0]
    return '%s:%s,%s'%(city,data['low'],data['high'])
print getweather(u'北京')
print getweather(u'西安')