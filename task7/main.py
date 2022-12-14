import re

with open('input') as f:
    lines = f.readlines()

def normalizer(lines):
    normalized=[]
    for i in lines:
        comm=i.strip()
        if comm[0]=='$':
            if i.strip()[2]=='c':
                normalized.append(comm[2:])
            else:
                normalized.append('ls')
        elif comm[0].isdigit():
            normalized.append(re.findall(r'\d+', comm)[0])
        else:
            normalized.append(comm)
    return normalized

def open_path(tree, path):
    cur_place=tree
    for i in path:
        cur_place=cur_place[i]
    return cur_place

def summ_count(tree):
    ct=0
    ct2=0
    for i in tree:
        if i=='dir_wgh':
            ct+=tree['dir_wgh']
        else:
            sp=summ_count(tree[i])
            ct+=sp[0]
            ct2+=sp[1]
    if ct <= 100000:
       ct2 += ct

    ans = [ct, ct2]
    return ans

def min(tree, cmin):
    ct=0
    for i in tree:
        if i=='dir_wgh':
            ct+=tree['dir_wgh']
        else:
            sp=min(tree[i], cmin)
            ct+=sp[0]
            cmin=sp[1]
    if ct > 4274331 and ct < cmin:
        cmin = ct
    ans = [ct, cmin]
    return ans

lines=normalizer(lines)
ct=0
tree={}
cur_path=[]
cur_place=[]
lines.append('END')

while lines[ct]!='END':
    comm=lines[ct]
    if comm[0]=='c':
        if comm=='cd /':
            cur_place=tree
            cur_path=[]
        elif comm=='cd ..':
            cur_path.pop()
            cur_place=open_path(tree, cur_path)
        else:
            cur_path.append(comm[3:])
            if comm[3:] in cur_place:
                cur_place=cur_place[comm[3:]]
            else:
                cur_place[comm[3:]] = {}
                cur_place=cur_place[comm[3:]]
        ct+=1
    elif lines[ct]=='ls':
        weight = 0
        ct+=1
        while lines[ct]!='END' and lines[ct]!='ls' and lines[ct][0]!='c':
            if lines[ct][0].isdigit():
                weight+=int(lines[ct])
            ct+=1
        cur_place['dir_wgh']=weight
    else:
        ct+=1




print(tree)
#print(summ_count(tree)[1], min(tree, 70000000)[1])#PART1 PART2 IN THAT ORDER











