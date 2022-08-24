import cv2 as cv

# img = cv.imread('OIP.jpg')
# cv.imshow('Original', img)


# Resizing
def rescaleFrame(frame, scale=0.5):
    # works on images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # works for live video only
    capture.set(3, width)
    capture.set(4, height)


# frame_resized = rescaleFrame(img)
# cv.imshow('Resized image', frame_resized)
video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    changeRes(300, 400)
    cv.imshow('Video', video)

    if cv.waitKey(20) or 0xFF == ord('q'):
        break

# cv.waitKey(0)
