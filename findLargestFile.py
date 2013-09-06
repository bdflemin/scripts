import os, re
def filePop(top):
    sizeList = []
    #exclude = "^/proc.*|^/sys.*|^/boot.*|^/tmp.*|^/mnt.*"
    exclude = "^/proc.*|^/sys.*|^/boot.*|/tmp.*|/home.*|/var.*|/data.*"
    # Skip any files that are located in /proc, /sys or /boot
    for root,dirs,files in os.walk(top):
        if re.findall(exclude,root):
            continue
        for f in files:
            fullpath = os.path.join(root,f)
            if (os.path.isfile(fullpath) or os.path.isdir(fullpath)) and not os.path.islink(fullpath):
                sizeList.append((os.path.getsize(fullpath),fullpath))
    return sizeList

def fileSort(fileList,top=15):
    sList = sorted(fileList, key=lambda a: a[0], reverse=True)
    for i in xrange(0,15):
        size = ((sList[i][0] / 1024) / 1024)
        directory = sList[i][1]
        print '%s MB --> %s' % (size,directory)

fileSort(filePop("/"))