from collections import defaultdict
infile = '3.txt'
data = open(infile).read().strip()
lines = [x.strip() for x in data.split('\n')]
alp = 'abcdefghijklmnopqrstuvwxyz'
Values = defaultdict(int)
for i in alp:
    Values[i] = alp.find(i) + 1
    Values[i.upper()] = alp.find(i) + 27

# Part 1
sum_ = 0
for line in lines:
    l = int(len(line)/2)
    sum_ += Values[set([x for x in line[:l] if x in line[l:]]).pop()]

print(sum_)

# Part 2
grp_sum = 0
i = 0
for i in range(0, len(lines), 3):
    grp_sum += Values[set([x for x in lines[i]
                          if ((x in lines[i+1]) & (x in lines[i+2]))]).pop()]

print(grp_sum)
