# Tesseract OCR using pytesseract
Small project of how to text parsing from image using Tesseract OCR in Python.

# Source code:

```python
#!/usr/bin/python
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd\
	= os.path.join(os.getenv("TMP"), "Tesseract-OCR", "tesseract.exe")
img = cv2.imread(os.path.join(os.getcwd(), "sample.png"))
custom_config = r'--oem 3 --psm 6'
img_str = pytesseract.image_to_string(img, config=custom_config)
print(img_str)
```

```shell
(xxxxxxxxx) (base) C:\Users\xxxxxxxxx\.virtualenvs\xxxxxxxxx-CvWzPnUJ\src>python main.py
Players online (19): NightNolif, Theltani, Justas, Fvj,
Nmtrang, BriansCat, UhYeahh, Baltty, Poseidon, Pondk,
NobleRai, AntsNae, SamRiddell, Oderotog, Taheryahia,
wmu, CecilPalmr, HeyimYaxo
```

# Useful link:
- "Pytesseract : "TesseractNotFound Error: tesseract is not installed or it's not in your path", how do I fix this?", available at https://stackoverflow.com/a/53672281.
