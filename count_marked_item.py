import os
import re

dataset_folder="./data/dataset1/"
dataset_folder ='./data/test_data/0620_train'
list_txt_file = "./list_txt/train_valid_copy.txt"
names_file = "./cfg/test-kym.names"
dict = {}

with open(names_file,'r') as txt: 
    names = txt.readlines()
#for i,name in enumerate(names):
#    names[i] = name.replace("\n","")


def read_list_txt():
    global txt_lists
    print('list txt file path:'+str(list_txt_file))
    with open(list_txt_file,'r') as txt:
        img_lists =[ os.path.basename(p[:-1]) for p in  txt.readlines()]
        txt_lists =[ p.replace('.jpg','.txt') for p in img_lists]

def main():
    files = os.listdir(dataset_folder)
    pattern = re.compile("[^.]*.txt") 
    for file in files:
        m = pattern.match(file)
        if(not m):
            continue

        path = os.path.join(dataset_folder,file)
        abs_path = os.path.abspath(path)

        if 'txt_lists' in globals():#txt_lists 변수가 있는경우 리스트 안에 있는 라벨링만 확인
            global txt_lists
            base_name1 = os.path.basename(path)
            if txt_lists.count(base_name1)!=0:
                continue

        with open(abs_path,'r') as txt:
            lines = txt.readlines()
            for line in lines:
                if line[0]=="/":
                    continue
                split = line.split()
                class_num = int(split[0])
                if(dict.has_key(class_num)):
                    dict[class_num] +=1
                else:
                    dict[class_num] = 0

    total_count = 0
    for item in dict.iteritems():
        name = names[item[0]]
        print(name,item[1])
        total_count += item[1]
    print('total_count:'+str(total_count))
            
#read_list_txt()

main()