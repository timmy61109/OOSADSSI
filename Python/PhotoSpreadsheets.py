#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# WTFPL license

import xlsxwriter
import imageio
import FileAccess as FA

def PhotoSpreadsheets(ReadPath, WritePath):
    pict = imageio.imread(ReadPath)
    FA.CreateCSV(WritePath)
    for RGBList in pict:
        i = 0
        for RGB in RGBList:
            col = '%02x%02x%02x' % (RGB[0], RGB[1], RGB[2])
            if i == 0:
                ColList = col
                i = 1
            else:
                ColList += col + ","
        ColList += "\n"
        FA.AddDataCSV(WritePath, ColList)
