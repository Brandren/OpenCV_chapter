import cv2
import numpy as np
import imagestack

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 400:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Sqrt"
                else:
                    objectType = "Rect"
            elif objCor == 5:
                objectType = "Penta"
            elif objCor == 6:
                objectType = "Hexa"
            elif objCor == 7:
                objectType = "Hepta"
            elif objCor == 8:
                objectType = "Cir"
            elif objCor == 9:
                objectType = "Nona"
            elif objCor == 10:
                objectType = "Deca"
            else:
                objectType = "None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-26,y+(h//2)-4),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

path = "shape.jpg"

img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)

#cv2.imshow("Shape Image",img)
#cv2.imshow("Shape Gray Image",imgGray)
#cv2.imshow("Shape Blur Image",imgBlur)

StackedImages=imagestack.stackImages(0.6,([img,imgGray,imgBlur],
                                          [imgCanny,imgContour,imgBlank]))

cv2.imshow("Shape Stacked Image",StackedImages)
cv2.waitKey(0)
