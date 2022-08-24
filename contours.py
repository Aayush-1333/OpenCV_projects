import cv2 as cv
import numpy as np

img = cv.imread('OIP.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh image', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} were found!")

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Image with contours drawn', blank)

cv.waitKey(0)
