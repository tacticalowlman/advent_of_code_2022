with open('input') as f:
    lines = f.readlines()
trs_hdn_mx=[]
trs_mx=[]
for i in lines:
    trs_ln=[]
    for k in i:
        if k.isdigit():
            trs_ln.append(int(k))
    trs_mx.append(trs_ln)

def check_h(mx):
    trs_hdn_mx=[]
    ct0=0
    for k in mx:
        ct = 0
        trs_hdn_ln = []
        max_h = 0
        for i in k:
            if ct>0 and i<=max_h:
                trs_hdn_ln.append('h')
            else:
                trs_hdn_ln.append('v')
            if i>max_h:
                max_h=i
            ct+=1
        trs_hdn_mx.append(trs_hdn_ln)
        ct0+=1
    return trs_hdn_mx

def rotate(trs_mx):
    rows = len(trs_mx)
    cols = len(trs_mx)
    new_mx = [[""] * rows for _ in range(cols)]
    for x in range(rows):
        for y in range(cols):
            new_mx[y][rows - x - 1] = trs_mx[x][y]
    return new_mx

def inverse(trs_mx):
    new_mx=[]
    for i in range(len(trs_mx)-1, -1, -1):
        new_ln=[]
        for k in range(len(trs_mx)-1, -1, -1):
            new_ln.append(trs_mx[i][k])
        new_mx.append(new_ln)
    return new_mx

def inverse_fx(trs_mx):
    new_mx=[]
    for i in range(len(trs_mx)):
        new_ln=[]
        for k in range(len(trs_mx)-1, -1, -1):
            #print(trs_mx[i][k])
            new_ln.append(trs_mx[i][k])
        new_mx.append(new_ln)
    return new_mx

def rotate_back(trs_mx):
    new_mx=trs_mx
    for i in range(3):
        new_mx=rotate(new_mx)
    return new_mx

def print_mx(trs_mx):
    for i in trs_mx:
        pnst=''
        for k in i:
            pnst+=' '+str(k)+' '
        print(pnst)

# def print_mx2(trs_mx):
#     pnst = ''
#     [[pnst+=str[k] for k in i] for i in trs_mx]




# def ct_sc(trs_mx):
#     new_mx=[]
#     #print(trs_mx[0])
#     for i in range(len(trs_mx)):
#         new_ln=[]
#         for k in range(len(trs_mx)):
#             ct1=1
#             ct2=1
#             cte=0
#             thl=0
#             thr=0
#             ctm=0
#             el=trs_mx[i][k]
#             ls=trs_mx[i][:k][::-1]
#             rs=trs_mx[i][k:]
#             rs.pop(0)
#             # if i<5 and k<5:
#             #     print(el, ls,  rs)
#             if len(ls)>0:
#                 thl = ls[cte]
#                 while el<thl and len(ls)>cte:
#                     el = ls[cte]
#                     ct1+=1
#                     cte+=1
#                     if ct1>10:
#                         print('AAAAAAAAAA', el, thl)
#             cte=0
#             if len(rs)>0:
#                 thr = rs[cte]
#                 while el<thr and len(rs)>cte:
#                     el = rs[cte]
#                     ct2+=1
#                     cte+=1
#             if ct1*ct2>ctm:
#                 ctm=ct1*ct2
#                 print(ctm)
#                 #print(ct1*ct2, el, thl, thr, ls, rs, '\n\n\n')
#             new_ln.append(ct1*ct2)
#         new_mx.append(new_ln)
#
#     return new_mx


# def ct_st(trs_mx):
#     new_mx=[]
#     for i in range(len(trs_mx)):
#         new_ln=[]
#         for k in range(len(trs_mx)):
#             el=trs_mx[i][k]
#             ls=trs_mx[i][:k][::-1]
#             rs=trs_mx[i][k:]
#             ct1=0
#             ct2=0
#             ctc=0
#             rs.pop(0)
#             #print(el, ls, rs)
#             if ls!=[]:
#                 while len(ls)>ctc and el>ls[ctc]:
#                     ct1+=1
#                     ctc+=1
#                 if el==ls[ctc]:
#                     ct1+=1
#             else:
#                 ct1=0
#             ctc=0
#             if rs!=[]:
#                 while len(rs)>ctc and el>rs[ctc]:
#                     ct2+=1
#                     ctc+=1
#                 if el==rs[ctc]:
#                     ct2+=1
#             else:
#                 ct2=0
#             #print(ct1, ct2)
#             new_ln.append(ct1 * ct2)
#         new_mx.append(new_ln)
#     return new_mx

def ct_st(trs_mx):
    new_mx=[]
    for i in range(len(trs_mx)):
        new_ln=[]
        for k in range(len(trs_mx)):
            el=trs_mx[i][k]
            ls=trs_mx[i][:k][::-1]
            rs=trs_mx[i][k:]
            rs.pop(0)
            ct1=0
            ct2=0
            stp=True
            for z in ls:
                if stp:
                    ct1 += 1
                    if el <= z:
                        stp = False
            stp=True
            for z in rs:
                if stp:
                    ct2 += 1
                    if el<=z:
                        stp = False
            new_ln.append(ct1 * ct2)
        new_mx.append(new_ln)
    return new_mx


#PART1
mx1=check_h(trs_mx)
mx2=inverse_fx(check_h(inverse_fx(trs_mx)))
mx3=rotate_back(check_h(rotate(trs_mx)))
mx4=rotate(check_h(rotate_back(trs_mx)))
ct=0
for i in range(len(mx1)):
    for k in range(len(mx1)):
        if mx1[i][k]=='v' or mx2[i][k]=='v' or mx3[i][k]=='v' or mx4[i][k]=='v':
            ct+=1

print(ct)
#PART2
# mx1=ct_st(trs_mx)
# mx2=rotate(ct_st(rotate_back(trs_mx)))
# fmx=[]
# maxi=0
# print_mx(mx1)
# print('\n\n')
# print_mx(mx2)
# for i in range(len(mx1)):
#     fln=[]
#     for k in range(len(mx1)):
#         fln.append(mx1[i][k]*mx2[i][k])
#         if mx1[i][k]*mx2[i][k]>maxi:
#             maxi=mx1[i][k]*mx2[i][k]
#     fmx.append(fln)
# print_mx(fmx)
# print(maxi)
#print(*mx1, sep='\n')

print('job one')


print('job two')