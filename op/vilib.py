import numpy as np
import cv2
import threading

class Vilib(object): 
    
    # camera = cv2.VideoCapture(Camera.video_source)

    # camera.set(3,320)
    # camera.set(4,240)
    # camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
    kernel_5 = np.ones((5,5),np.uint8)#4x4的卷积核
    color_default = 'blue'
    color_dict = {'red':[0,4],'orange':[7,20],'yellow':[21,37],'green':[42,85],'blue':[92,124],'purple':[115,160]}
    lower_color = np.array([min(color_dict[color_default]), 105, 90])  
    upper_color = np.array([max(color_dict[color_default]), 255, 255])
    hdf_flag = False 
    cdf_flag = False
    stf_flag = False
    
    human_object_counter = 0
    human_object_coor = np.array([160,120])
    human_object_size = np.array([0,0]) 

    color_object_counter = 0
    color_object_coor = np.array([160,120])
    color_object_size = np.array([0,0])  
    # object_shape_type = "circles"
    
    # @staticmethod
    # def contours_detect_func(img):
    #     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #     ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    #     # cv.imshow("input image", img)
    #     out_binary, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #     for cnt in range(len(contours)):
    #         # 提取与绘制轮廓
    #         cv.drawContours(result, contours, cnt, (0, 255, 0), 2)
    #         # 轮廓逼近
    #         epsilon = 0.01 * cv.arcLength(contours[cnt], True)
    #         approx = cv.approxPolyDP(contours[cnt], epsilon, True)

    #         # 分析几何形状
    #         corners = len(approx)
    #         shape_type = ""
    #         if corners == 3:
    #             count = self.shapes['triangle']
    #             count = count+1
    #             self.shapes['triangle'] = count
    #             shape_type = "triangle"
    #         if corners == 4:
    #             count = self.shapes['rectangle']
    #             count = count + 1
    #             self.shapes['rectangle'] = count
    #             shape_type = "rectangle"
    #         if corners >= 10:
    #             count = self.shapes['circles']
    #             count = count + 1
    #             self.shapes['circles'] = count
    #             shape_type = "circles"
    #         if 4 < corners < 10:
    #             count = self.shapes['polygons']
    #             count = count + 1
    #             self.shapes['polygons'] = count
    #             shape_type = "polygons"
    #     return img
    @staticmethod
    def color_detect_object_parameter(obj_parameter):
        if obj_parameter == 'x':
            return int(Vilib.color_object_coor[0]/107.0)-1   #max_size_object_coordinate_x
        elif obj_parameter == 'y':
            return int(Vilib.color_object_coor[1]/80.1)-1   #max_size_object_coordinate_y
        elif obj_parameter == 'w':
            return Vilib.color_object_size[0]   #objects_max_width
        elif obj_parameter == 'h':
            return Vilib.color_object_size[1]   #objects_max_height
        elif obj_parameter == 'num':      
            return Vilib.color_object_counter   #objects_count
        return None

    @staticmethod
    def human_detect_object_parameter(obj_parameter):
        if obj_parameter == 'x':
            return int(human_object_coor[0]/107.0)-1
        elif obj_parameter == 'y':
            return int(human_object_coor[1]/80.1)-1
        elif obj_parameter == 'w':
            return human_object_size[0]
        elif obj_parameter == 'h':
            return human_object_size[1]
        elif obj_parameter == 'num':      
            return Vilib.human_object_counter   #objects_count
        return None

    @staticmethod
    def color_change(color_name):
        Vilib.color_default = color_name
        Vilib.lower_color = np.array([min(Vilib.color_dict[color_name]), 105, 90])  
        Vilib.upper_color = np.array([max(Vilib.color_dict[color_name]), 255, 255])

    @staticmethod
    def camera_start(web_func = True):
        if web_func == True:
            from flask_camera import web_camera_start
            t1 = threading.Thread(target=web_camera_start)  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
            t1.start() #线程执行
        


    @staticmethod
    def human_detect_func(img):
        if Vilib.hdf_flag == True:
            resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR) 
            gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY) 
            faces = Vilib.face_cascade.detectMultiScale(gray, 1.3, 5)
            Vilib.human_object_counter = len(faces)
            max_area = 0
            if Vilib.human_object_counter > 0:
                for (x,y,w,h) in faces:
                    x = x*2
                    y = y*2
                    w = w*2
                    h = h*2
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    object_area = w*h
                    if object_area > max_area: 
                        object_area = max_area
                        Vilib.human_object_coor[0] = x + w/2
                        Vilib.human_object_coor[1] = y + h/2
                        Vilib.human_object_size[0] = w
                        Vilib.human_object_size[1] = h
            return img
        else:
            return img

    @staticmethod
    def color_detect_func(img):

        # 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度
        if Vilib.cdf_flag == True:
            resize_img = cv2.resize(img, (80,60), interpolation=cv2.INTER_LINEAR)
            hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
            # print(Vilib.lower_color)
            mask = cv2.inRange(hsv, Vilib.lower_color, Vilib.upper_color)           # 3.inRange()：介于lower/upper之间的为白色，其余黑色             
                
            # mask = cv2.GaussianBlur(mask, (7, 7), 0)          #高斯滤波
          
            # ret, binary = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)     ####把图片变为二值图放在binary里面

            open_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN,Vilib.kernel_5,iterations=1)              #开运算  

            contours, hierarchy = cv2.findContours(open_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          ####在binary中发现轮廓，轮廓按照面积从小到大排列
                # p=0
            Vilib.color_object_counter = len(contours)
            max_area = 0

            if Vilib.color_object_counter > 0: 
                for i in contours:    #遍历所有的轮廓
                    x,y,w,h = cv2.boundingRect(i)      #将轮廓分解为识别对象的左上角坐标和宽、高

                        #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
                    if w > 5 and h > 5: 
                        x = x*4
                        y = y*4
                        w = w*4
                        h = h*4
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                                #给识别对象写上标号
                        cv2.putText(img,Vilib.color_default,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)#加减10是调整字符位置
 
                        object_area = w*h
                        if object_area > max_area: 
                            object_area = max_area
                            Vilib.color_object_coor[0] = x + w/2
                            Vilib.color_object_coor[1] = y + h/2
                            Vilib.color_object_size[0] = w
                            Vilib.color_object_size[1] = h
            else:
                Vilib.color_object_coor = np.array([160,120])
                Vilib.color_object_size = np.array([0,0])
            return img
        else:
            return img
