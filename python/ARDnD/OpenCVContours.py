import numpy as np
import cv2

cap = cv2.VideoCapture(1)
while(True):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
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
            #hull = cv2.convexHull(cnt)
            rect = cv2.minAreaRect(cnt)
            brect = cv2.boundingRect(cnt)
            box = cv2.cv.BoxPoints(rect)
            #box = rect
            area = cv2.contourArea(cnt)
            if area > 100:
                #objects.append(np.int0(hull))
                objects.append(np.int0(box))
            if area > maxarea:
                maxarea = area
                #boundry = np.int0(hull)
                boundry = np.int0(brect)
                cbnd=cnt
            i+=1
        
        #print boundry
        #bndleft = boundry[boundry[:,0].argmin()][0]
        #bndtop = boundry[boundry[:,1].argmin()][0]
        #bndright = boundry[boundry[:,0].argmax()][0]
        #bndbottom = boundry[boundry[:,1].argmax()][0]
        imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Include everything inside the boundry
        maskbnd = np.zeros(imgray.shape,np.uint8)
        cv2.drawContours(maskbnd,[cbnd],0,255,-1)
        final = cv2.bitwise_and(frame,frame, mask=maskbnd)
        
        bndleft = boundry[0] # Calculate limits
        bndtop = boundry[1]
        bndright = boundry[0] + boundry[2]
        bndbottom = boundry[1] + boundry[3]
        #final = cv2.add(resblue,resred)
        for object in objects: # Draw frames around objects
            objleft = object[object[:,0].argmin()][0]
            objtop = object[object[:,1].argmin()][1]
            #objleft = object[0]
            #objtop = object[1]
            if objleft > bndleft and objleft < bndright and objtop > bndtop and objtop < bndbottom: # Don't draw anything outside the boundry
                cv2.drawContours(final ,[object],0,(0, 255, 0),2)
       
        cv2.rectangle(final,(bndleft,bndtop),(bndright,bndbottom),(0,0,255),2)
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