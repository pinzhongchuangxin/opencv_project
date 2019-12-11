# import picar_4wd as fc
import sys
import tty
import termios
import asyncio
from ezblock import Servo,PWM,Pin
import threading
import time
import numpy as np

power_val = 50
key = 'status'
p1 = PWM('P12')
p2 = PWM('P13')

dir_Servo = Servo(PWM("P0"))
cam_Servo_x = Servo(PWM("P1"))
cam_Servo_y = Servo(PWM("P2"))

cam_Servo_x.angle(0)
cam_Servo_y.angle(0)
dir_Servo.angle(0)

cam_key_x = 0
cam_key_y = 0
car_dir_angle = 0
key = 'e'
left_rear_dir_pin = Pin("D4")
right_rear_dir_pin = Pin("D5")

def motion_control():
    global cam_key_x,cam_key_y,car_dir_angle
    time_delay = 0.03
    stop_width_list =[25,20]

    sub_list = np.array([0,0])
    add_list = np.array([0,0])
    center_key = np.array([160,120])

    # add_list = center_key + stop_width_list  
    # sub_list = center_key - stop_width_list 
    while True:
        # print("key： ",key)
        # print(cam_key_x)
        if key == 'd': 
            cam_key_x +=2
            if cam_key_x > 90:
                cam_key_x = 90
            cam_Servo_x.angle(-1*cam_key_x)
            dir_Servo.angle(int(cam_key_x/2.0))  
            time.sleep(time_delay)

        elif key == '8':
            cam_key_y +=2
            if cam_key_y > 0:
                cam_key_y = 0

            cam_Servo_y.angle(cam_key_y)
            time.sleep(time_delay)

        elif key == 'a':
            cam_key_x -=2
            if cam_key_x < -89:
                cam_key_x = -89
    
            cam_Servo_x.angle(-1*cam_key_x)
            dir_Servo.angle(int(cam_key_x/2.0))  
            time.sleep(time_delay)

        elif key == '2':
            cam_key_y -=2
            if cam_key_y < -90:
                cam_key_y = -90
    
            cam_Servo_y.angle(cam_key_y) 
            time.sleep(time_delay)
        # elif key == ''
        if key == 'q':
            break

  


def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)

def Keyborad_control():
    while True:
        global power_val,key
        key=readkey() 
        # print(key)
        if key=='q':
            print("quit")
            break
 

def hh():
    global key
    s_time = time.time()
    while True:
        # print("hh：",key)
        if key == 'w':
            left_rear_dir_pin.value(0)
            right_rear_dir_pin.value(1)
            p1.pulse_width_percent(75)
            p2.pulse_width_percent(75)
            # key = 'no'
        elif key == 's':
            left_rear_dir_pin.value(1)
            right_rear_dir_pin.value(0)
            p1.pulse_width_percent(75)
            p2.pulse_width_percent(75)
            # key = 'no'
        elif key == 'e':
            p1.pulse_width_percent(0)
            p2.pulse_width_percent(0)
        if time.time() - s_time >=0.5:
            s_time = time.time()
            key = 'e'
            time.sleep(0.5)
        if key=='q':
            p1.pulse_width_percent(0)
            p2.pulse_width_percent(0)
            break
            # print("quit")  

def car_start():
    global key
    t1 = threading.Thread(target=Keyborad_control)  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    #线程执行
    t2 = threading.Thread(target=hh)  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1motion_control(key)
    t3 = threading.Thread(target=motion_control)
    t1.start()
    # t2.start() #线程执行
    t3.start() #线程执行
if __name__ == '__main__':
    car_start()




