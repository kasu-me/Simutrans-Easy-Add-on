import PIL
import os
import sys
from PIL import Image, ImageChops
import time

with open(sys.argv[1],"r") as f:
    file=f.read()
abspth=os.path.dirname(sys.argv[1])+"\\"
commands=file.split("\n")
flow_count=1
for i in commands:
    print("\r処理中 : "+str(flow_count)+"/"+str(len(commands)),end="")
    #空白行は無視
    if i!="":
        com=i.split("=>")
        com0=com[0].split("[")[1].split("]")[0].split(",")
        for j in range(len(com0)):
            #単純合成
            if com[0].startswith("+"):
                im = Image.open(abspth+com0[j]+".png")
                #画像合成
                if j==0:
                    back_im = im.copy()
                else:
                    im=im.resize(back_im.size, resample=0)
                    back_im.alpha_composite(im)
            #乗算
            elif com[0].startswith("*"):
                im = Image.open(abspth+com0[j]+".png")
                white = Image.new('RGBA', im.size, (255, 255, 255, 255))
                white.alpha_composite(im)
                if j==0:
                    back_im = white.copy()
                else:
                    back_im = ImageChops.multiply(white,back_im)
        back_im.save(abspth+com[1]+".png")
    flow_count+=1
print("\n")
print("成功")
time.sleep(2)