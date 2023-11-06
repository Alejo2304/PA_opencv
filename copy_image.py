import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img/opencv.png')
assert img is not None, "file could not be read, check with os.path.exists()"

plt.subplot(121),plt.title('Original'),plt.imshow(img, 'gray')

# Define the ROI to copy
roi = img[2:85,49:138]

# Create a copy of the ROI
roi_copy = roi.copy()

# Paste the copied ROI into a new position in the image
img[86:169, 3:92] = roi_copy
img[87:170, 93:182] = roi_copy

cv.imwrite('img/copy_image.png', img)

plt.subplot(122),plt.title('Modified'),plt.imshow(img, 'gray')
plt.show()