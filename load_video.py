import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#video capture object
vid = cv.VideoCapture(0)

while(True):

    #capture the video frame by frame
    ret, frame = vid.read()
    #resize the frames
    frame = cv.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv.INTER_CUBIC) 
    #display the frames
    cv.imshow('Frame', frame)

    #action to close the program
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()

