import numpy as np

with open('input') as f:
    lines = f.readlines()

cavern_mx = np.chararray((600, 600))
cavern_mx[:]='.'


def filler(lines, mx):
    for i in lines:
        line = [[int(l) for l in s.split(',')] for s in i.strip().split(' -> ')]
        for k in range(len(line) - 1):
            x1, y1 = line[k]
            x2, y2 = line[k + 1]
            print(x1, y1, x2, y2)
            if x1 == x2:
                print('x!')
                if y1 < y2:
                    for y in range(y1, y2+1):
                        mx[y][x1] = '#'
                        print(x1, y)
                else:
                    for y in range(y2, y1+1):
                        mx[y][x1] = '#'
                        print(x1, y)
            if y1 == y2:
                print('y!')
                if x1 < x2:
                    for x in range(x1, x2+1):
                        mx[y1][x] = '#'
                        print(x, y1)
                else:
                    for x in range(x2, x1+1):
                        mx[y1][x] = '#'
                        print(x, y1)
    return mx


cavern_mx = filler(lines, cavern_mx)


print('\n\n\n', cavern_mx[498][4])

# for i in cavern_mx:
#     for k in i:
#         if cavern_mx[i][k]!=0:
#             print(cavern_mx[i][k], i, k)

print(cavern_mx[0:20, 490:510].decode())
