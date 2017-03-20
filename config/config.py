import ConfigParser

CONFIG = '/Users/apple/code/python/data_group_automation_project/config.ini'
XLS_FILE = '/Users/apple/code/python/data_group_automation_project/test.xls'


# 读取配置文件
def read_config(namespace, key):
    config = ConfigParser.ConfigParser()
    config.read(CONFIG)
    return config.get(namespace, key)
