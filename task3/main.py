import numpy as np

with open('input') as f:
    lines = f.readlines()
lines=[i.strip() for i in lines]
abc='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ct=0
cst=0

for i in lines:
    fhf=i[0:int(len(i)/2)]
    shf=i[int(len(i)/2):]
    #print(i, fhf, shf)
    for n in fhf:
        for k in shf:
            if n==k and cst==0:
                ct+=abc.find(n)+1
                #print(n, abc.find(n)+1, ct)
                cst=1
    cst=0

print(ct)

linesr=np.array(lines)
linesr=linesr.reshape(100, 3)
for i in linesr:
    for k in i[0]:
        if i[1].find(k)!=-1 and i[2].find(k)!=-1 and cst==0:
            ct += abc.find(k) + 1
            #print(i[0], i[1], i[2], k, abc.find(k) + 1, ct)
            cst=1
    cst=0

print(ct)