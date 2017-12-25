# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:55:12 2017

@author: 林亦盛
Changing video into numpy data on Windows, since it is unavailable to open videos by opencv on Ubuntu virtual machine. 
"""

import numpy as np
import cv2

cap = cv2.VideoCapture()
ret = cap.open('West.mp4')
print(ret)


frames = list()
i = 0
while ret:
    ret, img = cap.read()
    if ret:
        frames.append(img)
        i += 1
np.save('west_video', frames)
