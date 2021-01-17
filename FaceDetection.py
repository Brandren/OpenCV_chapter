import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
print("Open Webcam")
while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
    cv2.imshow('Face Detection',img)
    k = cv2.waitKey(30)
    if k == 27:
        print("Close Webcam")
        break

cap.release()
cv2.destroyAllWindows()
