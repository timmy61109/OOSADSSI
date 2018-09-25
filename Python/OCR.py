#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from PIL import Image
import pytesseract
import os

result_dir = '../Image/'
lists = os.listdir(result_dir)
for Document in lists:
    text = pytesseract.image_to_string(Image.open('../Image/' + Document),lang='chi_sim')
    print text
