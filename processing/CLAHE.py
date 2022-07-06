#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:44:34 2022

@author: nibaran
"""
path ='/home/nibaran/Downloads/original/*.*'
import numpy as np
import cv2 
img_number =1
import glob
img_list=glob.glob(path)
for file in img_list[0:9]:
    
    img = cv2.imread(file,0)
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=0.90, tileGridSize=(8,8))

    cl1 = clahe.apply(img)
    cv2.imwrite("/home/nibaran/Downloads/clahe/" + str(img_number) +".jpg", cl1)
    img_number+=1