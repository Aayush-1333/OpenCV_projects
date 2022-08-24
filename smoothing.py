import cv2 as cv

img = cv.imread('OIP.jpg')

# ============= Blurring techniques =================

# Averaging method
avg = cv.blur(img, (3, 3))
cv.imshow('Average Blur', avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral blur


cv.waitKey(0)
