
"""
Created on Thu Jun  9 13:26:15 2022

@author: nibaran
"""


#from IPython.display import Image , display
#from google.colab import files
#import torch
#import skimage.color
#import numpy as np
#from matplotlib import pyplot as plt
import numpy as np
import cv2 
import cv2 as cv
import glob

path = '/media/nibaran/STORAGE/Masters/Mahbub/DMR_DataSet/Healthy/*.*'
img_list =glob.glob(path)
img_number =1


#from matplotlib import pyplot as plt
for file in img_list[0:515]:
    img = cv2.imread(file, 0)
    kernel = np.ones((15,15),np.float32)/225
    dst = cv.filter2D(img,-1,kernel) 
    
  #files.download('1.jpg')
    cv2.imwrite("/media/nibaran/STORAGE/Masters/Mahbub/DMR_DataSet/smoothed_image/"+ str(img_number)+".jpg", dst)
    img_number+=1