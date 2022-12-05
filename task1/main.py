f = open("task1.txt", "r")
longst=f.read()
longst=longst.replace('\n\n', '\n@\n')
longst=longst.split()
cr=[]
ct1=0
ct2=0
ct3=0
ctcr=0
for i in longst:
    if i!='@':
        cr.append(i)
    else:
        print(cr, ctcr, ct1, ct2, ct3)
        for k in cr:
            ctcr+=int(k)
        if ctcr>ct3:
            if ct2!=0:
                ct1 = ct2
            if ct3!=0:
                ct2 = ct3
            ct3=ctcr
        elif ctcr>ct2:
            if ct2!=0:
                ct1=ct2
            ct2=ctcr
        elif ctcr>ct1:
            ct1=ctcr
        cr=[]
        ctcr=0


print(ct1+ct2+ct3)
