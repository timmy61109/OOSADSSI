#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# WTFPL license

import xlsxwriter
import imageio
import FileAccess as FA

def PhotoSpreadsheetsCSV(ReadPath, WritePath):
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

def PhotoRGB(ReadPath):
    pict = imageio.imread(ReadPath)
    AllList = []
    for X in range(0, pict.shape[0]):
        for Y in range(0, pict.shape[1]):
            a = pict[X, Y]
            col = '%03d%03d%03d' % (a[0], a[1], a[2])
            AllList.append([X, Y, col])
    return AllList

def PhotoRGBCSV(ReadPath, WritePath):
    FA.CreateCSV(WritePath)
    for X, Y, col in PhotoRGB(ReadPath):
        x , y, col = str(X), str(Y), str(col)
        ColList = x + "," + y + "," + col + "\n"
        FA.AddDataCSV(WritePath, ColList)

def PhotoSpreadsheetsXlsx(ReadPath, WritePath):
    pict = imageio.imread(ReadPath)

    workbook = xlsxwriter.Workbook(WritePath)
    worksheet = workbook.add_worksheet()

    for i in range(0, pict.shape[0]):
        for j in range(0, pict.shape[1]):
            a = pict[i, j]
            col = '#%02x%02x%02x' % (a[0], a[1], a[2])
            format = workbook.add_format()
            format.set_bg_color(col)
            worksheet.write(i, j, '', format)
    workbook.close()
