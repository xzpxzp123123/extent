import os, sys
from subprocess import Popen

def findcov(path):
    res=[]
    for file in os.listdir(path):
        if os.path.isdir(path+"\\"+file):
            tmp=findcov(path+"\\"+file)
            res.extend(tmp)
        else:
            if "_cov" in file:
                res.append(path+"\\"+file)
    return res


targetdir="K:\\Nignx\\ConfDiagDetector\\"

for file in os.listdir(targetdir):
    print(file)
    covlist = findcov(targetdir+file)
    cov=""
    for i in covlist:
        print(i)
        cov = cov + i + " "
    cov = cov+"self-check_cov "
    res = Popen("genhtml -o ~/Desktop/" + cov + "--ignore-errors source", shell=True)
    res.communicate()






