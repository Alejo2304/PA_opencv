import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


#crear graficos con matplotlib
#plt.title("Sports Watch Data"),plt.xlabel("Average Pulse"),plt.ylabel("Calorie Burnage")
plt.subplot(3,1,1)
plt.plot(x, y), plt.title('Mamaguevazo')


#Trabajar con Imagenes
img = cv.imread('./img/img1.jpeg')
plt.subplot(3,1,3)
plt.imshow(img,'gray'), plt.title('Test 1')

plt.show()

