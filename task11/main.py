import re
import copy

with open('input') as f:
    lines = f.readlines()

def extract_monkeys(lines):
    monkeys = []
    new_monkey = []
    ct = 0
    for i in lines:
        if i == '\n':
            ct = -1
            monkeys.append(new_monkey)
            new_monkey = []
        else:
            if ct != 2:
                new_monkey.append([int(i) for i in re.findall('[0-9]+', i)])
            else:
                new_monkey.append(i[i.find('=') + 5:].strip().split())
        ct += 1
    monkeys.append(new_monkey)
    return monkeys

def monkey_mode(monkeys, k):
    monkey=monkeys[k]
    ct=0
    for i in monkey[1]:
        if monkey[2][0]=='+':
            if monkey[2][1] == 'old':
                monkey_thing =(i+i)
            else:
                monkey_thing=(i+int(monkey[2][1]))
        else:
            if monkey[2][1] == 'old':
                monkey_thing = (i*i)
            else:
                monkey_thing = (i*int(monkey[2][1]))
        monkey_thing=monkey_thing
        if monkey_thing%monkey[3][0]==0:
            monkeys[monkey[4][0]][1].append(monkey_thing)
        else:
            monkeys[monkey[5][0]][1].append(monkey_thing)
        ct+=1
    answer=[monkeys, ct]
    return answer

def max_activity(monkey_activity):
    mx1 = 0
    mx2 = 0
    for i in monkey_activity:
        print(i, mx1, mx2)
        if i > mx1:
            if i > mx2:
                mx1 = mx2
                mx2 = i
            else:
                mx1 = i
    return mx1*mx2

monkeys=extract_monkeys(lines)
monkey_activity=[0 for i in monkeys]

#PART1
for i in range(10000):
    print(i)
    for k in range(len(monkeys)):
        monkeys, ct=monkey_mode(monkeys, k)
        monkey_activity[k]+=ct
        monkeys[k][1]=[]

print(max_activity(monkey_activity))
print(monkeys)

