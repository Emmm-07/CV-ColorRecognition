# https://www.youtube.com/watch?v=t71sQ6WY7L4&t=1311s

import cv2

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h =  image.shape[0]
    w = image.shape[1]

    cX = int(w / 2)
    cY = int(h / 2)

    # Setup color identifier in the center
    pixel_center_hsv = hsv_frame[cY, cX]
    print(pixel_center_hsv)
    h ,s ,v = pixel_center_hsv

    if v < 35:
        color = "BLACK"
    elif s < 35:
        if v <200:
            color="GRAY"
        else:
            color="WHITE"
    elif h < 5:
        color="RED"
    elif h < 22:
        color="ORANGE"
    elif h < 33:
        color="YELLOW"
    elif h < 78:
        color = "GREEN"  
    elif h < 131:
        color = "BLUE"  
    elif h < 167:
        color = "VIOLET" 
    else:
        color="RED" 


    pixel_center_bgr = image[cY,cX]
    b ,g , r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.putText(image, text=color,org=(10,50), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(b,g,r),thickness=2)
    cv2.putText(image, text="Position the object on the center",org=(190,15), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(255,255,255),thickness=1)
    cv2.circle(image, (cX,cY), radius=5 , color=(0,0,0), thickness=2)
    

    cv2.imshow("Image", image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

