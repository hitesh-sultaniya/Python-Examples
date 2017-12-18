import cv2,time

video = cv2.VideoCapture(0)


while True:
    check, frame = video.read()

    grayFace = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing",frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break



video.release()

cv2.destoryAllWindows()
