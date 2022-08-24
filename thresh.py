import cv2 as cv

img = cv.imread('large_img.jpg')
# cv.imshow('Original', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# ======== Simple thresholding =========
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold image', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold image inverse', thresh_inv)

# ========== Adaptive thresholding ============
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive threshold image', adaptive_thresh)

cv.waitKey(0)
