# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:55:12 2017

@author: 林亦盛
"""

import numpy as np
import cv2
'''
img = cv2.imread('haha.png',0)
print(img)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
cap = cv2.VideoCapture()
ret = cap.open('Vince Carter.mp4')
print(ret)

'''
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

    cv2.imshow('frame',gray)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
'''
frames = list()
i = 0
while ret:
    ret, img = cap.read()
    if ret:
        frames.append(img)
        i += 1
np.save('vince_video', frames)
