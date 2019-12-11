import numpy as np
import cv2
import time

def rotate(image, angle, center = None, scale = 1.0):

    (h, w) = image.shape[:2]

    if center is None:
            center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated 

cap = cv2.VideoCapture(0)
fps=int(cap.get(cv2.CAP_PROP_FPS))
print("fps: ",fps)
# print(cap.get(cv2.CAP_PROP_BUFFERSIZE))
fpscount = 0
start_time = time.time()
while 1:
    ret, img = cap.read()
    img = rotate(img, 180, center = None, scale = 1.0)
    # cv2.imshow('img',img)
    # fpscount += 1
    # if (time.time()- start_time) >= 1:
    #     print(fpscount)
    #     start_time = time.time()
    #     fpscount = 0
    # img = cv2.resize(img, (320,240), interpolation=cv2.INTER_CUBIC)
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows() 