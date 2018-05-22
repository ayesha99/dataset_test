import os
import re

dataset_folder="./data/dataset1/"
names_file = "./cfg/test-kym.names"
dict = {}

with open(names_file,'r') as txt: 
    names = txt.readlines()
#for i,name in enumerate(names):
#    names[i] = name.replace("\n","")

def main():
    files = os.listdir(dataset_folder)
    pattern = re.compile("[^.]*.txt") 
    for file in files:
        m = pattern.match(file)
        if(not m):
            continue

        path = os.path.join(dataset_folder,file)
        abs_path = os.path.abspath(path)

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

    
    for item in dict.iteritems():
        name = names[item[0]]
        print(name,item[1])
            


main()