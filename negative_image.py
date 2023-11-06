import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#load the image
img1 = cv.imread('./img/img1.jpeg')
img1 = img1[: , : , ::-1]

#convert img to matrix. 
img1_matrix = np.array(img1)
img_invert = np.invert(img1_matrix)
cv.imwrite('./img/img_invert.jpeg', img_invert)

#show image
plt.subplot(1,2,1)
plt.imshow(img1), plt.title('Image 1'), plt.subplots_adjust(wspace=1)

plt.subplot(1,2,2)
plt.imshow(img_invert), plt.title('Negative'), plt.subplots_adjust(wspace=1)

plt.show()