import json

with open('input') as f:
    lines = f.readlines()

g = open("input2", "r")

fordendict = json.load(g)


def letters_to_nums(lines):
    height_mx = []
    height_ln = []
    ct = 0
    for i in lines:
        height_ln2 = []
        for k in i.strip():
            if k == 'S':
                height_ln.append(1)
                height_ln2.append(1)
            elif k == 'E':
                height_ln.append(27)
                height_ln2.append(27)
            else:
                if abc.find(k)==25:
                    print(k)
                height_ln.append(abc.find(k) + 1)
                height_ln2.append(abc.find(k) + 1)
            ct += 1
        height_mx.append(height_ln2)
    ret = [height_mx, height_ln]
    return ret


abc = 'abcdefghijklmnopqrstuvwxyz'
height_mx, height_ln = letters_to_nums(lines)

# for i in height_mx:
#     print(i)
# start_point = [0, 0]
# end_point = [2, 5]
start_point = [21, 0]
end_point = [21, 138]
mx_x = len(height_mx[0])
mx_y = len(height_mx)
ct = 0
graph = {}
graph_parents = {}
min_path_length = len(height_mx) * len(height_mx)

# import string
#
# for ind, i in enumerate(height_mx):
#     if 19 < ind < 23:
#         print(''.join(map(lambda x: string.ascii_lowercase[x - 1], i)))
# print(lines[20:22], sep='\n')

def coord_translator(n):
    x = n % mx_x
    y = n // mx_x
    return [x, y]


def coord_translator_reverse(x, y):
    return x * mx_x + y


def conc(ls1, ls2):
    for i in ls2:
        if not (i in ls1):
            ls1.append(i)
    return ls1


def close_points(point):
    y, x = coord_translator(point)
    close_points = []
    if x < mx_y - 1:
        if height_mx[x + 1][y] < height_mx[x][y]:
            close_points.append(coord_translator_reverse(x + 1, y))
        elif abs(height_mx[x + 1][y] - height_mx[x][y]) <= 1:
            close_points.append(coord_translator_reverse(x + 1, y))
    if x > 0:
        if height_mx[x - 1][y] < height_mx[x][y]:
            close_points.append(coord_translator_reverse(x - 1, y))
        elif abs(height_mx[x - 1][y] - height_mx[x][y]) <= 1:
            close_points.append(coord_translator_reverse(x - 1, y))
    if y < mx_x - 1:
        if height_mx[x][y + 1] < height_mx[x][y]:
            close_points.append(coord_translator_reverse(x, y + 1))
        elif abs(height_mx[x][y + 1] - height_mx[x][y]) <= 1:
            close_points.append(coord_translator_reverse(x, y + 1))
    if y > 0:
        if height_mx[x][y - 1] < height_mx[x][y]:
            close_points.append(coord_translator_reverse(x, y - 1))
        elif abs(height_mx[x][y - 1] - height_mx[x][y]) <= 1:
            close_points.append(coord_translator_reverse(x, y - 1))
    return close_points


for i in range(len(height_ln)):
    point = close_points(i)
    points = []
    graph[i] = point

nbrs_of_nbrs = graph[0]
ct = 0
nbrs = []
pp = 0
queue = [coord_translator_reverse(*start_point)]
visited = []
dists = {coord_translator_reverse(*start_point): 0}
print('SAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', coord_translator_reverse(*end_point))


a = {int(k): v for k, v in fordendict.items()}

# print(fordendict)
# for i in range(len(graph)):
#     print(i)
#     try:
#         print(graph[i], a[i])
#     except:
#         print(i)


if a == graph:
    print('HUI')

while queue != []:
    # print(queue)
    el = queue.pop(0)
    for i in graph[el]:
        if i not in visited:
            dists[i] = dists[el] + 1

            visited.append(i)
            queue.append(i)
            if i == 3519:
                break

print(coord_translator(3519))
print(dists[3519])
