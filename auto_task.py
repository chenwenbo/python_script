#!/usr/bin/env python
# -*- coding: utf-8 -*-

from database import database
from xls import xls
from mail import mail


if __name__ == '__main__':
    results, fields = database.query_data()
    xls.convert_database_result_2_xls(results, fields)
    mail.send_mail_by_xls()
