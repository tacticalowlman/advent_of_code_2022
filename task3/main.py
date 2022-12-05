import numpy as np

with open('input') as f:
    lines = f.readlines()
lines=[i.strip() for i in lines]
abc='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ct=0
cst=0

#PART1
for i in lines:
    fhf=i[0:int(len(i)/2)]
    shf=i[int(len(i)/2):]
    for n in fhf:
        for k in shf:
            if n==k and cst==0:
                ct+=abc.find(n)+1
                cst=1
    cst=0

print(ct)
ct=0

#PART2
linesr=np.array(lines)
linesr=linesr.reshape(100, 3)
for i in linesr:
    for k in i[0]:
        if i[1].find(k)!=-1 and i[2].find(k)!=-1 and cst==0:
            ct += abc.find(k) + 1
            cst=1
    cst=0

print(ct)