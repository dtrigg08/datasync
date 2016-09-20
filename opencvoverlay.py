# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:33:55 2016

@author: DT
"""

import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


cap = cv2.VideoCapture(r'bowling 013.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    #cv2.imshow('frame',frame)
    plt.imshow(frame)
    plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





