import socket
import Image
import numpy as np
import cv2

cam = cv2.VideoCapture(0)
# cam.setResolution(320,240)
clisocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
    ret, img = cam.read()
    result, imgencode = cv2.imencode('.jpg', frame)
    data = numpy.array(imgencode)
    stringData = data.tostring()
#   im = im.resize((160,120))
#   da = im.tostring()
    clisocket.sendto(da, ("127.0.0.1", 1234))
s.close()