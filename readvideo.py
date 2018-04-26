import cv2
import os

cap = cv2.VideoCapture("./capture1.ogv")
output_folder="./output/"
i =0
while(cap.isOpened()):
    ret, img = cap.read()
    
    i+=1

    if(i%20==19):
        imS = cv2.resize(img,None,fx=0.5,fy=0.5)
        cv2.imshow("video",imS)
        key = cv2.waitKey(1)
        cv2.imwrite(os.path.join(output_folder,"sample{:3d}.jpg".format(i)),img)
        if(key==ord('q')):
            break


