f = open('input', 'r')

input_st = f.read()

dl = 0
clock = 0
stable_rocks = 0
empty_str = '.......'
tetris_mx = [empty_str for i in range(3)]


def print_mx(mx):
    for j, i in enumerate(mx):
        pnst = ''
        for k in i:
            pnst += str(k)
        print(pnst)
    print('')


def command(clock):
    return input_st[clock % len(input_st)]


def horizontal_stick(tetris_mx, clock):
    tetris_mx.reverse()
    tetris_mx.append('..@@@@.')
    tetris_mx.reverse()
    figure_x = 2
    figure_y = 0
    print_mx(tetris_mx)
    print(command(clock))
    while figure_y + 1 < len(tetris_mx) and tetris_mx[figure_y + 1][figure_x:figure_x + 4] == '....':
        if command(clock) == '<' and figure_x != 0 and tetris_mx[figure_y][figure_x - 1] == '.':
            figure_x -= 1
        elif command(clock) == '>' and figure_x != 3 and tetris_mx[figure_y][figure_x + 4] == '.':
            figure_x += 1
        figure_y += 1
        clock += 1
        tetris_mx[figure_y - 1] = tetris_mx[figure_y - 1].replace('@', '.')
        tetris_mx[figure_y] = tetris_mx[figure_y][:figure_x] + '@@@@' + tetris_mx[figure_y][figure_x + 4:]
        print_mx(tetris_mx)
        print(command(clock))
    tetris_mx[figure_y] = tetris_mx[figure_y].replace('@', '#')
    return [tetris_mx, clock]


def vertical_stick(tetris_mx, clock):
    tetris_mx.reverse()
    for i in range(4):
        tetris_mx.append('..@....')
    tetris_mx.reverse()
    space_free_l, space_free_r = True, True
    figure_x = 2
    figure_y = 0
    print_mx(tetris_mx)
    print(command(clock))
    while figure_y + 4 < len(tetris_mx) and tetris_mx[figure_y + 4][figure_x] == '.':
        if command(clock) == '<' and figure_x != 0:
            for i in range(4):
                space_free_l = True
                if not (tetris_mx[figure_y + i][figure_x - 1] == '.'):
                    space_free_l = False
            if space_free_l:
                figure_x -= 1
        elif command(clock) == '>' and figure_x != 6:
            for i in range(4):
                space_free_r = True
                if not (tetris_mx[figure_y + i][figure_x + 1] == '.'):
                    space_free_r = False
            if space_free_r:
                figure_x += 1
        clock += 1
        if tetris_mx[figure_y + 4][figure_x] == '.':
            figure_y += 1
            for i in range(4):
                tetris_mx[figure_y + i - 1] = tetris_mx[figure_y + i - 1].replace('@', '.')
            for i in range(4):
                tetris_mx[figure_y + i] = tetris_mx[figure_y + i][:figure_x] + '@' + tetris_mx[figure_y + i][figure_x + 1:]
        else:
            for i in range(4):
                tetris_mx[figure_y + i] = tetris_mx[figure_y + i].replace('@', '.')
                tetris_mx[figure_y + i] = tetris_mx[figure_y + i][:figure_x] + '@' + tetris_mx[figure_y + i][figure_x + 1:]
        print_mx(tetris_mx)
        print(command(clock))
    for i in range(4):
        tetris_mx[figure_y + i] = tetris_mx[figure_y + i].replace('@', '#')
    return [tetris_mx, clock]



def square(tetris_mx, clock):
    tetris_mx.reverse()
    for i in range(2): tetris_mx.append('..@@...')
    tetris_mx.reverse()
    space_free_l, space_free_r = True, True
    figure_x = 2
    figure_y = 0
    print_mx(tetris_mx)
    print(command(clock))
    while figure_y + 2 < len(tetris_mx) and tetris_mx[figure_y + 2][figure_x:figure_x + 2] == '..':
        pass
    return [tetris_mx, clock]


while clock < 50:
    while len(tetris_mx) > 0 and tetris_mx[0] == empty_str:
        tetris_mx.pop(0)
    tetris_mx.reverse()
    for i in range(3): tetris_mx.append(empty_str)
    tetris_mx.reverse()
    tetris_mx, clock = vertical_stick(tetris_mx, clock)
    print_mx(tetris_mx)
    tetris_mx, clock = horizontal_stick(tetris_mx, clock)
    print_mx(tetris_mx)
    # tetris_mx, clock = square(tetris_mx, clock)
    # print_mx(tetris_mx)
    print('                     cycle!')

# while stable_rocks < 6:
#     for i in range(3):
#         if tetris_mx[i] != empty_str:
#             tetris_mx.reverse()
#             for k in range(3 - i):
#                 tetris_mx.append(empty_str)
#             tetris_mx.reverse()
#
#     if stable_rocks % 5 == 0:
#         tetris_mx = horizontal_stick(tetris_mx, clock)
#
#     clock += 1
