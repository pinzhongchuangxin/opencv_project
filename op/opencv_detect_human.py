import numpy as np
import cv2
  
  
face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
# eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")  
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml") 
  
img = cv2.imread("666.jpg")  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
                      
# faces = face_cascade.detectMultiScale(gray,1.3,5,cv2.CASCADE_SCALE_IMAGE,(50,50),(100,100))
faces = face_cascade.detectMultiScale(gray,1.3,5,minSize=(20, 20)) 
  
if len(faces)>0:  
    for faceRect in faces:  
        x,y,w,h = faceRect  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)  
  
        roi_gray = gray[y:y+h,x:x+w]  
        roi_color = img[y:y+h,x:x+w]  
  
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,1,cv2.CASCADE_SCALE_IMAGE,(2,2))  
        for (ex,ey,ew,eh) in eyes:  
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)  
              
cv2.imshow("img",img)  

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()  #wait for ESC key to exit
