#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
python
import os
import PhotoSpreadsheets as PS

result_dir = '../Image/'
lists = os.listdir(result_dir)
for Document in lists:
    ReadPath, WritePath = "../Image/" + Document, "../Data/" + Document[:-4] + ".csv"
    #PS.PhotoSpreadsheetsCSV(ReadPath, WritePath)
    PS.PhotoRGBCSV(ReadPath, WritePath)

^Z
python
import os
import PhotoSpreadsheets as PS
import imageio
import FileAccess as FA

def PhotoRGB(ReadPath):
    pict = imageio.imread(ReadPath)
    for X in range(0, pict.shape[0]):
        for Y in range(0, pict.shape[1]):
            a = pict[X, Y]
            col = '%03d%03d%03d' % (a[0], a[1], a[2])
            col, X ,Y = str(col), str(X), str(Y)
            #AllList = [X, Y, col]
            AllList = X + Y + col
            print AllList
            #return AllList

result_dir = '../Image/'
lists = os.listdir(result_dir)
for Document in lists:
    ReadPath = "../Image/" + Document
    PhotoRGB(ReadPath)
