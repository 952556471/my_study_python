# -*- coding:utf-8 -*-
# 如何判断字符串是否以字符串b开头或者结尾
# 使用字符串的str.startwith()和str.endwith()方法，
# 注意，多个匹配时参数使用元组
import os
import stat
listdiry = os.listdir(".")
print listdiry

s = "go.sh"
print s.endswith('.sh')

s.endswith(('.sh','.py','.go'))

listdiry1 = [name for name in listdiry if name.endswith(('.go','.sh'))]
print listdiry1
os.stat("my-2-4-1.py")
os.stat("my-2-4-1.py").st_mode
print oct(os.stat("my-2-4-1.py").st_mode)

os.chmod("my-2-4-1.py",os.stat("my-2-4-1.py").st_mode | stat.S_IXUSR)