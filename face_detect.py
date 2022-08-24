import cv2 as cv

img = cv.imread('Aayush photo passport.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
print(f"No. of faces found = {len(face_rect)}")
cv.imshow('Detected faces', img)

cv.waitKey(0)
