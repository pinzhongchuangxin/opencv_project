import cv2
import numpy as np

capture = cv2.VideoCapture(0)


kernel_2 = np.ones((2,2),np.uint8)#2x2的卷积核
kernel_3 = np.ones((3,3),np.uint8)#3x3的卷积核
kernel_4 = np.ones((4,4),np.uint8)#4x4的卷积核
kernel_8 = np.ones((8,8),np.uint8)#8x8的卷积核
kernel_20 = np.ones((20,20),np.uint8)#20x20的卷积核

# erosion_count = 2      #腐蚀的次数
# dilation_count = 2     #膨胀的次数

def Rgb_convert_Hsv(rgb=[0,0,0]):
    R,G,B = rgb[0]/255.0,rgb[1]/255.0,rgb[2]/255.0
    max_val = max(R,G,B)
    min_val = min(R,G,B) 
    if (max_val-min_val) != 0:
        if R == max_val:
            H = (G-B)/float(max_val-min_val)
        if G == max_val:
            H = 2 + (B-R)/float(max_val-min_val)
        if B == max_val:
            H = 4 + (R-G)/float(max_val-min_val)

        H = int(H * 30)
        if H < 0:
            H = H + 180
        V=int(max(R,G,B)*255)
        S=int((max_val-min_val)/max_val*255)
        
        # HSV_list = []
        # HSV_list.append(H)
        # HSV_list.append(int(S*255))
        # HSV_list.append(int(V*255))
        # return HSV_list
        return H,S,V
    else:
        return 0,0,max_val

def color_div(color_num=6):
    return int(180.0/color_num)



def string_convert_hsv(color_default = 'blue'):
    # color_basic = color_div()
    kernel_4 = np.ones((4,4),np.uint8)#20x20的卷积核

    erosion_count = 1      #腐蚀的次数
    dilation_count = 1     #膨胀的次数

    color_dict = {'red':[0,4],'orange':[7,20],'yellow':[21,37],'green':[42,85],'blue':[92,107],'purple':[115,160]}
    # color_dict = {'red':[0,4],'orange':[7,20],'yellow':[21,37],'green':[42,85],'blue':[100,124],'purple':[115,160]}

    lower_color = np.array([min(color_dict[color_default]), 105, 90])  
    upper_color = np.array([max(color_dict[color_default]), 255, 255])

    # 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度

    while(True):
        
        ret, frame = capture.read()           # 1.捕获视频中的一帧
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
        
        mask = cv2.inRange(hsv, lower_color, upper_color)           # 3.inRange()：介于lower/upper之间的为白色，其余黑色             
        
        mask = cv2.GaussianBlur(mask, (7, 7), 0)          #高斯滤波

        erosion = cv2.erode(mask,kernel_4,iterations = erosion_count)                    #腐蚀
        dilation = cv2.dilate(erosion,kernel_4,iterations = dilation_count)              #膨胀             
        
        res = cv2.bitwise_and(frame, frame, mask=dilation)                  ####与操作，只保留原图中的蓝色部分

        ret, binary = cv2.threshold(dilation,127,255,cv2.THRESH_BINARY)     ####把图片变为二值图放在binary里面

        contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          ####在binary中发现轮廓，轮廓按照面积从小到大排列
        # p=0
        for i in contours:    #遍历所有的轮廓
            x,y,w,h = cv2.boundingRect(i)      #将轮廓分解为识别对象的左上角坐标和宽、高
            #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
            if w > 15 and h > 15: 
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                    #给识别对象写上标号
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,color_default,(x-10,y+10), font, 1,(0,0,255),2)#加减10是调整字符位置
        #    p +=1

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', binary)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__=='__main__':
    string_convert_hsv('blue')

