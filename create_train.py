import os
import re
from shutil import copy2
dataset_folder="./data/dataset1/"
img_list_folder="./list_txt/"
def main():
    files = os.listdir(dataset_folder)
    files.sort()
    text = open(os.path.join(dataset_folder,"train.txt"),'w')
    pattern = re.compile("[^.]*.jpg") 
    for file in files:
        m = pattern.match(file)
        if(not m):
            continue
        path = os.path.join(dataset_folder,file)
        abs_path = os.path.abspath(path)
        text.write(abs_path)
        text.write('\n')
    text.close()

def create_train_dir(dataset_dir):
    files = os.listdir(dataset_dir)
    files.sort()
    text = open(os.path.join(dataset_dir,"train.txt"),'w')
    pattern = re.compile("[^.]*.jpg") 
    for file in files:
        m = pattern.match(file)
        if(not m):
            continue
        path = os.path.join(dataset_dir,file)
        abs_path = os.path.abspath(path)
        text.write(abs_path)
        text.write('\n')
    text.close()
import random
# train.txt -> train_set.txt train_valid.txt test.txt
def prepare_dataset_txt(dataset_dir):
    img_list = []
    with open(os.path.join(dataset_dir,"train.txt"),'r') as train:
        while True:
            line = train.readline()
            if not line:
                break                
            img_list.append(line)

    train_set = []
    valid_set = []
   
    test_set_ratio = 0.2
    random.shuffle(img_list)
    test_set_cnt = min(int(test_set_ratio*len(img_list)),20)
    test_set = img_list[0:test_set_cnt-1]
    train_set = img_list[test_set_cnt:]
    valid_set_cnt = min(len(train_set),20)
    valid_set = train_set[0:valid_set_cnt-1]
    test_set_path = os.path.join(dataset_dir,"test.txt")
    valid_set_path = os.path.join(dataset_dir,"train_valid.txt")
    train_set_path = os.path.join(dataset_dir,"train_set.txt")
    with open(test_set_path,'w') as txt:
        txt.writelines(test_set)
    with open(valid_set_path,'w') as txt:
        txt.writelines(valid_set)
    with open(train_set_path,'w') as txt:
        txt.writelines(train_set)
    
    train_txt = os.path.join(dataset_dir,"train.txt")
    copy2(test_set_path,img_list_folder)
    copy2(valid_set_path,img_list_folder)
    copy2(train_set_path,img_list_folder)
    copy2(train_txt,img_list_folder)

#create_train_dir(dataset_folder)
#prepare_dataset_txt(dataset_folder)

create_train_dir('./data/test_data/0620_train')