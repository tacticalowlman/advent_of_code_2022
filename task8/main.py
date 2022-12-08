with open('input') as f:
    lines = f.readlines()
trs_hdn_mx=[]
for i in lines:
    trs_ln=[]
    for k in lines[i]:
        trs_ln.append(int(lines[i][k].strip()))
    trs_hdn_mx.append(trs_ln)

print(trs_hdn_mx)

def check_h(line):
    max_h=0
    ths_hdn_ln=[]
    for i in line:
        ii=int(i)
        if ii>0 and ii<99 and ii<=max_h:
            print(ii, max_h, 'h')
            ths_hdn_ln.append('h')
        else:
            print(ii, max_h, 'v')
            ths_hdn_ln.append('v')
        if ii>max_h:
            max_h=ii
    return ths_hdn_ln

# print('231424301543353234613653325560166326262063626431047044000133041410622363320013444135310231215142114')
# print(check_h('231424301543353234613653325560166326262063626431047044000133041410622363320013444135310231215142114'))


def rows_to_cols(lines):
    new_mx=[]
    for i in lines:
        newst=''
        for k in lines:
            newst+=lines[k][i]
        new_mx.append(newst)
    return new_mx

# print(lines)
# print(rows_to_cols(lines))
