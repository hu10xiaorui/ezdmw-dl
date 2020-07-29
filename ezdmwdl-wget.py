import os
import platform
import re
if platform.system() == "Windows":
    cpt = os.popen('''chcp''').read()
    cp = re.sub('[^0-9]','', cpt)
    os.system("chcp 936")
vidl = input("输入第一话视频链接：")
hv = int(input("输入集数："))
vids = vidl.find("html5/")
vide = vidl.find(".html")
vid = vidl[vids+6:vide]
print("视频id：",vid)
for v in range(hv):
    print("==================================================================================================")
    print("下载视频网页中...")
    vp = os.popen('''curl --keepalive-time 10 "https://api.tzdjzu.com/index.php?nk='''+str(int(vid)+v)+'''&barrage_switch="''').read()
    print("视频网页下载成功")
    dvp=vp.find('''<source src="''')
    dvep=vp.find('''" onerror="load_fail[0]()">''')
    vurl=vp[dvp+13:dvep]
    print("视频地址：",vp[dvp+13:dvep])
    print("下载第"+str(v+1)+"集中...")
    os.system('''wget -o '''+str(v+1)+'''.mp4 "'''+vp[dvp+13:dvep]+'''"''')
    print("视频下载成功")
os.system("chcp "+cp)
