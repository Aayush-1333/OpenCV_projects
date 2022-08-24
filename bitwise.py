import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# === bitwise AND ===
# AND ----> intersecting regions
bitwise_AND = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_AND', bitwise_AND)

# === bitwise OR ===
# OR -----> non-intersecting as well as intersecting regions
bitwise_OR = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_OR', bitwise_OR)

# === bitwise XOR ===
# XOR ------> non-intersecting regions
bitwise_XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_XOR', bitwise_XOR)

# === bitwise NOT ===
# NOT ----> inverse of binary colors
bitwise_NOT = cv.bitwise_not(rectangle)
cv.imshow('Bitwise rectangle NOT', bitwise_NOT)

cv.waitKey(0)
