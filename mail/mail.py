#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
abspath = os.path.abspath('.') + '/python_script/config'
sys.path.append(abspath)
from config import config
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# 将xls文件作为邮件附件发送
def send_mail_by_xls():
    print 'start send mail'

    _user = config.read_config('email', 'user')
    _pwd = config.read_config('email', 'pwd')
    _to = config.read_config('email', 'to')

    try:
        msg = MIMEMultipart()
        msg['From'] = _format_addr(u'Python爱好者 <%s>' % _user)
        msg['To'] = _format_addr(u'管理员 <%s>' % _to)
        msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

        # 邮件正文是MIMEText:
        msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open(
            '/Users/apple/code/python/python_script/test.xls',
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
