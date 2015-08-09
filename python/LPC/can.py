import numpy as np
import cv2
import cv2.cv as cv
 
def nothing(no):
  no=1

cap = cv2.VideoCapture(0)

cv2.namedWindow("controls")
cv.CreateTrackbar("smax", "controls", 190, 255, nothing)
cv.CreateTrackbar("smin", "controls", 140, 255, nothing)
cv.CreateTrackbar("vmax", "controls", 190, 255, nothing)
cv.CreateTrackbar("vmin", "controls", 140, 255, nothing)
cv.CreateTrackbar("ehigh", "controls", 190, 5000, nothing)
cv.CreateTrackbar("elow", "controls", 140, 5000, nothing)
while(True):
    smax = cv2.getTrackbarPos("smax", "controls")
    smin = cv2.getTrackbarPos("smin", "controls")
    vmax = cv2.getTrackbarPos("vmax", "controls")
    vmin = cv2.getTrackbarPos("vmin", "controls")
    elow = cv2.getTrackbarPos("elow", "controls")
    ehigh = cv2.getTrackbarPos("ehigh", "controls")
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_black = np.array([0,smin,vmin])
    upper_black = np.array([255,smax,vmax])

    # Threshold the HSV image to get only black colors
    maskblack = cv2.inRange(hsv, lower_black, upper_black)
    # Invert the image to get only the light colors

    black = cv2.bitwise_and(frame,frame, mask=maskblack)
    hsv = cv2.bitwise_and(hsv,hsv, mask=maskblack)
    amaskblack = cv2.bitwise_not(maskblack)

    ablkcontours, ablkhierarchy = cv2.findContours(amaskblack,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = np.zeros(imgray.shape,np.uint8)
    if len(ablkcontours) != 0:
        for cnt in ablkcontours:
          area = cv2.contourArea(cnt)
          if area > elow and area < ehigh:
            cv2.drawContours(edges,[cnt],0,255,-1)
            
    cv2.imshow('frame',frame)
    cv2.imshow('gray',hsv)
    cv2.imshow('black',black)
    cv2.imshow('edges',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print smax, smin, vmax, vmin, elow, ehigh
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("frame.png", frame)
        cv2.imwrite("gray.png", hsv)
        cv2.imwrite("black.png", black)
        cv2.imwrite("edges.png",edges)
        print smax, smin, vmax, vmin, elow, ehigh
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
