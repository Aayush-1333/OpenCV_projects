import cv2 as cv
import numpy as np

img = cv.imread('OIP.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Original', img)
# cv.imshow('Grayscale', gray)

# Gradients can be assumed similar to edges
# however, they are different from mathematical point of view
# =========== Laplacian method ===========
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# ========= Sobel gradient magnitude representation method =========
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny edges', canny)

cv.waitKey(0)
