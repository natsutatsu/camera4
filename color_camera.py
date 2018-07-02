import numpy as np
import cv2

def myfunc(i):
    pass # do nothing


cv2.namedWindow('title') # create win with win name

cv2.createTrackbar("v", "title", 0, 10, myfunc)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue
    
    v = cv2.getTrackbarPos("v", "title")
    
    if(v==0):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif(v==1):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    elif(v==2):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    elif(v==3):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    elif(v==4):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
    elif(v==5):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    elif(v==6):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2BGRA)
    elif(v==7):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2Luv)
    elif(v==8):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2Lab)
    elif(v==9):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2XYZ)
    elif(v==10):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    cv2.imshow('title', i)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()


