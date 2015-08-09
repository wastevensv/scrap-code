import numpy as np
import cv2

cap = cv2.VideoCapture(1)
while(True):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([80,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    resblue = cv2.bitwise_and(frame,frame, mask= maskblue)

    # define range of blue color in HSV
    #lower_red = np.array([20,50,50])
    #upper_red = np.array([40,255,255])

    # Threshold the HSV image to get only blue colors
    #maskred = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    #resred = cv2.bitwise_and(frame,frame, mask= maskred)
    
    #mask = cv2.add(maskblue,maskred)
    
    #contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(maskblue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    final = resblue
    if len(contours) != 0:
        
        boundry = contours[0]
        objects=[]
        
        maxarea = 200
        i=0
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            box = cv2.cv.BoxPoints(rect)
            area = cv2.contourArea(cnt)
            M = cv2.moments(cnt)
            if area > maxarea:
                maxarea = area
                boundry = np.int0(box)
            elif area > 250 and area < 10000:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                c = (cx, cy)
                objects.append(c)
                #print objects, area
            i+=1
        
        #final = cv2.add(resblue,resred)
        
        for object in objects:
            cv2.circle(final,object, 10, (0,255,0), -1)
       
        cv2.drawContours(final ,[boundry],0,(0, 0, 255),2)
        #result = cv2.drawContours(final, contours, -1, (0,255,0), 3)
        
    cv2.imshow('frame',frame)
    
    cv2.imshow('mask - blue',maskblue)
    cv2.imshow('res - blue',resblue)
    
    #cv2.imshow('mask - red',maskred)
    #cv2.imshow('res - red',resred)
    
    #cv2.imshow('mask - final',mask)
    cv2.imshow('final',final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()