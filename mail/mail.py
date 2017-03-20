#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
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


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# 将xls文件作为邮件附件发送
def send_mail_by_xls():
    print 'start send mail'

    _user = read_config('email', 'user')
    _pwd = read_config('email', 'pwd')
    _to = read_config('email', 'to')

    try:
        msg = MIMEMultipart()
        msg['From'] = _format_addr(u'Python爱好者 <%s>' % _user)
        msg['To'] = _format_addr(u'管理员 <%s>' % _to)
        msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

        # 邮件正文是MIMEText:
        msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open(
            '/Users/apple/code/python/data_group_automation_project/test.xls',
                'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            # mime = MIMEBase('xls', 'xls', filename='test.xls')
            mime = MIMEBase('application', 'octet-stream')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition',
                            'attachment', filename='test.xls')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(_user, _pwd)
        server.sendmail(_user, _to, msg.as_string())
        server.quit()

    except smtplib.SMTPException, e:
        print "Falied,%s" % e
