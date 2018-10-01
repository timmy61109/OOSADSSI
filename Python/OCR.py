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
