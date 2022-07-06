#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:24:35 2022

@author: nibaran
"""
import numpy as np
import glob
import cv2
import matplotlib.pyplot as plt
from sklearn.preprocessing import Binarizer
path = '/home/nibaran/Downloads/sick_enhance_canny/*.*'
img_list = glob.glob(path)
img_number =1
for file in img_list[0:37]:
    img = cv2.imread(file,0)

    
    binary = Binarizer(threshold=0.5)
    binary1 = binary.transform(img)
    x=np.array(binary1)*255
    plt.imshow(x)
    cv2.imwrite("/home/nibaran/Downloads/sick_enhance_canny_B/" +str(img_number)+'.jpg', x)
    img_number+=1
    