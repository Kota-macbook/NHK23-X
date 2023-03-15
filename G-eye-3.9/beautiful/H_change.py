import cv2
import numpy as np
import math

def change_H(img,Hi):
#    Hi=0.034439

    img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V=cv2.split(img2)

    VF=V.astype(np.float16)
    HF=H.astype(np.float32)

    V3=148-VF
    V3*=Hi

    HF=np.where(HF<=148,HF,HF+V3)

    H_Re=np.abs(HF).astype(np.uint8)

    img2=cv2.merge((H_Re,S,V))

    img3=cv2.cvtColor(img2,cv2.COLOR_HSV2BGR)

    return img3

img = cv2.imread("./test_images/de_pole3.png")
img2 = change_H(img,2.34439)

cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img2", 640, 480)

while True:
    cv2.imshow("img2",img2)
    if cv2.waitKey(1000)==27:
        break
    cv2.destroyAllWindows
    cv2.imshow("img2",img)
    if cv2.waitKey(1000)==27:
        break

cv2.destroyAllWindows