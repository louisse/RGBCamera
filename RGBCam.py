import cv2
import numpy as np

#face_cascade = cv2.CascadeClassifier('cascadeH5.xml')
#face_cascade = cv2.CascadeClassifier('cascadG.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture(0)
while True:
  _, frame = cap.read()
  #frame = cv2.imread('body.jpg')
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
  cv2.imshow("frame",frame)
  #cv2.imshow("gray",gray)
  k = cv2.waitKey(10) & 0xFF
  if k == 27:
    break
cap.release()