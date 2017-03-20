#!/usr/bin/env python
# -*- coding: utf-8 -*-

' this is a config module'

__author__ = 'wenbo chen'

import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')


CONFIG = '/Users/apple/code/python/python_script/config.ini'


# 读取配置文件
def read_config(namespace, key):
    config = ConfigParser.ConfigParser()
    config.read(CONFIG)
    return config.get(namespace, key)


if __name__ == '__main__':
    print read_config('database', 'user')
