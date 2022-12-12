with open('input') as f:
    lines = f.readlines()

abc='abcdefghijklmnopqrstuvwxyz'

def letters_to_nums(lines):
    height_mx=[]
    for i in lines:
        height_ln=[]
        for k in i.strip():
            if k=='S':
                height_ln.append(0)
            elif k=='E':
                height_ln.append(28)
            else:
                height_ln.append(abc.find(k)+1)
        height_mx.append(height_ln)
    return height_mx

height_mx=letters_to_nums(lines)

def path_finder(height_mx):
    


print(*letters_to_nums(lines), sep='\n')

