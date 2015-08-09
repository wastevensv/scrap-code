import numpy as np
import cv2

seen = False
lastseen = (0,0)
lostfor = 0
seenfor = 0
cap = cv2.VideoCapture(0)

#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, int(1280))
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, int(1024))
while(True):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_black = np.array([0,0,0])
    upper_black = np.array([255,255,120])

    # Threshold the HSV image to get only black colors
    maskblack = cv2.inRange(hsv, lower_black, upper_black)
    # Invert the image to get only the light colors
    antiblack = cv2.bitwise_not(maskblack)

    # Detect contours in both images.
    ablkcontours, ablkhierarchy = cv2.findContours(antiblack,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    blkcontours, blkhierarchy = cv2.findContours(maskblack,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # If there are black contours, set the boundary to the biggest one.
    if len(blkcontours) != 0:
        boundry = blkcontours[0]
        bxboundry = ((0,0),(0,10),(10,0),(10,10))
        maxarea = -1
        i=0
        for cnt in blkcontours:
            rect = cv2.minAreaRect(cnt)
            box = cv2.cv.BoxPoints(rect)
            box=np.int0(box)
            area = cv2.contourArea(cnt)
            M = cv2.moments(cnt)
            if abs(area) > maxarea:
                maxarea = abs(area)
                boundry = cnt
                i+=1

    # Create mask image with only the boundary
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    maskbnd = np.zeros(imgray.shape,np.uint8)
    cv2.drawContours(maskbnd,[boundry],0,255,-1)

    if len(ablkcontours) != 0:
        for cnt in ablkcontours:
            cv2.drawContours(antiblack,[cnt],0,255,-1)

    finalmask = cv2.bitwise_and(maskbnd, antiblack) # Include everything inside the boundary

    contours, hierarchy = cv2.findContours(finalmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        point = (0,0)
        maxarea = -1
        i=0
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            box = cv2.cv.BoxPoints(rect)
            area = cv2.contourArea(cnt)
            M = cv2.moments(cnt)
            cx = int((box[1][0]+box[3][0])/2)
            cy = int((box[1][1]+box[3][1])/2)
            c = (cx, cy)
            if abs(area) > maxarea and abs(area) > 50:
                maxarea = area
                point = c
                i+=1
                
        if(i > 0):
            if(lostfor == 1):
                cv2.imwrite("lostframe.png",frame)
            elif(lostfor in range(20,40)):
                print "\n LCLICK"
            elif(lostfor in range(40,60)):
                print "\n RCLICK"
            elif(lostfor>50):
                print
            elif(lostfor>0):
                print "lost @ "+str(lastseen)+" for "+str(lostfor)+" frames       \r"
            lostfor=0
            lastseen = point
            print "seen @ "+str(lastseen)+"       \r",
        else:
            lostfor+=1
            print "lost @ "+str(lastseen)+" for "+str(lostfor)+" frames       \r",
    else:
        if(lostfor==0): print
        lostfor+=1
        print "lost @ "+str(lastseen)+" for "+str(lostfor)+" frames       \r",



    finalmask = cv2.bitwise_and(maskbnd, antiblack)
    final = cv2.bitwise_and(frame,frame, mask=finalmask)

    cv2.circle(final,lastseen, 10, (0,255,0), -1)
    cv2.polylines(final ,[boundry],1,(0, 0, 255),2)

    cv2.imshow('frame',frame)
    cv2.imshow('mask - final',finalmask)
    cv2.imshow('final',final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
