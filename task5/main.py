import re

with open('input') as f:
    lines = f.readlines()

ABC=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'   
bricks=[]
norm_bricks=[]
commands=[]
bre=0

for i in lines:
    if i=='\n':
        bre=1
    else:
        if bre==0:
            bricks.append(i)
        else:
            commands.append(re.findall(r'\d+', i))
bricks.pop()

for i in range(9):
    norm_stack=[]
    for k in reversed(bricks):
        if ABC.find(k[1+i*4])!=0:
            norm_stack.append(ABC.find(k[1+i*4]))
    norm_bricks.append(norm_stack)

for i in commands:
    bl_num=int(i[0])
    tk_st=int(i[1])-1
    br_st=int(i[2])-1
    norm_bricks[br_st].extend(reversed(norm_bricks[tk_st][-bl_num:]))#FOR PART2 JUST REMOVE REVERSED FUNCTION
    norm_bricks[tk_st]=norm_bricks[tk_st][:-bl_num]

for i in range(9):
    print(ABC[norm_bricks[i][len(norm_bricks[i])-1]], end='')




