# -*- coding:utf-8 -*-
# 如何使用临时文件
# 临时文件不用命名，关闭之后自动删除


# 使用标准库中tempfile下的TemporaryFile,NamedTemporaryFile
# TemporaryFile创建的额文件在文件系统中找不到

from tempfile import TemporaryFile,NamedTemporaryFile
f = TemporaryFile()
f.write('ajhdh0' * 1000)
f.seek(0)
print f.read(100)

ntf = NamedTemporaryFile()
print ntf.name

ntf = NamedTemporaryFile(delete=False)  # 关闭后文件不被删除
print ntf.name

