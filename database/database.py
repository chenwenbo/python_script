#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
abspath = os.path.abspath('.') + '/python_script/config'
sys.path.append(abspath)
from config import config
import MySQLdb as mysqldb


# 查询sql数据并转化为list
def query_data():
    print 'start query data'
    db = mysqldb.connect(host=config.read_config('database', 'host'),
                         user=config.read_config('database', 'user'),
                         passwd=config.read_config('database', 'passwd'),
                         db=config.read_config('database', 'db'))
    cursor = db.cursor()
    cursor.execute(config.read_config('database', 'sql'))
    # 重置游标的位置
    cursor.scroll(0, mode='absolute')
    # 搜取所有结果
    results = cursor.fetchall()
    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    db.close()
    return results, fields
