
import cv2 
import glob
path = '/home/nibaran/Downloads/sick_enhance/*.*'
img_list =glob.glob(path)
img_number =1


for file in img_list[0:37]:
    img = cv2.imread(file, 0)
    # blur the image to denoise using GaussianBlur filter
    blurred_image = cv2.GaussianBlur(img, (3,3), 1.4)
    
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (9,9), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (9,9), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (9,9), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    blurred_image = cv2.GaussianBlur(blurred_image, (3,3), 1.4)
    
    edges = cv2.Canny(blurred_image, 10, 50)
    #
    
    
    
    #canny edge detection
    edges =cv2.Canny(edges, 10,50)
    edges =cv2.Canny(edges, 10,50)
    edges =cv2.Canny(edges, 10,50)
    #dilation operation
    edges = cv2.dilate(edges, (3,3))
    edges = cv2.dilate(edges, (3,3))
    edges = cv2.dilate(edges, (3,3))
    edges = cv2.dilate(edges, (3,3))
    
    
    cv2.imwrite("/home/nibaran/Downloads/sick_enhance_canny/"+ str(img_number)+".jpg", edges)
    img_number+=1
      



 





  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  




