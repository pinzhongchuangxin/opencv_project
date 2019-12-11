import cv2
import time

# ip_camera_url = 'http://admin:admin@192.168.18.37:8081/'
ip_camera_url = 'http://192.168.6.245:9000/mjpg'
# 创建一个窗口
# cv2.namedWindow('ip_camera', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

cap = cv2.VideoCapture(ip_camera_url)
# cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
cap.set(3,320)
cap.set(4,240)
if not cap.isOpened():
    print('请检查IP地址还有端口号，或者查看IP摄像头是否开启，另外记得使用sudo权限运行脚本')

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('ip_camera', frame)


    if cv2.waitKey(1) == ord('q'):
        # 退出程序
        break

# cv2.destroyWindow('ip_camera')
# cap.release()