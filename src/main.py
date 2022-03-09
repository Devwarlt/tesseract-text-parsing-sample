#!/usr/bin/python

"""
Solving "pytesseract.pytesseract.TesseractNotFoundError" exception:
	https://stackoverflow.com/a/53672281
"""

import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd\
	= os.path.join(os.getenv("TMP"), "Tesseract-OCR", "tesseract.exe")
img = cv2.imread(os.path.join(os.getcwd(), "sample.png"))
custom_config = r'--oem 3 --psm 6'
img_str = pytesseract.image_to_string(img, config=custom_config)
print(img_str)