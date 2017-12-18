import cv2

listImages = ["galaxy.jpg","kangaroo.jpg","Lighthouse.jpg","MoonSun.jpg"]

for imageString in listImages:
    image = cv2.imread(imageString,0)
    resizeImage = cv2.resize(image,(100,100))
    cv2.imwrite(imageString+"resizeImage.jpg",resizeImage)
