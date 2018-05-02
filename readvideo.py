import cv2
import os

#video -> image
vid_file_name="./data/0502_video2.mp4"
#
cap = cv2.VideoCapture(vid_file_name)
output_folder="./data/0502_video2_original/"
i =0


if( not os.path.exists(output_folder)):
    os.mkdir(output_folder)

while(cap.isOpened()):
    ret, img = cap.read()
    
    i+=1

    if(i%100==99):
        imS = cv2.resize(img,None,fx=0.5,fy=0.5)
        cv2.imshow("video",imS)
        key = cv2.waitKey(1)
        cv2.imwrite(os.path.join(output_folder,"sample_180502video2_{:05d}.jpg".format(i)),img)
        if(key==ord('q')):
            break


