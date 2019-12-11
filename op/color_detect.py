import cv2
import numpy as np

capture = cv2.VideoCapture(0)
print("1")
class test_vi(object):
    test_img = np.ones((320,240),np.uint8)


kernel_2 = np.ones((2,2),np.uint8)#2x2的卷积核
kernel_3 = np.ones((3,3),np.uint8)#3x3的卷积核
kernel_4 = np.ones((4,4),np.uint8)#4x4的卷积核
kernel_8 = np.ones((8,8),np.uint8)#8x8的卷积核
kernel_20 = np.ones((20,20),np.uint8)#20x20的卷积核

erosion_count = 2      #腐蚀的次数
dilation_count = 2     #膨胀的次数

# 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度
lower_blue = np.array([98, 100, 100])
upper_blue = np.array([124, 255, 255])
print("2")
def main():
    while(True):
        print('start')
        ret, frame = capture.read()           # 1.捕获视频中的一帧
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)           # 3.inRange()：介于lower/upper之间的为白色，其余黑色             
        
        mask = cv2.GaussianBlur(mask, (7, 7), 0)          #高斯滤波

        erosion = cv2.erode(mask,kernel_20,iterations = erosion_count)                    #腐蚀
        erosion = cv2.erode(erosion,kernel_20,iterations = erosion_count)
        dilation = cv2.dilate(erosion,kernel_20,iterations = dilation_count)              #膨胀
        dilation = cv2.dilate(dilation,kernel_20,iterations = dilation_count)             
        
        res = cv2.bitwise_and(frame, frame, mask=dilation)                  ####与操作，只保留原图中的蓝色部分

        ret, binary = cv2.threshold(dilation,127,255,cv2.THRESH_BINARY)     ####把图片变为二值图放在binary里面

        contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          ####在binary中发现轮廓，轮廓按照面积从小到大排列
        # p=0
        for i in contours:    #遍历所有的轮廓
            x,y,w,h = cv2.boundingRect(i)      #将轮廓分解为识别对象的左上角坐标和宽、高
                #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
            if w > 15 and h > 15: 
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,),3)
                        #给识别对象写上标号
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'blue',(x-10,y+10), font, 1,(0,0,255),2)#加减10是调整字符位置
            #    p +=1
            test_vi.test_img = frame
            # cv2.imshow('frame', frame)
            # cv2.imshow('mask', mask)
            # cv2.imshow('res', res) 

if __name__ == '__main__':
    print("3")
    while True:
        main()
    print('stop')