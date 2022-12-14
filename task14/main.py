with open('input') as f:
    lines = f.readlines()
cavern_mx = [[' ' for k in range(0, 600)] for i in range(0, 600)]


def filler(lines, mx):
    for i in lines:
        line = [[int(l) for l in s.split(',')] for s in i.strip().split(' -> ')]
        for k in range(len(line) - 1):
            x1, y1 = line[k]
            x2, y2 = line[k + 1]
            # #print(x1, y1, x2, y2)
            if x1 == x2:
                # #print('x!')
                if y1 < y2:
                    for y in range(y1, y2 + 1):
                        mx[y][x1] = '#'
                        # #print(x1, y)
                else:
                    for y in range(y2, y1 + 1):
                        mx[y][x1] = '#'
                        # #print(x1, y)
            if y1 == y2:
                # #print('y!')
                if x1 < x2:
                    for x in range(x1, x2 + 1):
                        mx[y1][x] = '#'
                        # #print(x, y1)
                else:
                    for x in range(x2, x1 + 1):
                        mx[y1][x] = '#'
                        # #print(x, y1)
    return mx


def lowest_point(mx):
    low = 0
    for i, ln in enumerate(mx):
        if '#' in ln and i > low:
            low = i
    return low


def print_mx(mx, y1, y2, x1, x2):
    #print('-' * (x2 - x1 + 1))
    for i in mx[y1:y2 + 1]:
        sstr = ''
        for k in i[x1:x2 + 1]:
            sstr += k
        #print(sstr)
    #print('-' * (x2 - x1 + 1))


def corn_activity(cavern_mx, lowest_point):
    x, y = 500, 0
    ct=0
    while y != lowest_point:
        #print(x, y)
        x, y = 500, 0
        y_p, x_p = -1, -1
        while y_p != y and y < lowest_point:
            below = [[y + 1, x - 1], [y + 1, x], [y + 1, x + 1]]
            #print(x, y, below)
            #print(cavern_mx[below[1][0]][below[1][1]])
            if cavern_mx[below[1][0]][below[1][1]] == ' ':
                #print('under')
                y_p, x_p = y, x
                x, y = x, y + 1
                cavern_mx[y_p][x_p] = ' '
                cavern_mx[y][x] = 'O'
            elif cavern_mx[below[0][0]][below[0][1]] == ' ':
                y_p, x_p = y, x
                x, y = x - 1, y + 1
                cavern_mx[y_p][x_p] = ' '
                cavern_mx[y][x] = 'O'
            elif cavern_mx[below[2][0]][below[2][1]] == ' ':
                #print('r')
                y_p, x_p = y, x
                x, y = x + 1, y + 1
                cavern_mx[y_p][x_p] = ' '
                cavern_mx[y][x] = 'O'
            else:
                y_p, x_p = y, x
                #print('all', y_p, y)
                cavern_mx[y_p][x_p] = ' '
                cavern_mx[y][x] = 'O'
            #print_mx(cavern_mx, 0, 10, 490, 510)
        ct+=1
    answer=[cavern_mx, ct-1]
    return answer


cavern_mx = filler(lines, cavern_mx)
cavern_mx, ct = corn_activity(cavern_mx, lowest_point(cavern_mx))
print_mx(cavern_mx, 0, 200, 400, 600)
print(ct)
