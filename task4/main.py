import re

with open('input') as f:
    lines = f.readlines()
lines=[i.strip() for i in lines]
nums=[]
ct1=0
ct2=0

for i in lines:
    nums.append(re.findall(r'\d+', i))

#ct1 for PART1 ct2 for PART2
for i in nums:
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    d=int(i[3])
    if b-a >= d-c:
        if c>=a and d<=b:
            ct1+=1
    else:
        if a>=c and b<=d:
            ct1+=1
    if not((a<c and b<c) or (a>d and b>d)):
        ct2+=1

print(ct1, ct2)