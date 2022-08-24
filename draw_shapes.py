import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype=np.uint8)
cv.imshow('Blank', blank)

# 1)  ==== Paint the image a certain color ====
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green square', blank)

# 2) ==== Draw a rectangle ====
cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=cv.FILLED)
cv.rectangle(blank, (0, 0), (blank.shape[0] // 2, blank.shape[1] // 2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Green rectangle', blank)

# 3) ===== Draw a circle =====
cv.circle(blank, (blank.shape[0] // 2, blank.shape[1] // 2), 40, (0, 0, 255), thickness=cv.FILLED)
cv.imshow('Circle', blank)

# 4) ====== Draw a straight line ======
cv.line(blank, (0, 0), (blank.shape[0] // 2, blank.shape[1] // 2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5) ====== Put some text ======
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text image', blank)

cv.waitKey(0)
