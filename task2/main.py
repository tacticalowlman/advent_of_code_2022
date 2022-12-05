with open('task2') as f:
    lines = f.readlines()
pairs = [(i.strip()).split() for i in lines]

en={
    'A':1,
    'B':2,
    'C':3
}
mn={
    'X':1,
    'Y':2,
    'Z':3
}
ct=0

#TASK2 a)
#for i in range(len(pairs)-1):
#    ep = en[pairs[i][0]]
#    mp = mn[pairs[i][1]]
#    if ep == mp:
#        ct+=3+mp
#    elif (ep > mp or (ep==1 and mp==3)) and not(ep==3 and mp==1):
#        ct+=mp
#    else:
#        ct+=6+mp

for i in range(len(pairs)-1):
    ep = en[pairs[i][0]]
    mp = mn[pairs[i][1]]
    if mp==1:
        if ep==1:
            ct+=3
        else:
            ct+=ep-1
    elif mp==2:
        ct+=3+ep
    else:
        if ep==3:
            ct+=7
        else:
            ct+=6+ep+1

print(ct)
