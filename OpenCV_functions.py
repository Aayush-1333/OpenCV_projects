import cv2 as cv
import numpy as np

# ===== Original to Grayscale conversion =====
img = cv.imread('OIP.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Original', img)
cv.imshow('Grayscale', gray)

# === Blur ===
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blur)

# === edge detection ===
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ==== Dilation of an image ====
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated image', dilated)

# ==== Erosion of an image ====
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded image', eroded)

# ===== Resizing =====
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image', resized)

# ===== Cropping =====
cropped = img[100:500, 200:400]
cv.imshow('Cropped image', cropped)

cv.waitKey(0)
