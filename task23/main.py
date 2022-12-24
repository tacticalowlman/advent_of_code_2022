import copy

with open('input') as f:
    lines = f.readlines()

previous_pos_mx = []
current_pos_mx = []
extension = 100
directions = 'nswe'
ct = 0

for i in range(extension):
    current_pos_mx.append(['.' for k in range(len(lines[0].strip()) + extension * 2)])
for i in lines:
    ln = []
    for k in range(extension):
        ln.append('.')
    for k in i.strip():
        ln.append(k)
    for k in range(extension):
        ln.append('.')
    current_pos_mx.append(ln)
for i in range(extension):
    current_pos_mx.append(['.' for k in range(len(lines[0].strip()) + extension * 2)])


def print_mx(mx):
    for j, i in enumerate(mx):
        pnst = ''
        for k in i:
            pnst += str(k)
        print(pnst)
    print('')


def point_nbrs(current_pos_mx, x, y):
    nbrs = [current_pos_mx[y - 1][x - 1],
            current_pos_mx[y - 1][x],
            current_pos_mx[y - 1][x + 1],
            current_pos_mx[y][x - 1],
            current_pos_mx[y][x + 1],
            current_pos_mx[y + 1][x - 1],
            current_pos_mx[y + 1][x],
            current_pos_mx[y + 1][x + 1]]
    return nbrs


def proposal_movement(current_pos_mx, directions):
    proposal_pos_mx = []
    for y in current_pos_mx:
        proposal_pos_ln = []
        for x in y:
            proposal_pos_ln.append([])
        proposal_pos_mx.append(proposal_pos_ln)
    for y, y_line in enumerate(current_pos_mx):
        for x, x_char in enumerate(y_line):
            if x_char == '#':
                nbrs = point_nbrs(current_pos_mx, x, y)
                stable = 0
                for b in nbrs:
                    if b == '.':
                        stable += 1
                if stable != 8:
                    for d in directions:
                        if d == 'n' and nbrs[0] == '.' and nbrs[1] == '.' and nbrs[2] == '.':
                            proposal_pos_mx[y - 1][x].append([x, y])
                            break
                        elif d == 's' and nbrs[5] == '.' and nbrs[6] == '.' and nbrs[7] == '.':
                            proposal_pos_mx[y + 1][x].append([x, y])
                            break
                        elif d == 'w' and nbrs[0] == '.' and nbrs[3] == '.' and nbrs[5] == '.':
                            proposal_pos_mx[y][x - 1].append([x, y])
                            break
                        elif d == 'e' and nbrs[2] == '.' and nbrs[4] == '.' and nbrs[7] == '.':
                            proposal_pos_mx[y][x + 1].append([x, y])
                            break

    directions = directions[1:] + directions[0]
    return [proposal_pos_mx, directions]


def movement(current_pos_mx, proposal_pos_mx):
    print_mx(current_pos_mx)
    for y, y_line in enumerate(proposal_pos_mx):
        for x, x_char in enumerate(y_line):
            if len(proposal_pos_mx[y][x]) == 1:
                x_p, y_p = proposal_pos_mx[y][x][0][0], proposal_pos_mx[y][x][0][1]
                current_pos_mx[y][x] = current_pos_mx[y_p][x_p]
                current_pos_mx[y_p][x_p] = '.'
    return current_pos_mx


def cut_mx(current_position_mx):
    x_min, y_min, x_max, y_max = 1000, 1000, 0, 0
    for y, y_line in enumerate(current_position_mx):
        for x, x_char in enumerate(y_line):
            cur_char = current_position_mx[y][x]
            if cur_char == '#' and x < x_min:
                x_min = x
            if cur_char == '#' and x > x_max:
                x_max = x
            if cur_char == '#' and y < y_min:
                y_min = y
            if cur_char == '#' and y > y_max:
                y_max = y
    cutted_mx = []
    for y, y_line in enumerate(current_position_mx):
        cutted_ln = []
        for x, x_char in enumerate(y_line):
            if x_min <= x <= x_max and y_min <= y <= y_max:
                cutted_ln.append(x_char)
        cutted_mx.append(cutted_ln)
    return cutted_mx


def count_mx(mx):
    ct = 0
    for y, y_line in enumerate(mx):
        for x, x_char in enumerate(y_line):
            if x_char == '.':
                ct += 1
    return ct


# PART1
# for i in range(10):
#     proposal_pos_mx, directions = proposal_movement(current_pos_mx, directions)
#     current_pos_mx = movement(current_pos_mx, proposal_pos_mx)
# cutted_mx = cut_mx(current_pos_mx)
# print(count_mx(cutted_mx))

# PART2
while previous_pos_mx != current_pos_mx:
    ct += 1
    proposal_pos_mx, directions = proposal_movement(current_pos_mx, directions)
    previous_pos_mx = copy.deepcopy(current_pos_mx)
    current_pos_mx = movement(current_pos_mx, proposal_pos_mx)

print(ct)
