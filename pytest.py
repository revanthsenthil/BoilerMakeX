import pytesseract as pt
import cv2
from PIL import Image
import numpy as np

pt.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

file = 'assets/schedule_1.png'
img = np.array(Image.open(file))

div = 5

shape = list(np.shape(img))
X = shape[0] // div
Y = shape[1] // div
x_val = 0
y_val = 0

for d in range div:
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img_i = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img_i = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img_i = cv2.GaussianBlur(img, (1, 1), 0)
    




# print(np.shape(img))

print(img[100, 100])

# cv2.imshow('1', img)

print(pt.image_to_string(img))

# cv2.waitKey()


# file = 'assets/schedule_2.png'

# img = cv2.imread(file, 0)
# thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)[1]

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# result = 255 - opening
# cv2.imshow('thresh', thresh)
# cv2.imshow('opening', opening)
# cv2.imshow('result', result)

# text = pt.image_to_string(result)

# cv2.waitKey()