with open('input') as f:
    lines = f.readlines()

lines.append('END')

current_symbol_index=0
signal_strength_ct=0
command_index=0
cycle_ct=0
x=1
string_crt=''

# #PART1
# while lines[command_index]!='END':
#     current_command=lines[command_index].split()
#     print(current_command, command_index, cycle_ct, x)
#     if current_command[0]=='addx':
#         for i in range(2):
#             if (cycle_ct + 20) % 40 == 0:
#                 signal_strength = x * cycle_ct
#                 signal_strength_ct += signal_strength
#                 print(cycle_ct, x, x * cycle_ct, signal_strength_ct)
#             cycle_ct += 1
#         x+=int(current_command[1].strip())
#     else:
#         if (cycle_ct + 20) % 40 == 0:
#             signal_strength = x * cycle_ct
#             signal_strength_ct += signal_strength
#             print(cycle_ct, x, x * cycle_ct, signal_strength_ct)
#         cycle_ct+=1
#     command_index+=1
#
#print(signal_strength_ct)

#PART2
while lines[command_index]!='END':
    current_command=lines[command_index].split()
    if current_command[0]=='addx':
        for i in range(2):
            current_symbol_index=cycle_ct % 40
            if current_symbol_index == 0:
                print(string_crt)
                string_crt=''
            if current_symbol_index in [x-1, x, x+1]:
                string_crt+='#'
            else:
                string_crt+='.'
            cycle_ct += 1
        x+=int(current_command[1].strip())
    else:

        current_symbol_index = cycle_ct % 40
        if current_symbol_index == 0:
            print(string_crt)
            string_crt = ''
        if current_symbol_index in [x - 1, x, x + 1]:
            string_crt += '#'
        else:
            string_crt += '.'
        cycle_ct += 1
    command_index+=1

print(string_crt)

