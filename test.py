# -*- coding: utf-8 -*-
import numpy as np
import cv2
cap= cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,img=cap.read()
    if ret==True:
        cv2.imshow('frame',img)
        k=cv2.waitKey(10)&0xff
        if k==ord('q'):
            cv2.imwrite('catch.jpg',img)
            break;

cap.release()
cv2.imshow('catch',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
