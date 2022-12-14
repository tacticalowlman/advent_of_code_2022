import json

with open('input') as f:
    lines = f.readlines()


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
                height_ln.append(26)
                height_ln2.append(26)
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

print('SAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', coord_translator_reverse(*end_point))


def itera(start_point):
    queue = [coord_translator_reverse(*start_point)]
    visited = []
    dists = {coord_translator_reverse(*start_point): 0}
    prs={}
    while queue != []:
        # print(queue)
        el = queue.pop(0)
        if el in graph:
            for i in graph[el]:
                if i not in visited:
                    dists[i] = dists[el] + 1
                    visited.append(i)
                    queue.append(i)
                    prs[i]=el
                    if i == 3358:
                        res_path = []
                        cur_vertex = 3358
                        while cur_vertex != coord_translator_reverse(*start_point):
                            res_path.append(cur_vertex)
                            cur_vertex = prs[cur_vertex]
                        res_path = list(reversed(res_path))
                        if True:
                            print(res_path)
                            print(' '.join(map(lambda x: str(height_mx[coord_translator(x)[1]][coord_translator(x)[0]]), res_path)))
                            #abc(x)[1], abc(x)[0]
                        return dists[3358]

    return 10000

import queue
import typing

T = typing.TypeVar('T')


def bfs(
        connections_list: typing.Dict[T, typing.List[T]],
        start: T,
        target: T,
) -> typing.Tuple[typing.Dict[T, T], typing.Dict[T, int], bool]:
    print(start, target)
    vertexes_queue = queue.Queue()
    visited = {start: True}
    dists_from_start = {start: 0}
    parents = {}
    vertexes_queue.put(start)
    while not vertexes_queue.empty():
        checking_vertex = vertexes_queue.get()
        #print('AAAA', connections_list, connections_list[checking_vertex])
        if checking_vertex not in connections_list:  # some vertexes dont have any connections
            continue
        for neighbour_vertex in connections_list[checking_vertex]:
            if not visited.get(neighbour_vertex, False):
                visited[neighbour_vertex] = True
                dists_from_start[neighbour_vertex] = dists_from_start[checking_vertex] + 1
                parents[neighbour_vertex] = checking_vertex
                vertexes_queue.put(neighbour_vertex)
                if neighbour_vertex == target:
                    return parents, dists_from_start, True
    return parents, dists_from_start, False


def construct_path_from_bfs(paths: typing.Dict[int, T], start: T, target: T) -> typing.List[T]:
    res_path = []
    cur_vertex = target
    while cur_vertex != start:
        res_path.append(cur_vertex)
        print(coord_translator(cur_vertex), height_mx[coord_translator(cur_vertex)[1]][coord_translator(cur_vertex)[0]])
        cur_vertex = paths[cur_vertex]
    res_path = list(reversed(res_path))
    return res_path



min=10000

for i in graph:
    start_point=coord_translator(i)
    if height_mx[start_point[1]][start_point[0]]==1:
        print(min)
        print(start_point, height_mx[start_point[1]][start_point[0]])
        prs, dist, exists=bfs(graph.copy(), i, 3358)
        print(graph[i])
        print(exists)
        if exists and dist[3358]<min:
            y=prs
            x=i
            min=dist[3358]

print('as')
print(prs)
print(construct_path_from_bfs(y, x, 3358))
print(min)

print(coord_translator(3358))
