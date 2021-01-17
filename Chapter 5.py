import cv2
img = cv2.imread("sample.png")
print(img.shape)

imgResize = cv2.resize(img,(300,300))
print(imgResize.shape)

imgCrop = img[0:200,200:500]
print(imgCrop.shape)

cv2.imshow("Sample Image",img)
cv2.imshow("Sample Image Resize",imgResize)
cv2.imshow("Sample Image Crop",imgCrop)
cv2.waitKey(0)
