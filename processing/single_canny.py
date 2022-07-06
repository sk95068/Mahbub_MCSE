#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:48:39 2022

@author: nibaran
"""

import cv2 
import glob
path = '/home/nibaran/Downloads/clahe/*.*'
#img_list =glob.glob(path)
img_number =1
img_list = glob.glob(path)
for file in img_list[0:29]:
    
    img = cv2.imread(file, 0)
# blur the image to denoise
    blurred_image = cv2.GaussianBlur(img, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (9,9), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (9,9), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (9,9), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
#canny edge detector
    edges = cv2.Canny(blurred_image, 10, 50)
    edges =cv2.Canny(edges, 10,50)
    edges =cv2.Canny(edges, 10,50)
    edges =cv2.Canny(edges, 10,50)
  #dilation operation  
    edges = cv2.dilate(edges, (3,3))
    edges = cv2.dilate(edges, (3,3))
    edges = cv2.dilate(edges, (3,3))
    edges = cv2.dilate(edges, (3,3))


    cv2.imwrite("/home/nibaran/Downloads/canny/"+ str(img_number)+".jpg", edges)
    img_number+=1
  

