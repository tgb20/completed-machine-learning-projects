import cv2
import time
import random

CAPTURE_WIDTH = 1280
CAPTURE_HEIGHT = 720

cap = cv2.VideoCapture(0)
cap.set(3, CAPTURE_WIDTH)
cap.set(4, CAPTURE_HEIGHT)
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time.sleep(1)

points = 0
hitTarget = True
targetX = 0
targetY = 0
targetW = 50

while(True):
    _, img = cap.read()
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (47, 184, 2), 5)

        if (x <= targetX <= x + w) and (y <= targetY <= y + h):
            hitTarget = True
            points += 1

    if hitTarget:
        targetX = random.randint(targetW, CAPTURE_WIDTH - targetW)
        targetY = random.randint(targetW, CAPTURE_HEIGHT - targetW)
        hitTarget = False

    cv2.rectangle(img, (targetX, targetY), (targetX + targetW, targetY + targetW), (0, 0, 255), 20)

    cv2.putText(img, "Points: " + str(points), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Face Tracking', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
