import numpy as np
import cv2

def myfunc(i):
    pass # do nothing  

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('gamma', # name of value
                   'title', # win name
                   1, # min
                   50, # max
                   myfunc) # callback func
cv2.setTrackbarPos("gamma", "title", 10)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    gamma = cv2.getTrackbarPos("gamma", "title") * 0.1
    if gamma == 0:
        gamma = 0.1
        cv2.setTrackbarPos("gamma", "title", 1)
    
    # ガンマ補正用ルックアップテーブル
    look_up_table = np.zeros((256, 1), dtype = 'uint8')
    for i in range(len(look_up_table)):
        look_up_table[i][0] = (len(look_up_table)-1) * pow(float(i) / (len(look_up_table)-1), 1.0 / gamma)
    
    # ルックアップテーブルによるガンマ補正
    gamma_correction_image = cv2.LUT(frame, look_up_table)

    ## do something by using v

    cv2.imshow('title', gamma_correction_image)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()

