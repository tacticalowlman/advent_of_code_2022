import re

with open('input') as f:
    lines = f.readlines()

mx = []
mx_visual = []
line = []
# EXAMPLES PARAMETERS
line_y = 10
line_size = 40
# PART1 PARAMETERS
# y_line = 2000000
# y_line_size = 10000000
beacons_on_y_line = []

for i in lines:
    ls = [int(k) for k in re.findall(r'\d+', i)]
    mx.append(ls)
    if ls[3] == line_y:
        beacons_on_y_line.append(ls[2])

# for i in range(line_size):
#     line = []
#     for k in range(line_size):
#         line.append('.')
#     mx_visual.append(line)

for i in range(line_size):
    line.append('.')


def line_beacons(mx):
    for i in mx:
        xS, yS, xB, yB = i
        distance_x = abs(xB - xS)
        distance_y = abs(yB - yS)
        if yS < line_y:
            place_on_line = xS - (yS + distance_x + distance_y - line_y)
            size_on_line = 1 + (yS + distance_x + distance_y - line_y) * 2
        else:
            place_on_line = xS - (distance_x + distance_y - (yS - line_y))
            size_on_line = 1 + (distance_x + distance_y - (yS - line_y)) * 2
        if size_on_line > 0:
            for k in range(place_on_line, place_on_line + size_on_line):
                if k not in beacons_on_y_line:
                    # print(k)
                    line[k] = '#'
                else:
                    line[k] = 'B'
    return line


line = line_beacons(mx)

ct = 0
for i in line:
    if i == '#':
        ct += 1

print(line, ct)
