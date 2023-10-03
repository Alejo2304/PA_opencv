import cv2 as cv
import numpy as py
from matplotlib import pyplot as plt

img = cv.imread('./img/img1.jpeg')

plt.imshow(img,'gray'), plt.title('Test 1')
plt.show()