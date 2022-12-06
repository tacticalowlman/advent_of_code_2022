f = open("input", "r")
longst=f.read()
mln=4#LENGTH OF THE MARKER ITSELF PART1 - 4, PART2 - 14

def check(s, st):
    ct=0
    for i in st:
        if s==i and ct==1:
            return False
        elif s==i:
            ct=1
    return True

def find(longst):
    ctsp=0
    for i in range(len(longst) - mln):

        ctsp+=1
        print(i, ctsp)
        ct = 0
        sst = longst[i:i + mln]
        for k in sst:
            if check(k, sst):
                ct+=1
                print(ct)
        if ct==14:
            return ctsp+mln-1

print(find(longst))



