with open('input') as f:
    lines = f.readlines()
cavern_mx = [[' ' for k in range(0, 700)] for i in range(0, 700)]


def filler(lines, mx):
    for i in lines:
        line = [[int(l) for l in s.split(',')] for s in i.strip().split(' -> ')]
        for k in range(len(line) - 1):
            x1, y1 = line[k]
            x2, y2 = line[k + 1]
            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2 + 1):
                        mx[y][x1] = '#'
                else:
                    for y in range(y2, y1 + 1):
                        mx[y][x1] = '#'
            if y1 == y2:
                if x1 < x2:
                    for x in range(x1, x2 + 1):
                        mx[y1][x] = '#'
                else:
                    for x in range(x2, x1 + 1):
                        mx[y1][x] = '#'
    return mx


def lowest_point(mx):
    low = 0
    for i, ln in enumerate(mx):
        if '#' in ln and i > low:
            low = i
    return low


def print_mx(mx, y1, y2, x1, x2):
    print('-' * (x2 - x1 + 1))
    for i in mx[y1:y2 + 1]:
        sstr = ''
        for k in i[x1:x2 + 1]:
            sstr += k
        print(sstr)
    print('-' * (x2 - x1 + 1))


def part2_adapter(cavern_mx, lowest_point):
    for i in range(len(cavern_mx[lowest_point+2])):
        cavern_mx[lowest_point+2][i]='#'
    return cavern_mx


def corn_activity(cavern_mx, lowest_point):
    x, y = 500, 0
    ct=0
    while y != lowest_point and cavern_mx[0][500]!='O':
        x, y = 500, 0
        y_p, x_p = -1, -1
        while y_p != y and y < lowest_point:
            below = [[y + 1, x - 1], [y + 1, x], [y + 1, x + 1]]
            if cavern_mx[below[1][0]][below[1][1]] == ' ':
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
                y_p, x_p = y, x
                x, y = x + 1, y + 1
                cavern_mx[y_p][x_p] = ' '
                cavern_mx[y][x] = 'O'
            else:
                y_p, x_p = y, x
                cavern_mx[y_p][x_p] = ' '
                cavern_mx[y][x] = 'O'
        #print_mx(cavern_mx, 0, 200, 300, 700)
        ct+=1
    answer=[cavern_mx, ct]
    return answer


cavern_mx = filler(lines, cavern_mx)


#PART1
cavern_mx, ct = corn_activity(cavern_mx, lowest_point(cavern_mx))
print_mx(cavern_mx, 0, 20, 300, 700)
print(ct-1)

# PART2
# cavern_mx=part2_adapter(cavern_mx, lowest_point(cavern_mx))
# cavern_mx, ct = corn_activity(cavern_mx, lowest_point(cavern_mx))
# print_mx(cavern_mx, 0, 200, 300, 700)
# print(ct)
