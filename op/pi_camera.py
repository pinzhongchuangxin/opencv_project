from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from vilib import Vilib
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=(320, 240))
 
# allow the camera to warmup
time.sleep(0.1)
start_time = time.time()
fpscount = 0
# capture frames from the camera
Vilib.cdf_flag = True
Vilib.hdf_flag = True
Vilib.color_change('blue')
print(cv2.useOptimized())
cv2.setUseOptimized(True)
print(cv2.useOptimized())
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
    t1 = cv2.getTickCount() 
    img = Vilib.color_detect_func(img) 
    img = Vilib.human_detect_func(img)
    t2 = cv2.getTickCount()
    print(round((t2-t1)/cv2.getTickFrequency(),3))
    # cv2.imshow("Frame", image)
    # key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    # if key == ord("q"):
    #     break