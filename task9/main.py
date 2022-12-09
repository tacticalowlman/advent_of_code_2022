import turtle

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

# def intermediate_position(xy_intermediate):
#     for i in range(1, 10):
#         x_h_pr, y_h_pr = xy_intermediate[i-1]
#         x_i, y_i=xy_intermediate[i]
#         xy_intermediate[i]current_tails_position(x_h, y_h, x_i, y_i, x_h_pr, y_h_pr)
#
#         x_h, y_h=x_i, y_i
#     return x_h, y_h


# s = turtle.getscreen()
# t = turtle.Turtle()
x_h, y_h=0, 0
x_t, y_t=0, 0
x_h_pr, y_h_pr=0, 0
xy_visited=[]
# xy_intermediate=[]
# xy_intermediate.append([x_h, y_h])
# for i in range[9]:
#     xy_intermediate.append([0, 0])

for i in lines:
    direction=i.split()[0]
    steps=int(i.split()[1])
    print(direction, steps)
    if direction=='U':
        for k in range(steps):
            y_h_pr=y_h
            y_h+=1
            x_t, y_t = current_tails_position(x_h, y_h, x_t, y_t, x_h_pr, y_h_pr)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
            #turtle.goto(x_t*10, y_t*10)
            print(x_h, y_h, x_t, y_t)
    elif direction=='D':
        for k in range(steps):
            y_h_pr = y_h
            y_h-=1
            x_t, y_t = current_tails_position(x_h, y_h, x_t, y_t, x_h_pr, y_h_pr)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
            #turtle.goto(x_t*10, y_t*10)
            print(x_h, y_h, x_t, y_t)
    elif direction == 'R':
        for k in range(steps):
            x_h_pr=x_h
            x_h+=1
            x_t, y_t = current_tails_position(x_h, y_h, x_t, y_t, x_h_pr, y_h_pr)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
            #turtle.goto(x_t*10, y_t*10)
            print(x_h, y_h, x_t, y_t)
    elif direction == 'L':
        for k in range(steps):
            x_h_pr = x_h
            x_h-=1
            x_t, y_t = current_tails_position(x_h, y_h, x_t, y_t, x_h_pr, y_h_pr)
            if [x_t, y_t] not in xy_visited:
                xy_visited.append([x_t, y_t])
            #turtle.goto(x_t*10, y_t*10)
            print(x_h, y_h, x_t, y_t)
    #print(x_h, y_h, x_t, y_t)
    #print(len(xy_visited))
    #print(xy_visited)

print(len(xy_visited))
#print(xy_visited)
