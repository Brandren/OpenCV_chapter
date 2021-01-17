import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
first_img = cv2.resize(cv2.imread("sample.png"),(300,300))
second_img = cv2.resize(cv2.imread("sample2.jpg"),(300,300))
third_img = cv2.resize(cv2.imread("sample3.png"),(750,590))

first_gray = cv2.cvtColor(first_img,cv2.COLOR_BGR2GRAY)
first_faces = face_cascade.detectMultiScale(first_gray, 1.5, 4)
for (x,y,w,h) in first_faces:
        cv2.rectangle(first_img,(x,y),(x+w,y+h),(255,0,0),5) 
cv2.imshow("Sample Face Detection Image", first_img)

second_gray = cv2.cvtColor(second_img,cv2.COLOR_BGR2GRAY)
second_faces = face_cascade.detectMultiScale(second_gray, 1.5, 4)
for (x,y,w,h) in second_faces:
        cv2.rectangle(second_img,(x,y),(x+w,y+h),(255,0,0),5) 
cv2.imshow("Sample Face Detection Image 2", second_img)


third_gray = cv2.cvtColor(third_img,cv2.COLOR_BGR2GRAY)
third_faces = face_cascade.detectMultiScale(third_gray, 1.5, 4)
for (x,y,w,h) in third_faces:
        cv2.rectangle(third_img,(x,y),(x+w,y+h),(255,0,0),5) 
cv2.imshow("Sample Face Detection Image 3", third_img)


cv2.waitKey(0)

