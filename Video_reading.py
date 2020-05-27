import cv2
import requests
import urllib.request
import numpy as np
import time
cap=cv2.VideoCapture(0)
url="http://192.168.43.1:8080/shot.jpg"
while True:
    img_resp=requests.get(url)
    img_array=np.array(bytearray(img_resp.content),dtype=np.uint8)
    img=cv2.imdecode(img_array, 0)

    cv2.imshow("AndroidCam", img)

    if cv2.waitKey(1) == 27:
        break