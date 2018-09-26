#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# WTFPL license

import xlsxwriter
import imageio
import FileAccess as FA

def a(ReadPath, WritePath):
    pict = imageio.imread(ReadPath)
    FA.CreateCSV(WritePath)
    for RGBList in pict:
        for RGB in RGBList:
            col = '#%02x%02x%02x' % (RGB[0], RGB[1], RGB[2])
            col.append(col)
            print col
        print col
