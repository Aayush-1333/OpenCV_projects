import cv2 as cv

# ======= reading images =======
img = cv.imread('large_img.jpg')
cv.imshow('Aayush', img)
cv.waitKey(0)

# ===== reading videos =====
# capture = cv.VideoCapture('sample-mp4-file.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(20) and 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()
