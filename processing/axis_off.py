#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:01:04 2022

@author: nibaran
"""


import glob
import cv2
import matplotlib.pyplot as plt
path = '/home/nibaran/Downloads/DMR/Enhanced_image_Healthy/final_canny_en_Healthy/1.jpg'
list =glob.glob(path)
img_number =1


for file in list[0:1]:
    img1 = cv2.imread(file, 1)
    crop_image =img1[50:253, 76:360]
    plt.axis('off')
    plt.imshow(img1)
    cv2.imwrite('/home/nibaran/Downloads/front_text_sick_axis/' +str(img_number)+'.jpg', crop_image)
    img_number+=1
    