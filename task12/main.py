with open('input') as f:
    lines = f.readlines()

abc='abcdefghijklmnopqrstuvwxyz'

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

height_mx=letters_to_nums(lines)
start_point=[0, 0]
end_point=[2, 5]
#start_point=[20, 0]
#end_point=[20, 138]
min_path_length=len(height_mx)*len(height_mx)

def path_finder(x, y, min_path_length, current_path_length):
    if abs(height_mx[x+1][y]-height_mx[x][y])<=1:
        current_path_length += 1
        if x+1==end_point[1] and y==end_point[0]:
            if current_path_length<min_path_length:
                min_path_length=current_path_length
            ret = [x + 1, y, min_path_length, current_path_length-1]
            return ret
        else:
            return path_finder(x+1, y, min_path_length, current_path_length)
    if abs(height_mx[x][y+1]-height_mx[x][y])<=1:
        current_path_length += 1
        if x==end_point[1] and y+1==end_point[0]:
            if current_path_length<min_path_length:
                min_path_length=current_path_length
            ret=[x, y+1, min_path_length, current_path_length-1]
            return ret
        else:
            return path_finder(x, y+1, min_path_length, current_path_length)
    if abs(height_mx[x-1][y]-height_mx[x][y])<=1:
        current_path_length += 1
        if x-1==end_point[1] and y==end_point[0]:
            if current_path_length<min_path_length:
                min_path_length=current_path_length
            ret = [x-1, y, min_path_length, current_path_length-1]
            return ret
        else:
            return path_finder(x-1, y, min_path_length, current_path_length)
    if abs(height_mx[x][y-1]-height_mx[x][y])<=1:
        current_path_length += 1
        if x==end_point[1] and y+1==end_point[0]:
            if current_path_length<min_path_length:
                min_path_length=current_path_length
            ret = [x, y-1, min_path_length, current_path_length-1]
            return ret
        else:
            return path_finder(x, y-1, min_path_length, current_path_length)
    return path_finder(x+1, y, min_path_length, current_path_length)




#print(height_mx, sep='\n')

