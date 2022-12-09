import numpy as np
infile = '4.txt'
data = open(infile).read().strip()
lines = [x.strip() for x in data.split('\n')]

# Part 1
c = 0
for line in lines:
    lim = [[int(x) for x in l.split('-')] for l in line.split(',')]
    if ((lim[0][0] <= lim[1][0]) & (lim[0][1] >= lim[1][1])) | ((lim[0][0] >= lim[1][0]) & (lim[0][1] <= lim[1][1])):
        # print(lim)
        c += 1
print(c)

# Part 2
c2 = 0
for line in lines:
    lim = [[int(x) for x in l.split('-')] for l in line.split(',')]
    if ((lim[0][0] <= lim[1][0] <= lim[0][1]) | (lim[0][0] <= lim[1][1] <= lim[0][1])) | \
       ((lim[1][0] <= lim[0][0] <= lim[1][1]) | (lim[1][0] <= lim[0][1] <= lim[1][1])):
        # print(lim)
        c2 += 1
print(c2)
