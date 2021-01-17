import cv2
import numpy as np
import imagestack

img = cv2.resize(cv2.imread("sample.png"),(300,300))

imgHorizontal = np.hstack((img,img))
imgVertical = np.vstack((img,img))
StackedImages=imagestack.stackImages(0.5,([img,img,img],
                             [img,img,img],
                             [img,img,img]))

cv2.imshow("Sample Horizontal Image",imgHorizontal)
cv2.imshow("Sample Vertical Image",imgVertical)
cv2.imshow("Sample Stacked Images", StackedImages)

cv2.waitKey(0)
