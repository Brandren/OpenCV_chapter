import cv2
import numpy as np
import imagestack

cap = cv2.VideoCapture(0)
cap.set(10,50)

#cv2.imshow("Shape Image",img)
#cv2.imshow("Shape Gray Image",imgGray)
#cv2.imshow("Shape Blur Image",imgBlur)

while True:
    ret, img = cap.read()
    imgBlur = cv2.GaussianBlur(img,(7,7),30)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgBlur,50,50)
    imgBlank = np.zeros_like(img)
    
    StackedImages=imagestack.stackImages(0.5,([img,imgBlur,imgHSV],
                                          [imgGray,imgCanny,imgBlank]))

    cv2.imshow("Shape Stacked Image",StackedImages)
    k = cv2.waitKey(1)
    if k == 27:
        break
