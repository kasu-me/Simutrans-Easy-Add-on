import os
import sys
import re
import time

def getWords(txt):
    return txt.split("[")[1].split("]")[0].split(",")

with open(sys.argv[1],"r") as f:
    file=f.read()
abspth=os.path.dirname(sys.argv[1])+"\\"
commands=file.split("\n")
filenames=commands[0].split("=>")
with open(abspth+filenames[0],"r") as f:
    dat=f.read()

search=getWords(commands[1])
replace=[]

result=[dat]

for i in commands[2:]:
    replace.append(getWords(i))


for i in replace:
    result.append(result[0])
    for j in range(len(search)):
        if i[j]=="$":
            i[j]=search[j]
        elif i[j].startswith("$"):
            i[j]=i[int(i[j].split("$")[1])]
        result[-1]=re.sub(search[j],i[j],result[-1])

with open(abspth+filenames[1],"w") as f:
    f.write("\n".join(result))

print("成功")
time.sleep(2)
