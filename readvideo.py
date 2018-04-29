import cv2
import os

#video -> image

cap = cv2.VideoCapture("./data/0429_capture.ogv")
output_folder="./output/"
i =0
while(cap.isOpened()):
    ret, img = cap.read()
    
    i+=1

    if(i%100==99):
        imS = cv2.resize(img,None,fx=0.5,fy=0.5)
        cv2.imshow("video",imS)
        key = cv2.waitKey(1)
        cv2.imwrite(os.path.join(output_folder,"sample_180429_{:05d}.jpg".format(i)),img)
        if(key==ord('q')):
            break


