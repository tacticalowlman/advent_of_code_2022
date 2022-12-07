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


#def cd(tree, path):
#    if path=='cd /':
#        return tree
#    elif path='cd ..':


def open_path(tree, path):
    cur_place=tree
    for i in path:
        cur_place=cur_place[i]
    return cur_place




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
            cur_path.append(comm[3])
            if comm[3] in cur_place:
                cur_place=cur_place[comm[3]]
            else:
                cur_place[comm[3]] = {}
                cur_place=cur_place[comm[3]]
        ct+=1
    else:
        ct+=1


#while ct<len(lines):
#    if lines[ct][0]=='c':
#
#    if lines[ct]=='ls':
#        weight = 0
#        idir = []
#        ct+=1
#        while ct<len(lines) and lines[ct]!='ls' and lines[ct][0]!='c':
#            print('ds', ct)
#            if lines[ct][0].isdigit():
#                lines[ct] = int(lines[ct])
#            print(lines[ct])
#            if isinstance(lines[ct], int):
#                weight+=int(lines[ct])
#            else:
#                idir.append(lines[ct])
#            smdir=[idir, weight]
#            ct += 1
#            print(ct, len(lines))
#        tree.append(smdir)
#    else:
#        ct+=1
#    print('e', ct)

print(tree)











