#!/usr/bin/env python
import numpy as np
import cv2
from cv_detection import color_detection

from cv_detection import detect_window


d = detect_window()

# print(cv2.ocl.haveOpenCL())
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# if face_cascade.empty(): raise Exception("your face_cascade is empty. are you sure, the path is correct ?")

# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# if eye_cascade.empty(): raise Exception("your eye_cascade is empty. are you sure, the path is correct ?")

c = color_detection()
video = cv2.VideoCapture(0)
ret, frame = video.read()
center = np.array([100,100,frame.shape[0]/2,frame.shape[0]/2])
alpha = 0.1
while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        # c.get_rect(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # if len(faces)>0:
        #     center= center*(1-alpha)+np.mean(faces,axis=0)*alpha
        #     print(center)
        #     for (x,y,w,h) in faces:
        #         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #     cv2.circle(frame,(int(center[0]),int(center[1])),10,(0,0,200),-1)
        #     # roi_gray = gray[y:y+h, x:x+w]
        #     # roi_color = frame[y:y+h, x:x+w]
        #     # eyes = eye_cascade.detectMultiScale(roi_gray)
        #     # for (ex,ey,ew,eh) in eyes:
        #     #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # cv2.imshow('Video', frame)
        d.update(frame)
        
    if cv2.waitKey(1) & 0xFF == 27:
        break