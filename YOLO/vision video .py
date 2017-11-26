# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 22:24:56 2017

@author: 林亦盛
"""

import numpy as np
import cv2
test_video_new = np.load('west_video_new1.npy')
#print(test_video_new.shape)



#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



#print(len(test_video_new))




fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('test_west_4.avi',-1, 30.0, (1280,720))
#cv2.VideoWriter.isOpened()

for i in range(500):
    frame = test_video_new[i]
    out.write(frame)
out.release()
