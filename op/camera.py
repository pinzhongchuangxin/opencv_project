import os
import cv2
import numpy as np
from base_camera import BaseCamera
import time
from vilib import Vilib
# from color_detect import test_vi
# from picamera import PiCamera
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# picamera = PiCamera()
# picamera.rotation = 180

class Camera(BaseCamera):
    video_source = 0
    # rt_img = np.zeros((480,640,3),np.uint8)

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source): 
        Camera.video_source = source 
    
    # @staticmethod
    # def send_frames():
    #     while True:
    #         yield cv2.imencode('.jpg', test_vi.test_img)[1].tobytes() 


    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)

        camera.set(3,320)
        camera.set(4,240)

        width = int(camera.get(3))
        height = int(camera.get(4))

        M = cv2.getRotationMatrix2D((width / 2, height / 2), 180, 1)

        camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
        # camera.rotation = 180
        # rawCapture = PiRGBArray(camera, size=(320, 240))

        # if not camera.isOpened():
        #     raise RuntimeError('Could not start camera.')
        start_time = time.time()
        fpscount = 0
        # print(cv2.useOptimized())
        cv2.setUseOptimized(True)
        # print(cv2.useOptimized())
        while True:
            # read current frame
            
            # img = cv2.warpAffine(img, M, (640, 480))
            # print(time.time()- start_time)
            _, img = camera.read()
            img = cv2.warpAffine(img, M, (320, 240))
            img = Vilib.human_detect_func(img)         
            img = Vilib.color_detect_func(img) 
            ##  FPS           
            # fpscount += 1
            # if (time.time()- start_time) >= 1:
            #     print(fpscount)
            #     start_time = time.time()
            #     fpscount = 0
            ##  FPS 
            # start_time = time.time()
            # t1 = cv2.getTickCount()

            
            # img = Vilib.human_detect_func(img)
            # t2 = cv2.getTickCount()
            # print(int(1/round((t2-t1)/cv2.getTickFrequency(),2)))

            # img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR) 
            # img = Vilib.color_detect_func(img) 
            
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes() 