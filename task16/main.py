with open('input') as f:
    lines = f.readlines()

graph = {}

for i in lines:
    ls = i.split()
    nbrs = []
    gphs = False
    print(ls)
    for k in ls:
        print(k)
        if gphs:
            if k[-1] != ',':
                nbrs.append(k)
            else:
                nbrs.append(k[:-1])
        if k == 'valves' or k == 'valve':
            gphs = True
    graph[ls[1]] = [int(ls[4].split('=')[1][:-1]), nbrs]


def evaluate_branches(graph):
    visited = ['AA']
    to_visit = []
    trees = []
    start_nbrs = graph['AA'][1]
    [to_visit.append(i) for i in start_nbrs]
    for i in to_visit:
        trees.append({i: graph[i][1]})
    to_visit = []
    for i in trees:
        to_visit = list(i.values())
        print(to_visit)
        while to_visit:
            point = to_visit.pop(0)
            if point not in visited:
                for k in graph[point]:
                    if k not in visited:
                        to_visit.append(k)
                        visited.append(k)
                        i[k] = graph[k]
    print(trees)

evaluate_branches(graph)

print(graph)
