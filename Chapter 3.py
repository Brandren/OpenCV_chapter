import cv2
cap = cv2.VideoCapture(0)
cap.set(10,50)

while True:
    ret, img = cap.read()
    cv2.imshow("Webcam",img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
