import cv2
import numpy as np


frameWidth = 640
framHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, framHeight)
cap.set(10, 150)

# Unfortunately depend of your camera quality,
# you need to adjust different values for different illuminations

# to be use during the night
myColors = [[0, 120, 109, 14, 255, 255],
            [0, 129, 141, 179, 255, 255]]

# to be use during the evening
# myColors = [[0, 109, 136, 88, 255, 255],
#            [0, 83, 25, 18, 255, 255]]


def findcolor(img, myColors):
    imgSHV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgSHV, lower, upper)
        getContours(mask)


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 600:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 255), 3)


while True:
    sucess, img = cap.read()
    imgResult = img.copy()
    findcolor(img, myColors)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


