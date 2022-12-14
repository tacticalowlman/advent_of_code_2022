with open('input') as f:
    lines = f.readlines()

def letters_to_nums(lines):
    height_mx=[]
    for i in lines:
        height_ln=[]
        for k in i.strip():
            if k=='S':
                height_ln.append(1)
            elif k=='E':
                height_ln.append(27)
            else:
                height_ln.append(abc.find(k)+1)
        height_mx.append(height_ln)
    return height_mx


abc='abcdefghijklmnopqrstuvwxyz'
height_mx=letters_to_nums(lines)
start_point=[0, 0]
end_point=[2, 5]
#start_point=[20, 0]
#end_point=[20, 138]
min_path_length=len(height_mx)*len(height_mx)


def close_points(path):
    x, y=path[-1]
    close_points=[]
    if not(x==end_point[1] and y==end_point[0]):
        if abs(height_mx[x+1][y]-height_mx[x][y])<=1 and not ([x+1, y] in path):
            close_points.append([x+1, y])
        if abs(height_mx[x-1][y]-height_mx[x][y])<=1 and not ([x-1, y] in path):
            close_points.append([x-1, y])
        if abs(height_mx[x][y+1]-height_mx[x][y])<=1 and not ([x, y+1] in path):
            close_points.append([x, y+1])
        if abs(height_mx[x][y-1]-height_mx[x][y])<=1 and not ([x, y-1] in path):
            close_points.append([x, y-1])
    return close_points


path=[[start_point[1], start_point[0]]]
paths={path[-1]:close_points(path)}


while True:





#print(height_mx, sep='\n')

