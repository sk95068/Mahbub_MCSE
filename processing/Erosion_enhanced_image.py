#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:54:19 2022

@author: nibaran
"""

import cv2
import glob
path = '/home/nibaran/Downloads/front_text_healthy_axis_en4/*.*'
color_img_list=glob.glob(path)

img_number =1
for file in color_img_list[0:13]:
    img = cv2.imread(file)
    img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eroded= cv2.erode(img,(3,3))
    eroded= cv2.erode(eroded,(3,3))
    eroded= cv2.erode(eroded,(3,3))
    eroded= cv2.erode(eroded,(3,3))
    eroded= cv2.erode(eroded,(3,3))
    cv2.imwrite('/home/nibaran/Downloads/clahe/' + str(img_number)+'.jpg', eroded)
    img_number +=1



    
  

