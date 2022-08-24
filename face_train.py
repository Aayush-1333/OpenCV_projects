import cv2 as cv
import os
import numpy as np

people = ["anne marie", "charlie puth", "elton john", "selena gomez"]
DIR = r"C:\Users\hellb\Artificial Intelligence\Computer_Vision\train"

features = []
labels = []
haar_cascade = cv.CascadeClassifier('haar_face.xml')


def create_train():
    # === looping over image folders ===
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        # === looping over images inside each folder ===
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rect:
                face_roi = gray[y:y + h, x:x + w]
                features.append(face_roi)
                labels.append(label)


create_train()
print("Training done ------------------")

features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on features and labels list
face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", labels)
