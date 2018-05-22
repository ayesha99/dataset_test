import os




def onlyImg():
    target_folder = './data/0509_deer_train/'
    files = os.listdir(target_folder)
    for i,file in enumerate(files):

        original = os.path.join(target_folder,file)
        fname,ext = os.path.splitext(original)
        new = os.path.join(target_folder,'smpl_180508_{:03d}'+ext).format(i)
        os.rename(original,new)

def withText(target_folder,infix):
    pairs = []
    jpgs = []
    txts = []
    files = os.listdir(target_folder)
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
            new = os.path.join(target_folder,'smpl_{}_{:03d}'+ext).format(infix,i)
            os.rename(original,new)
            print("rename:"+new)


#withText('./data/0513_cat2_train/',"180513_cat2")