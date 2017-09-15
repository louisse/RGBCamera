import cv2
import numpy as np

head_cascade = cv2.CascadeClassifier('data/cascadeH5.xml')
body_cascade = cv2.CascadeClassifier('data/cascadG.xml')
#face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
#fbody_cascade = cv2.CascadeClassifier('data/haarcascade_fullbody.xml')
cap = cv2.VideoCapture(0)
while True:
  _, frame = cap.read()
  
  #gray is thermal image
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  lower = np.array([100])
  upper = np.array([255])

  mask = cv2.inRange(gray, lower, upper)
  res = cv2.bitwise_and(frame,frame, mask=mask)

  heads = head_cascade.detectMultiScale(res, 1.05, 5)
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

  #insert code to send to socket

  k = cv2.waitKey(10) & 0xFF
  if k == 27:
    break
cap.release()