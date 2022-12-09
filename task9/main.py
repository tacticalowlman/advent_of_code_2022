with open('input') as f:
    lines = f.readlines()

def current_tails_position(x_h, y_h, x_t, y_t, x_h_pr, y_h_pr):
    if abs(x_h-x_t)>1:
        x_t=x_h_pr
        if abs(y_h-y_t)==1:
            y_t=y_h

    if abs(y_h-y_t)>1:
        y_t=y_h_pr
        if abs(x_h-x_t)==1:
            x_t=x_h
    return [x_t, y_t]

def current_tails_position_for_pt2(x_h, y_h, x_t, y_t):
    ct=0
    if x_h-x_t>1:
        print('1')
        x_t=x_h-1
        ct+=1
        if abs(y_h-y_t)==1 and ct<2:
            print('12')
            y_t=y_h
    if x_h-x_t<-1:
        print('2')
        x_t=x_h+1
        ct += 1
        if abs(y_h-y_t)==1 and ct<2:
            print('22')
            y_t=y_h
    if y_h-y_t>1:
        print('3')
        y_t=y_h-1
        ct += 1
        if abs(x_h-x_t)==1 and ct<2:
            print('32')
            x_t=x_h
    if y_h-y_t<-1:
        print('4')
        y_t=y_h+1
        ct += 1
        if abs(x_h-x_t)==1 and ct<2:
            print('42')
            x_t=x_h
    return [x_t, y_t]

def intermediate_position(xy_intermediate):
    for i in range(1, 10):
        print(i)
        xy_intermediate[i]=current_tails_position_for_pt2(xy_intermediate[i-1][0], xy_intermediate[i-1][1], xy_intermediate[i][0], xy_intermediate[i][1])
    return xy_intermediate

def print_rope(mi_x, ma_x, mi_y, ma_y, rope):
    abs_max_y = abs(mi_y)+abs(ma_y)
    grid = [[[x, ma_y-y-1 ,'.'] for x in range(mi_x,ma_x)] for y in range(ma_y)]
    for y in range(mi_y,0):
        grid.append([[x, y, '.'] for x in range(mi_x, ma_x)])
    print('---')
    for part_ind, part in enumerate(rope):
        for row in grid:
            for dot in row:
                if (dot[0], dot[1]) == tuple(part):
                    if dot[2] in ['.', 's']:
                        if part_ind == 0:
                            dot[2] = 'H'
                        else:
                            dot[2] = part_ind
                elif (dot[0], dot[1]) == (0, 0):
                    dot[2] = 's'
    print(*[''.join(map(lambda x: str(x[2]), i)) for i in grid], sep='\n')
    print('---')

x_h, y_h=0, 0
x_t, y_t=0, 0
x_h_pr, y_h_pr=0, 0
xy_visited=[]
xy_intermediate=[]
xy_intermediate.append([x_h, y_h])
for i in range(9):
    xy_intermediate.append([0, 0])

#PART1
for i in lines:
    direction=i.split()[0]
    steps=int(i.split()[1])
    if direction=='U':
        for k in range(steps):
            y_h+=1
            x_t, y_t=current_tails_position_for_pt2(x_h, y_h, x_t, y_t)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
    elif direction=='D':
        for k in range(steps):
            y_h-=1
            x_t, y_t=current_tails_position_for_pt2(x_h, y_h, x_t, y_t)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
    elif direction == 'R':
        for k in range(steps):
            x_h+=1
            x_t, y_t=current_tails_position_for_pt2(x_h, y_h, x_t, y_t)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
    elif direction == 'L':
        for k in range(steps):
            x_h-=1
            x_t, y_t=current_tails_position_for_pt2(x_h, y_h, x_t, y_t)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])

print(len(xy_visited))

#PART2
# for i in lines:
#     direction=i.split()[0]
#     steps=int(i.split()[1])
#     if direction=='U':
#         for k in range(steps):
#             y_h+=1
#             xy_intermediate[0]=x_h, y_h
#             xy_intermediate=intermediate_position(xy_intermediate)
#             x_t,y_t=xy_intermediate[9]
#             if [x_t, y_t] not in xy_visited:
#                 xy_visited.append([x_t, y_t])
#     elif direction=='D':
#         for k in range(steps):
#             y_h-=1
#             xy_intermediate[0] = x_h, y_h
#             xy_intermediate = intermediate_position(xy_intermediate)
#             x_t, y_t = xy_intermediate[9]
#             if [x_t, y_t] not in xy_visited:
#                 xy_visited.append([x_t, y_t])
#     elif direction == 'R':
#         for k in range(steps):
#             x_h+=1
#             xy_intermediate[0] = x_h, y_h
#             xy_intermediate = intermediate_position(xy_intermediate)
#             x_t, y_t = xy_intermediate[9]
#             if [x_t, y_t] not in xy_visited:
#                 xy_visited.append([x_t, y_t])
#     elif direction == 'L':
#         for k in range(steps):
#             x_h-=1
#             xy_intermediate[0] = x_h, y_h
#             xy_intermediate = intermediate_position(xy_intermediate)
#             x_t, y_t = xy_intermediate[9]
#             if [x_t, y_t] not in xy_visited:
#                 xy_visited.append([x_t, y_t])
#
# print(len(xy_visited))
