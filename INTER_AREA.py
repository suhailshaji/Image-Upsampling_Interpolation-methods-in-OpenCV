import cv2
 
img = cv2.imread('/home/suhail/Desktop/Office/Upsampling/Interpolation_Using-OpenCv_Methods/image2.jpeg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 220 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 

cv2.imwrite('/home/suhail/Desktop/Office/Upsampling/Interpolation_Using-OpenCv_Methods/INTER_AREA_resize_2.jpeg', resized)
print('Resized Dimensions : ',resized.shape)