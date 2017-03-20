#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt

XLS_FILE = '/Users/apple/code/python/python_script/test.xls'


def convert_database_result_2_xls(results, fields):
    print 'start create xls'
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('results', cell_overwrite_ok=True)

    # 写上字段信息
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0])

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1, len(results) + 1):
        for col in range(0, len(fields)):
            sheet.write(row, col, u'%s' % results[row - 1][col])

    workbook.save(XLS_FILE)
