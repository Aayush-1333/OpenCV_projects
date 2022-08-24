import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('OIP.jpg')
# cv.imshow('Original', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
masked_gray = cv.bitwise_and(gray, gray, mask=mask)
masked_rgb = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked Image', masked)
cv.imshow('Masked color image', masked_rgb)

# =========== Grayscale Histogram ==============
# gray_hist = cv.calcHist([gray], [0], masked_gray, [256], [0, 256])
# cv.imshow('Grayscale', gray)

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No. of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


# ============ Color Histogram =============
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    color_hist = cv.calcHist([masked_rgb], [i], None, [256], [0, 256])
    plt.plot(color_hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
