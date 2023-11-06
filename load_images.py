import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#load the image
img1 = cv.imread('./img/img1.jpeg')
img2 = cv.imread('./img/img2.jpeg')
img3 = cv.imread('./img/img3.jpeg')
#switch color system from bgr to rgb
img1_rgb = img1[ : , : , ::-1] 
img2_rgb = img2[ : , : , ::-1] 
img3_rgb = img3[ : , : , ::-1] 

#grid to show multiple images
plt.subplot(1,3,1)
#show image
plt.imshow(img1_rgb,'gray' ), plt.title('Image 1'), plt.subplots_adjust(wspace=1)

plt.subplot(1,3,2)
plt.imshow(img2_rgb,'gray'), plt.title('Image 2'), plt.subplots_adjust(wspace=1)

plt.subplot(1,3,3)
plt.imshow(img3_rgb,'gray'), plt.title('Image 3'), plt.subplots_adjust(wspace=1)


plt.show()

