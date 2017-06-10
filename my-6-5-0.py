# -*- coding:utf-8 -*-

# 如何读物excel文件
# 使用pip安装。pip install xlrd xlwt
# 使用第三方库xlrd和xlwt，这两个库分别用于excel的读和写

import xlrd
book = xlrd.open_workbook('demo.xlsx')
book.sheets()
sheet = book.sheet_by_index(0)  # 第一个sheet
print sheet.nrows  # 行数
print sheet.ncols  # 列数
cell = sheet.cell(0, 0)
print cell.ctype  #类型
print cell.value  #值

print sheet.row()   #获取某一行
print sheet.row(1)   #返回是一个列表
print sheet.row_values(1)  #类似切片操作
print sheet.row_values(1,1)  #类似切片操作,跳过第一个

print sheet.col_values()
print sheet.col()

#添加一个单元格
# sheet.put_cell(rowx, colx, ctype, value, xf_index)








