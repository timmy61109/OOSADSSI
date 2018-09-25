#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
#學務處生輔組站立反省(OOSADSSI,Office Of Student Affairs Discipline Section Standing Introspection)
#20180327成功利用網路上的範例存入xlsx

from openpyxl import *
import time
import datetime

wb = load_workbook(filename='106_1_OOSADSSI_20171213.xlsx', read_only=True)
ws = wb['a']
a = ""
i = 0
for row in ws.rows:
    for cell in row:
        print cell.value
