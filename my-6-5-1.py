# -*- coding:utf-8 -*-

# 如何读物excel文件
# 使用pip安装。pip install xlrd xlwt
# 使用第三方库xlrd和xlwt，这两个库分别用于excel的读和写
#写入xls
import xlwt
wbook = xlwt.Workbook
wsheet = wbook.add_sheet("sheet1")  # 添加一个表
# wsheet.write(r, c, label,)
wbook.save('out.xlsx')   # 保存






