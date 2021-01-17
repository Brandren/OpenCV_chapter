import cv2
import numpy as np
img = cv2.resize(cv2.imread("sample.png"),(300,300))
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgcolorBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Sample Image", img)
cv2.imshow("Sample Gray Image", imgGray)
cv2.imshow("Sample Blur Image", imgBlur)
cv2.imshow("Sample Color Blur Image", imgcolorBlur)
cv2.imshow("Sample Canny Image", imgCanny)
cv2.imshow("Sample Dialation Image", imgDialation)
cv2.imshow("Sample Eroded Image", imgEroded)
cv2.waitKey(0)
