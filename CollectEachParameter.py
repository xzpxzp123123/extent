import re
import os

def ReadHtml(HtmlPath):
    with open(HtmlPath,'r') as f:
        HtmlContent = f.read()
    pattern=r'<table cellpadding=1 border=0 width="100%">(.*?)</table>'
    table = re.findall(pattern, HtmlContent, re.S | re.M)
    datapattern = r'<td class="headerCovTableEntry">(.*?)</td>'
    ratiopattern = r'<td class="headerCovTableEntryLo">(.*?)</td>'
    data = re.findall(datapattern, table[0], re.S | re.M)
    ratio = re.findall(ratiopattern,table[0],re.S | re.M)
    Lines_Hit =data[0]
    Lines_Total = data[1]
    Functions_Hit = data[2]
    Functions_Total = data[3]
    Lines_Coverage =ratio[0]
    Functions_Coverage =ratio[1]
    return Lines_Hit

targetdir = "K:/leo/data/httpd/each/ConfDiagDetector"
num=0
sum = 0
for i in os.listdir(targetdir):
    print(i)
    for file in os.listdir(targetdir+'/'+i):
        if "index.html"==file:
            num = ReadHtml(targetdir+'/'+i+'/'+file)
            sum = sum+(int(num)-8648)
            tmp = str(int(num)-8648)
            with open(targetdir+"/httpd_ConfDiagDetector_cov.txt",'a') as fp:
                fp.write(i+" "+tmp+"\n")
with open(targetdir + "/httpd_ConfDiagDetector_cov.txt", 'a') as fp:
    fp.write("SUM "+str(sum))


