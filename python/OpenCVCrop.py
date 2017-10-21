from __future__ import print_function
import numpy as np
import cv2
from sys import argv
from time import sleep

cap = cv2.VideoCapture(int(argv[1]))

cap.set(3, 1280);
cap.set(4, 720);

while(True):

    # Take each frame
    if not cap.isOpened():
        continue
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #mask = cv2.adaptiveThreshold(cv2.split(hsv)[2],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    _, mask = cv2.threshold(cv2.split(hsv)[2],0,1,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    
    # Threshold the HSV image to get only blue colors

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    box = None
    i = 0
    maxarea = 100
    for cnt in contours:
        epsilon = 0.1*cv2.arcLength(cnt,True)
        rect = cv2.approxPolyDP(cnt,epsilon,True)
        area = cv2.contourArea(rect)
        if area > maxarea and len(rect) == 4:
                box = np.float32(rect)
                maxarea = area
        i+=1
    
    if box is not None:
        diffx = np.int0(box[0] - box[1])
        sizex = int(cv2.magnitude(diffx[0][0], diffx[0][1])[0][0])
        diffy = np.int0(box[0] - box[2])
        sizey = int(cv2.magnitude(diffy[0][0], diffy[0][1])[0][0])
        
        dst = np.float32([[0,0],[0,sizex],[sizey,sizex],[sizey,0]])

        print(box)
        print(dst)

        print(frame.shape)
        M = cv2.getPerspectiveTransform(box, dst) 
        output = cv2.warpPerspective(frame,M,(int(sizey),int(sizex)))
        cv2.imshow('output',output)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            cv2.imwrite('frame.png',frame)
            cv2.imwrite('out.png',output)
        cv2.drawContours(frame,[np.int0(box)],0,(0,0,255),2)
        
    #result = cv2.drawContours(final, contours, -1, (0,255,0), 3)
    
    #cv2.imshow('mask',mask)
    frame = cv2.resize(frame,(frame.shape[1]/2,frame.shape[0]/2))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
