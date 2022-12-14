import numpy as np
import sys
import cv2

image=cv2.imread("C:/Users/karan/Desktop/P/Digital Recognition/test_lyst7894.png")

image1=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
thresh=cv2.adaptiveThreshold(blur,255,1,1,11,2)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

samples=np.empty((0,100),np.float32)
responses=[]

keys=[i for i in range(48,58)]

for cnt in contours:

    if cv2.contourArea(cnt)<50:
        [x,y,w,h]=cv2.boundingRect(cnt)

        if h>28:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            roi=thresh[y:y+h,x:x+w]
            roismall+cv2.resize(roi,(10,10))
            cv2.imshow("norm",image)

            key=cv2.waitKey(0)

            if key==27:
                sys.exit()
            elif key in keys():
                responses.append(int(chr(key)))
                sample=roismall.reshape((1,100))
                samples=np.append(damples,sample,0)

responses=np.array(responses,np.float32)
responses= responses.reshape((responses.size,1))
print("Training Complete")

samples=np.float32(samples)
responses=np.float32(responses)

cv2.imwrite("Train_result.png",image)
np.savetxt("generalsamples.data",samples)
np.savetxt("generalresponses.data",responses)
