import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

np.load('features.npy', allow_pickle=True)
np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
people = ["anne marie", "charlie puth", "elton john", "selena gomez"]

img_list = os.listdir(r'C:\Users\hellb\Artificial Intelligence\Computer_Vision\validation')
for pic in img_list:
    img = cv.imread(r'C:\Users\hellb\Artificial Intelligence\Computer_Vision\validation\{}'.format(pic))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Person', gray)

    # detect face
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)

    for (x, y, w, h) in face_rect:
        face_roi = gray[y: y + h, x: x + w]

        label, confidence = face_recognizer.predict(face_roi)
        print(f"{people[label]} with confidence of {confidence:2f}%")

        cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

        cv.imshow('Detected faces', img)

    cv.waitKey(0)
