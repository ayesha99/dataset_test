import os
import re
output_folder="./output/"
def main():
    files = os.listdir('./output/')
    files.sort()
    text = open(os.path.join(output_folder,"train.txt"),'w')
    pattern = re.compile("[^.]*.jpg") 
    for file in files:
        m = pattern.match(file)
        if(not m):
            continue
        path = os.path.join(output_folder,file)
        abs_path = os.path.abspath(path)
        text.write(abs_path)
        text.write('\n')
    text.close()

def create_train_dir(img_dir):
    files = os.listdir(img_dir)
    files.sort()
    text = open(os.path.join(img_dir,"train.txt"),'w')
    pattern = re.compile("[^.]*.jpg") 
    for file in files:
        m = pattern.match(file)
        if(not m):
            continue
        path = os.path.join(img_dir,file)
        abs_path = os.path.abspath(path)
        text.write(abs_path)
        text.write('\n')
    text.close()

#create_train_dir('copy/')