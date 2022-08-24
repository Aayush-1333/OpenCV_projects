import cv2 as cv
import numpy as np

img = cv.imread('OIP.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

# Splitting of color channels
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Merging of color channels
merged = cv.merge([b, g, r])
# cv.imshow('Merged image', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue colors involved', blue)
cv.imshow('Green colors involved', green)
cv.imshow('Red colors involved', red)

cv.waitKey(0)
