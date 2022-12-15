import re
import time

with open('input') as f:
    lines = f.readlines()

mx = []
mx_visual = []
line = []
# EXAMPLES PARAMETERS
# line_y = 10
# line_size = 20
# PART1 PARAMETERS
line_y = 4000000
line_size = 4000000
beacons_on_y_line = []

for i in lines:
    ls = [int(k) for k in re.findall(r'(-?[\d]+)', i)]
    mx.append(ls)
    # if ls[3] == line_y:
    #     beacons_on_y_line.append(ls[2])



for i in range(line_size):
    line = []
    for k in range(line_size):
        line.append('.')
    mx_visual.append(line)


for i in lines:
        _, _, x, y, _, _, _, _, x_clo, y_clo = i.split()
        x = int(x.split('=')[1][:-1])
        y = int(y.split('=')[1][:-1])
        x_clo = int(x_clo.split('=')[1][:-1])
        y_clo = int(y_clo.split('=')[1])

def print_mx(mx):
    s = ''
    for l in range(4):
        s += ''.join([str(i) for i in range(10)])
    print(s)
    for j, i in enumerate(mx):
        pnst = ''
        for k in i:
            pnst += str(k)
        print(pnst + ' ' + str(j))


# def print_mx(mx, y1, y2, x1, x2):
#     print('-' * (x2 - x1 + 1))
#     for i in mx[y1:y2 + 1]:
#         sstr = ''
#         for k in i[x1:x2 + 1]:
#             sstr += k
#         print(sstr)
#     print('-' * (x2 - x1 + 1))


def line_beacons(mx, j):
    t=time.time()
    line = mx_visual[j]
    for i in mx:
        xS, yS, xB, yB = i
        distance_x = abs(xB - xS)
        distance_y = abs(yB - yS)
        if yS < j:
            place_on_line = xS - (yS + distance_x + distance_y - j)
            size_on_line = 1 + (yS + distance_x + distance_y - j) * 2
        else:
            place_on_line = xS - (distance_x + distance_y - (yS - j))
            size_on_line = 1 + (distance_x + distance_y - (yS - j)) * 2
        #print(i, place_on_line, size_on_line)
        if size_on_line > 0:
            for k in range(place_on_line, place_on_line + size_on_line):
                if k < line_size:
                    line[k] = '#'
    print(f'processed time for one str {time.time()-t} current str now {j}')
    return mx_visual


for i in range(line_size):
    mx_visual = line_beacons(mx, i)

print_mx(mx_visual)

for i_ind, i in enumerate(mx_visual):
    for k_ind, k in enumerate(i):
        if k=='.':
            print(k_ind, i_ind)

# line = line_beacons(mx)
#
# ct = 0
# for i in line:
#     if i == '#':
#         ct += 1
#
# print(line, ct)
