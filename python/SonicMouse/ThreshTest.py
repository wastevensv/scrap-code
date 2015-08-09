import numpy as np
import cv2

cap = cv2.VideoCapture(1)
while(True):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,127,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    resblue = cv2.bitwise_and(frame,frame, mask= maskblue)
    
    # define range of red color in HSV
    lower_red = np.array([175,127,127])
    upper_red = np.array([200,255,255])

    # Threshold the HSV image to get only blue colors
    maskred = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    resred = cv2.bitwise_and(frame,frame, mask= maskred)
    
    mask = cv2.add(maskblue,maskred)
    res = cv2.add(resblue,resred)
    
    cv2.imshow('frame',frame)
    
    cv2.imshow('mask - blue',maskblue)
    cv2.imshow('mask - red',maskred)
    
    cv2.imshow('final',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break