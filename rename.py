import os

files = os.listdir('./output/')

for i,file in enumerate(files):
    os.rename(os.path.join( './output/',file),os.path.join('./output/','smpl{:03d}.jpg'.format(i)))