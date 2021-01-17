import cv2
cap = cv2.VideoCapture("sample.mp4")

while True:
    ret, img = cap.read()
    cv2.imshow("Sample Video",img)
    k = cv2.waitKey(30)
    if k == 27:
        break
    
