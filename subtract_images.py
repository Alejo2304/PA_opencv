import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#load the image
img1 = cv.imread('./img/img3.jpeg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('./img/img5.jpeg', cv.IMREAD_GRAYSCALE) 

#convert img to matrix. 
img1_matrix = np.array(img1)
img2_matrix = np.array(img2)

subtract = np.subtract(img1_matrix, img2_matrix)
cv.imwrite('./img/img_subtract.jpeg', subtract)

#grid to show multiple images
plt.subplot(2,2,1)
#show image
plt.imshow(img1,'gray' ), plt.title('Image 1'), plt.subplots_adjust(wspace=1)

plt.subplot(2,2,2)
plt.imshow(img2,'gray'), plt.title('Image 2'), plt.subplots_adjust(wspace=1)

plt.subplot(2,2,(3,4))
plt.imshow(subtract,'gray'), plt.title('Sum')

plt.show()