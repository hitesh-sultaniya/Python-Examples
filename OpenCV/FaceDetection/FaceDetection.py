import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faceImage = cv2.imread("news.jpg")

grayFaceImage = cv2.cvtColor(faceImage,cv2.COLOR_BGR2GRAY)

faceRects = faceCascade.detectMultiScale(grayFaceImage,scaleFactor=1.1,minNeighbors=5)

for x,y,width,height in faceRects:
    faceImage = cv2.rectangle(faceImage,(x,y),(x+width,y+height),(0,255,0),3)

resizeFaceImage = cv2.resize(faceImage,(int(faceImage.shape[1]/3),int(faceImage.shape[0]/3)))

cv2.imshow("FaceDetection",resizeFaceImage)

cv2.waitKey(0)

cv2.destroyAllWindows()
