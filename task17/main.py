f = open('input', 'r')

input_st = f.read()

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
    print_mx(tetris_mx)
    print(command(clock), '\n')
    if command(clock) == '<':
        tetris_mx[0] = '.@@@@..'
    else:
        tetris_mx[0] = '...@@@@'
    figure_pos = tetris_mx[0].find('@')
    clock += 1
    next_st = tetris_mx[1][figure_pos:figure_pos + 4]
    while next_st != '' and next_st == '....':
        print_mx(tetris_mx)
        print(command(clock), clock, '\n')
        figure_pos = tetris_mx[0].find('@')
        if command(clock) == '<' and figure_pos != 0:
            figure_pos -= 1
        elif command(clock) == '>' and figure_pos != 3:
            figure_pos += 1
        tetris_mx[1] = tetris_mx[1][:figure_pos] + '@@@@' + tetris_mx[1][figure_pos + 4:]
        tetris_mx.pop(0)
        if len(tetris_mx) != 1:
            next_st = tetris_mx[1][figure_pos:figure_pos + 4]
        else:
            next_st = ''
        clock += 1
    return [tetris_mx, clock]


def vertical_stick(tetris_mx, clock):
    tetris_mx.reverse()
    for i in range(4): tetris_mx.append('..@....')
    tetris_mx.reverse()
    print_mx(tetris_mx)
    figure_pos = tetris_mx[0].find('@')
    if command(clock) == '<':
        for i in range(4): tetris_mx[i] = '.@.....'
    else:
        for i in range(4): tetris_mx[i] = '...@...'
    clock += 1
    next_st = tetris_mx[1][figure_pos]
    while next_st != '' and next_st == '.':
        merge_st = tetris_mx[1]
        tetris_mx[1] = tetris_mx[0]
        tetris_mx.pop(0)
        new_st = ''
        figure_pos = tetris_mx[0].find('@')
        if command(clock) == '<' and figure_pos != 0:
            figure_pos -= 1
            new_st = merge_st[:figure_pos] + '@' + merge_st[figure_pos + 1:]
            for i in range(4): tetris_mx[i] = new_st

            figure_pos -= 1
            tetris_mx[0] = new_st



        elif command(clock) == '>' and figure_pos != 3:
            figure_pos += 1
            for i in range(figure_pos): new_st += '.'
            new_st += '@'
            for i in range(6 - figure_pos): new_st += '.'
            for i in range(4): tetris_mx[i] = new_st
        if len(tetris_mx) != 1:
            next_st = tetris_mx[1][figure_pos:figure_pos + 4]
        else:
            next_st = ''
        clock += 1
    return [tetris_mx, clock]


while clock < 100:
    for i in range(3):
        if tetris_mx[i] != empty_str:
            tetris_mx.reverse()
            for k in range(3 - i):
                tetris_mx.append(empty_str)
            tetris_mx.reverse()
    tetris_mx, clock = horizontal_stick(tetris_mx, clock)
    print_mx(tetris_mx)
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
