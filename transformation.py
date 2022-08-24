import cv2 as cv
import numpy as np

img = cv.imread('OIP.jpg')


# ==== Translation ====
def translate(original_img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (original_img.shape[1], original_img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# x --> Right
# y --> Down
# -x --> Left
# -y --> Up
# translated = translate(img, -100, -100)
# cv.imshow('Translated image', translated)


# ====== Rotation ======
def rotate(original_img, angle, rotPoint=None):
    (height, width) = original_img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(original_img, rotMat, dimensions)


# rotated = rotate(img, 45)
# cv.imshow('Rotated image', rotated)

# ======= Flipping =======
# 1 --> flip vertically, 0 --> flip horizontally, -1 --> flip both vertically and horizontally
flip = cv.flip(img, -1)
cv.imshow('Flipped image', flip)

cv.waitKey(0)
