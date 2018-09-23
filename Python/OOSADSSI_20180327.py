#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
#學務處生輔組站立反省(OOSADSSI,Office Of Student Affairs Discipline Section Standing Introspection)
#20180327成功利用網路上的範例存入xlsx

from openpyxl import *
import time
import datetime
wb = Workbook()
wb2 = load_workbook(filename='106_1_OOSADSSI_20171213.xlsx')

wb2.save('106_1_OOSADSSI_20171213.xlsx')
