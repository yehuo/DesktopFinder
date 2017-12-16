import os
import shutil


def picfilter():
    oripath = os.environ.get(
        'LOCALAPPDATA') + '\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
    destpath = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\Desktop\windows_pic'

    if not os.path.isdir(destpath):
        os.makedirs(destpath)

    for name in os.listdir(oripath):
        oripic = oripath + '\\' + name
        # print(os.path.isfile(oripic))
        destpic = destpath + '\\' + name  # +'.jpg'
        f = open(oripic, 'r')
        # print(os.path.getsize(oripic))
        # print(f.__sizeof__())
        if os.path.getsize(oripic) > 57600:  # 57600=320*180 which means 320KB
            shutil.copyfile(oripic, destpic)
        f.close()


def namechange(old, new):
    if new == '':
        return False
    abpath = "C:\\Users\\l\\Desktop\\windows_pic"
    if not os.path.isdir(abpath):
        print("no such direction")
        return False
    if old not in os.listdir(abpath):
        print("no such pic")
        return False
    os.rename(os.path.join(abpath, old), os.path.join(abpath, new))
    return True


def getlist():
    '''return a list of pictures in desktop dir'''
    abpath = "C:\\Users\\l\\Desktop\\windows_pic"
    if os.path.isdir(abpath):
        return os.listdir(abpath)
    print("set the dir first please")
    return None
