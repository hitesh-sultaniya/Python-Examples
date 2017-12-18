import cv2

image = cv2.imread("galaxy.jpg",0)

#print(type(image))
#print(image)
#print(image.shape)
#print(image.ndim)

#image = cv2.imread("galaxy.jpg",1)

#print(image.ndim)

rsizedImage = cv2.resize(image,(int(image.shape[1]/2),int(image.shape[0]/2)))
cv2.imshow("Galaxy",rsizedImage)
cv2.imwrite("Galaxy_Resized.jpg",rsizedImage)
cv2.waitKey(0)
cv2.destroyAllWindow()
