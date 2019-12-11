from flask_camera import web_camera_start
from camera import Camera
import time
import threading
from vilib import Vilib

Vilib.cdf_flag = True
# Vilib.hdf_flag = True
Vilib.color_change('red') 


# def forever_threading():
#     while True:
#         forever()

def forever():
    last_time = time.time()
    time.sleep(1)
    sub_time = time.time() - last_time
    print(sub_time)

if __name__ == '__main__':
    Vilib.threading_start_with(web_camera_start,forever)
    while True:
        print('end')
    
    # t1 = threading.Thread(target=web_camera_start)  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    # t1.start() #线程执行
    # t2 = threading.Thread(target=forever_threading) #这里就是创建了一个线程对象t2
    # t2.start()
    


