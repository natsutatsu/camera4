import numpy as np
import cv2

def myfunc(i):
    pass #平均値 # do nothing


cv2.namedWindow('title') # create win with win name

cv2.createTrackbar("filter", "title", 1, 50, myfunc)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):

    ret, frame = cap.read()
    if not ret: continue
    
    fil = cv2.getTrackbarPos("filter", "title")
    
    blur = cv2.blur(frame,(fil,fil)) #平均値
    
    cv2.imshow('title', blur)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()


