# -*- coding:utf-8 -*-

# 如何读物excel文件
# 使用pip安装。pip install xlrd xlwt
# 使用第三方库xlrd和xlwt，这两个库分别用于excel的读和写
#写入xls
#coding:utf8
import xlrd, xlwt

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

for row in xrange(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')

for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('output.xlsx')


