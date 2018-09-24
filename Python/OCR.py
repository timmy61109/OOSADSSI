#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('../Image/1.png'),lang='chi_sim')
print text
