import io
import time
import picamera
from base_camera import BaseCamera
from picamera.array import PiRGBArray
import cv2
import cv2
from vilib import Vilib

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            # camera = PiCamera()
            camera.resolution = (320, 240)
            camera.framerate = 32
            camera.rotation = 180


            # rawCapture = PiRGBArray(camera, size=(320, 240))
            # time.sleep(2)

            # stream = io.BytesIO()
            rawCapture = PiRGBArray(camera, size=(320, 240))
            start_time = time.time()
            fpscount = 0
            Vilib.cdf_flag = True
            Vilib.hdf_flag = True
            Vilib.color_change('blue')
            print(cv2.useOptimized())
            cv2.setUseOptimized(True)
            print(cv2.useOptimized())
            for _ in camera.capture_continuous(rawCapture, format="bgr",
                                                 use_video_port=True):
                # return current frame
                # stream.seek(0)
                img = _.array
                    # img = frame.array
                t1 = cv2.getTickCount() 
                img = Vilib.color_detect_func(img) 
                img = Vilib.human_detect_func(img)
                t2 = cv2.getTickCount()
                print(round((t2-t1)/cv2.getTickFrequency(),3))
                # yield stream.read()
                yield cv2.imencode('.jpg', img)[1].tobytes()
                rawCapture.truncate(0)
                # reset stream for next frame
                # stream.seek(0)
                # stream.truncate()