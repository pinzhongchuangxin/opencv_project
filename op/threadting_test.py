import time
from vilib import Vilib
# from ezblock import Servo,PWM
# from robothat import *
import numpy as np
# from keyborad_control import car_start
# from camera import Camera

# dir_Servo = Servo(PWM("P0"))
# cam_Servo_x = Servo(PWM("P1"))
# cam_Servo_y = Servo(PWM("P2"))

# cam_Servo_x.angle(0)
# cam_Servo_y.angle(0)
# dir_Servo.angle(0)

# cam_coor_x = 0
# cam_coor_y = 0
# car_dir_angle = 0


Vilib.cdf_flag = True
Vilib.hdf_flag = True
Vilib.color_change('blue')
# car_start()
Vilib.camera_start() 

# def motion_control(coor):
#     global cam_coor_x,cam_coor_y,car_dir_angle
#     time_delay = 0.03
#     stop_width_list =[25,20]

#     sub_list = np.array([0,0])
#     add_list = np.array([0,0])
#     center_coor = np.array([160,120])

#     add_list = center_coor + stop_width_list  
#     sub_list = center_coor - stop_width_list 
    
#     if coor[0] > add_list[0]: 
#         cam_coor_x +=2
#         if cam_coor_x > 90:
#             cam_coor_x = 90
#         cam_Servo_x.angle(-1*cam_coor_x)
#         dir_Servo.angle(int(cam_coor_x/2.0))  
#         time.sleep(time_delay)

#     if coor[1] > add_list[1]:
#         cam_coor_y +=2
#         if cam_coor_y > 0:
#             cam_coor_y = 0

#         cam_Servo_y.angle(cam_coor_y)
#         time.sleep(time_delay)

#     if coor[0] <= sub_list[0]:
#         cam_coor_x -=2
#         if cam_coor_x < -89:
#             cam_coor_x = -89
   
#         cam_Servo_x.angle(-1*cam_coor_x)
#         dir_Servo.angle(int(cam_coor_x/2.0))  
#         time.sleep(time_delay)

#     if coor[1] <= sub_list[1]:
#         cam_coor_y -=2
#         if cam_coor_y < -90:
#             cam_coor_y = -90
   
#         cam_Servo_y.angle(cam_coor_y) 
#         time.sleep(time_delay)

#     # if coor[0] <= sub_list[0]:
#     #     car_dir_angle -=5
#     #     if car_dir_angle < -45:
#     #         car_dir_angle = -45
   
#     #     dir_Servo.angle(car_dir_angle) 
#     #     time.sleep(0.03)

#     # if coor[0] > add_list[0]:
#     #     car_dir_angle +=5
#     #     if car_dir_angle > 45:
#     #         car_dir_angle = 45

#     #     dir_Servo.angle(car_dir_angle)
#     #     time.sleep(0.03) 
    
    # if coor[0] == 160 and coor[1] == 120:
    #     set_motor_speed(1,0)
    #     set_motor_speed(2,0)
    # else:
    #     set_motor_speed(1,-50)
    #     set_motor_speed(2,-50)   

while True:
    pass
    # motion_control(Vilib.color_object_coor)
    # cam_Servo_x.angle(-45)
    # cam_Servo_y.angle(-45)
    # print(Vilib.color_object_coor)
    # time.sleep(0.5)
    # t+=1 
    # print(Camera.rt_img)
    # if t>10:
    #     print('red')
        # Vilib.color_change('red')
    #     if t>20:
    #         t = 0
    # else:
    #     print('blue')
        # Vilib.color_change('blue')
 
# print ("Exiting Main Thread")