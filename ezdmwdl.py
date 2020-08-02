import os
import platform
import re
import webbrowser
import wget
if platform.system() == "Windows":
    cpt = os.popen('''chcp''').read()
    cp = re.sub('[^0-9]','', cpt)
    os.system("chcp 936")
vidl = input("输入番剧链接：")
hv = int(input("输入集数："))
browser = input("使用浏览器下载？(建议使用浏览器)（y/n）：").lower()
videourll=[]
vp = os.popen('''curl --keepalive-time 10  --insecure  --retry-delay 3 --retry-max-time 0  --retry 100 "'''+vidl+'''"''').read().replace("\n","")
urllsp=vp.find("国内高速节点")
urllep=vp.find('''<span class="1">1</span>''')
urll=vp[urllsp+12:urllep]
rurll=urll
for x in range(hv):
    a=rurll.find('''<a href="''')
    b=rurll.find('''" >    	        <span class="''')
    c=rurll.find('''</a>''')
    videourll.append(rurll[a+len('''<a href="'''):b].replace('''"''',"").replace(">","").replace("\t","").replace(" ","").replace("/Home/Index/html5/","").replace(".html",""))
    rurll=rurll[c+4:]

i=0
for video in videourll:
    print("==================================================================================================")
    print("下载视频网页中...")
    vp = os.popen('''curl --keepalive-time 10 --insecure  --retry-delay 3 --retry-max-time 0  --retry 100 "https://api.tzdjzu.com/index.php?nk='''+video+'''&barrage_switch="''').read()
    print("视频网页下载成功")
    dvp=vp.find('''<source src="''')
    dvep=vp.find('''" onerror="load_fail[0]()">''')
    vurl=vp[dvp+13:dvep]
    print("视频地址：",vp[dvp+13:dvep])
    print("下载第"+str(hv-i)+"集中...")

    if browser == "y":
        webbrowser.open(vp[dvp+13:dvep])
    else:
        wget.download(vp[dvp+13:dvep], str(hv-i)+".mp4")
        #os.system('''curl --keepalive-time 10  --retry-delay 3 --retry-max-time 0 --retry 100 -o '''+str(hv-i)+'''.mp4 "'''+vp[dvp+13:dvep]+'''"''')
    print("视频下载成功")
    i=i+1
if platform.system() == "Windows":
    os.system("chcp "+cp)
