# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:38:10 2016

@author: farmer
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 22:11:54 2016

@author: Administrator
"""

import os
import time
import cv2
#imagePath = sys.argv[1]
#imagePath = "G:\\boy_girl.jpg"
#imagePath = "G:\\all_star.jpg"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("F:\\\
opencv2\\opencv\\sources\\data\\haarcascades\\\
haarcascade_frontalface_default.xml") #1
noseCascade = cv2.CascadeClassifier("F:\\\
opencv2\\opencv\\sources\\data\\haarcascades\\\
haarcascade_mcs_nose.xml")
# Read the image
pic_l=[]
def pic_names(path):
    for i in os.listdir(path):
        yield ("g:\\face\\"+i)
pictures=list(pic_names("g:\\face\\"))
print "*******************************************************"
for i in range(len(pictures)):
    image = cv2.imread(pictures[i])#2
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#3
    # Detect faces in the image
    t0=time.time()
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.156,
            minNeighbors=4,
            minSize=(5,5),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    ) #4
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #print "Found %d faces" %(len(faces))
    N_face=0
    for n,(x,y,w,h) in zip(range(len(faces)),faces):
        face_p=image[y:y+h,x:x+w,:]
        cv2.imwrite("g:\\part.jpg",face_p)
        face_part=cv2.imread("g:\\part.jpg")
        face_part = cv2.cvtColor(face_part, cv2.COLOR_BGR2GRAY)
        noses = noseCascade.detectMultiScale(
        face_part,
        scaleFactor=1.24,
        minNeighbors=5,
        minSize=(3,3),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
        if len(noses):
            N_face+=1
            print "%d处人脸和鼻子都匹配!" %(n+1)
            blur=cv2.GaussianBlur(image[y:y+h,x:x+w,:],(85,85),0)
            image[y:y+h,x:x+w,:]=blur
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            print "%d处没有鼻子!" %(n+1)
        
    print "For picture:\"%s\",found %d faces in %.3fs" %(str(pictures[i]),N_face,(time.time()-t0))#5
    print "*******************************************************"
    cv2.imshow("Faces found", image)#7
    cv2.waitKey(0) #8
    cv2.destroyAllWindows()