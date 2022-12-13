import numpy as np
infile = '91.txt'
data = open(infile).read().strip()
lines = [[x.split()[0], int(x.split()[1])] for x in data.split('\n')]

n = sum([x[1] for x in lines])
hgrid = np.zeros([2*n+1, 2*n+1])
tgrid = np.zeros([2*n+1, 2*n+1])

# Initializing the starting Position :
hgrid[n, n], tgrid[n, n] = 1, 1
hi, hj = n, n
ti, tj = n, n

print(hgrid.compress(np.all(hgrid == 0, axis=0), axis=1))
print(tgrid)
# def tail_loc():


# for line in lines:
#     print(line)
#     if line[0] == 'R':
#         for step in range(1, line[1]+1):
#             hgrid[hi, hj+1] = 1
#             tgrid[ti, tj] = 1
#             j += 1
#     elif line[0] == 'L':
#         hgrid[m, :line[1]+1] = 1
#     elif line[0] == 'U':
#         ...
#     else:
#         ...
#     print(hgrid)
#     print(tgrid)
