from collections import defaultdict
import re
infile = '5.txt'
data = open(infile).read()
lines = [x for x in data.split('\n')]

moves = []
stacks = defaultdict(list)
for line in lines:
    if line.__contains__('['):
        print(line)
        for match in re.finditer(r'([A-Z])', line):
            stacks[int((match.start()-1)/4)].append(match.__getitem__(0))
    if line.__contains__('move'):
        moves.append(line)
stacks = {k: stacks[k] for k in sorted(stacks)}
stacks1 = stacks.copy()
print('before:', stacks)

# Part 1
for move in moves:
    m = [int(x) for x in re.findall(r'\d+', move)]
    stacks[m[2]-1] = stacks[m[2]-1][::-1]
    stacks[m[2]-1].extend(stacks[m[1]-1][:m[0]])
    stacks[m[2]-1] = stacks[m[2]-1][::-1]
    stacks[m[1]-1] = stacks[m[1]-1][m[0]:]
print('after:', stacks)
print(''.join([x[0] for x in stacks.values()]))

# Part 2
for move in moves:
    m = [int(x) for x in re.findall(r'\d+', move)]
    stacks1[m[2]-1] = stacks1[m[2]-1][::-1]
    stacks1[m[2]-1].extend(stacks1[m[1]-1][:m[0]][::-1])
    stacks1[m[2]-1] = stacks1[m[2]-1][::-1]
    stacks1[m[1]-1] = stacks1[m[1]-1][m[0]:]
print('after2:', stacks1)
print(''.join([x[0] for x in stacks1.values()]))
