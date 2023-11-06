import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#load the image
img1 = cv.imread('./img/img1.jpeg')

#switch color system from bgr to rgb
img1_rgb = img1[ : , : , ::-1] 

#show image
plt.imshow(img1_rgb,'gray' ), plt.title('Image 1')
plt.show()
