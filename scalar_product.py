import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#load the image
img1 = cv.imread('./img/img3.jpeg', cv.IMREAD_GRAYSCALE)
img1 = img1[ : , : , ::-1]

scalar = 0

#convert img to matrix. 
img1_matrix = np.array(img1)
img_scalar = np.multiply(img1_matrix, scalar)
cv.imwrite('./img/img_scalar.jpeg', img_scalar)

#grid to show multiple images
plt.subplot(1,2,1)
#show image
plt.imshow(img1,'gray' ), plt.title('Image 1'), plt.subplots_adjust(wspace=1)

plt.subplot(1,2,2)
plt.imshow(img_scalar,'gray'), plt.title('Image 2'), plt.subplots_adjust(wspace=1)

plt.show()