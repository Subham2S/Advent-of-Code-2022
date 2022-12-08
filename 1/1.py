import sys
from collections import defaultdict
infile = '1.txt'
data = open(infile).read().strip()
lines = [x.strip() for x in data.split('\n')]

elfs = defaultdict(int)
i = 1
for line in lines:
    if line == '':
        i += 1
    else:
        elfs[i] += int(line)

# Part - 1
print(elfs[max(elfs, key=elfs.get)])

# Part - 2
print(sum(
    dict(sorted(elfs.items(), key=lambda item: item[1], reverse=True)[:3]).values()))

# Easier Approach
# Part - 1
print(max(elfs.values()))

# Part - 2
print(sum(sorted(elfs.values(), reverse=True)[:3]))
