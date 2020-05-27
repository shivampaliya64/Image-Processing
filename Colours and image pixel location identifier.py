import numpy as np
import cv2

def click_event(event, x, y , flag , param):
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ,', y)
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strXY = str(x)+', '+str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255, 255, 0), 4)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strBGR = str(blue)+','+str(green)+','+str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)
#img = np.zeros((512,512,3), np.uint8) ## to form image on black background
img = cv2.imread('lena.jpg') # You can have your own image or address within brackets
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()