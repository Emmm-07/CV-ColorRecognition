import cv2
import numpy as np


def nothing(x):
    pass

# Trackbar
cv2.namedWindow("HSV Color Picker")
cv2.createTrackbar("H", "HSV Color Picker", 0, 179,nothing)
cv2.createTrackbar("S", "HSV Color Picker", 255, 255,nothing)
cv2.createTrackbar("V", "HSV Color Picker", 255, 255,nothing)

img_hsv = np.zeros((250,500,3),np.uint8)

while True:
    h = cv2.getTrackbarPos("H", "HSV Color Picker")
    s = cv2.getTrackbarPos("S", "HSV Color Picker")
    v = cv2.getTrackbarPos("V", "HSV Color Picker")

    img_hsv[:] = (h,s,v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("HSV Color Picker", img_bgr)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
