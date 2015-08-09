import numpy as np
import cv2

cap = cv2.VideoCapture(2)
while(True):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in BGR
    lower_blue = np.array([140,0,0])
    upper_blue = np.array([255,100,100])

    # Threshold the HSV image to get only blue colors
    maskblue = cv2.inRange(frame, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    resblue = cv2.bitwise_and(frame,frame, mask= maskblue)

    # define range of blue color in BGR
    lower_red = np.array([0,0,140])
    upper_red = np.array([100,100,255])

    # Threshold the HSV image to get only blue colors
    maskred = cv2.inRange(frame, lower_red, upper_red)

    # Bitwise-AND mask and original image
    resred = cv2.bitwise_and(frame,frame, mask= maskred)
    
    mask = cv2.add(maskblue,maskred)
    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    boxes=[]
    i=0
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        area = cv2.contourArea(cnt)
        if area > 100:
            boxes.append(np.int0(hull))
        i+=1
    
    final = cv2.add(resblue,resred)
    
    for box in boxes:
        cv2.drawContours(final ,[box],0,(0,0,255),2)
    #result = cv2.drawContours(final, contours, -1, (0,255,0), 3)
    
    cv2.imshow('frame',frame)
    
    cv2.imshow('mask - blue',maskblue)
    cv2.imshow('res - blue',resblue)
    
    cv2.imshow('mask - red',maskred)
    cv2.imshow('res - red',resred)
    
    cv2.imshow('mask - final',mask)
    cv2.imshow('final',final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()