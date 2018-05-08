import os

target_folder = './data/0508_firetruck_train/'
files = os.listdir(target_folder)

def onlyImg():
    for i,file in enumerate(files):

        original = os.path.join(target_folder,file)
        fname,ext = os.path.splitext(original)
        new = os.path.join(target_folder,'smpl_180508_{:03d}'+ext).format(i)
        os.rename(original,new)

def withText():
    pairs = []
    jpgs = []
    txts = []
    for i,file in enumerate(files):
        original = os.path.join(target_folder,file)
        fname,ext = os.path.splitext(original)
        if(ext.lower()=='.jpg'):
            jpgs.append(file)
        elif(ext.lower()=='.txt'):
            txts.append(file)
        else:
            print("not supported ext: ",ext)

    for jpgfile in jpgs:
        for txtfile in txts:
            fname1,ext1 = os.path.splitext(jpgfile)
            fname2,ext2 = os.path.splitext(txtfile)
            if(fname1==fname2):
                pairs.append((jpgfile,txtfile))
                break
    
    for i, pair in enumerate(pairs):
        for file in pair:
            original = os.path.join(target_folder,file)
            fname,ext = os.path.splitext(original)
            new = os.path.join(target_folder,'smpl_firetruck_180508_{:03d}'+ext).format(i)
            os.rename(original,new)
withText()