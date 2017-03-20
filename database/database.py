#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import MySQLdb as mysqldb
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CONFIG = '/Users/apple/code/python/data_group_automation_project/config.ini'
XLS_FILE = '/Users/apple/code/python/data_group_automation_project/test.xls'


# 读取配置文件
def read_config(namespace, key):
    config = ConfigParser.ConfigParser()
    config.read(CONFIG)
    return config.get(namespace, key)


# 查询sql数据并转化为list
def query_data():
    print 'start query data'
    db = mysqldb.connect(host=read_config('database', 'host'),
                         user=read_config('database', 'user'),
                         passwd=read_config('database', 'passwd'),
                         db=read_config('database', 'db'))
    cursor = db.cursor()
    cursor.execute(read_config('database', 'sql'))
    # 重置游标的位置
    cursor.scroll(0, mode='absolute')
    # 搜取所有结果
    results = cursor.fetchall()
    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    db.close()
    return results, fields
