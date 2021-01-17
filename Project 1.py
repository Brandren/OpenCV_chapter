import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(10,50)


myColors = [[0,131,0,48,255,255],  #Red
           [84,73,0,116,255,255], # Blue
           [0,0,0,179,255,32]]   #Black 

myColorValues = [[0,0,255],
                 [255,0,0],  #BGR
                 [0,0,0]]

myPoints = [] #[x,y,colorId]

def findColor(img,myColors,myColorValues):
        imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        count = 0
        newPoints = []
        for color in myColors:
                lower = np.array(color[0:3])
                upper = np.array(color[3:6])
                mask = cv2.inRange(imgHSV,lower,upper)
                x,y = getContours(mask)
                cv2.circle(imgResult,(x,y),10,(myColorValues[count]),cv2.FILLED)
                if x != 0 and y != 0:
                        newPoints.append([x,y,count])
                count += 1
                #cv2.imshow(str(color[1]),mask)
        return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 400:
                #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
                 peri = cv2.arcLength(cnt,True)
                 approx = cv2.approxPolyDP(cnt,0.02*peri,True)
                 x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y
    

def drawOnCanvas(myPoints,myColorValues):
        for point in myPoints:
                cv2.circle(imgResult,(point[0],point[1]),10,(myColorValues[point[2]]),cv2.FILLED)

            
while True:
    ret, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!= 0:
            for newP in newPoints:
                    myPoints.append(newP)
    if  len(myPoints)!= 0:
            drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Webcam",imgResult)
    k = cv2.waitKey(1)
    if k == 27:
        break
    

