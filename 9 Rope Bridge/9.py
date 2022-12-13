import pandas as pd
#import sys
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)
infile = '9.txt'
data = open(infile).read().strip()
lines = [[x.split()[0], int(x.split()[1])] for x in data.split('\n')]

n = sum([x[1] for x in lines])
hgrid = np.zeros([2*n+1, 2*n+1])
tgrid = np.zeros([2*n+1, 2*n+1])

# Initializing the starting Position :
hi, hj, ti, tj = n, n, n, n
hgrid[hi, hj], tgrid[ti, tj] = 1, 1

# print(hgrid.compress(np.all(hgrid == 0, axis=0), axis=1))
# print(tgrid)


def tail_loc(h1, h2, t1, t2, s):
    if s == 'R':
        if (((h1 == t1) & (h2 == t2)) | ((h1 == t1) & (h2 == t2 - 1)) |
            (((h1 == t1 + 1) | (h1 == t1 - 1)) & (h2 == t2)) |
                (((h1 == t1 + 1) | (h1 == t1 - 1)) & (h2 == t2 - 1))):
            h2 += 1
        elif ((h1 == t1) & (h2 == t2 + 1)):
            h2 += 1
            t2 += 1
        else:
            t1, t2 = h1, h2
            h2 += 1
    elif s == 'L':
        if (((h1 == t1) & (h2 == t2)) | ((h1 == t1) & (h2 == t2 + 1)) |
            (((h1 == t1 + 1) | (h1 == t1 - 1)) & (h2 == t2)) |
                (((h1 == t1 + 1) | (h1 == t1 - 1)) & (h2 == t2 - 1))):
            h2 -= 1
        elif ((h1 == t1) & (h2 == t2 - 1)):
            h2 -= 1
            t2 -= 1
        else:
            t1, t2 = h1, h2
            h2 -= 1
    elif s == 'U':
        if (((h1 == t1) & (h2 == t2)) | ((h2 == t2) & (h1 == t1 + 1)) |
            (((h2 == t2 + 1) | (h2 == t2 - 1)) & (h1 == t1)) |
                (((h2 == t2 + 1) | (h2 == t2 - 1)) & (h1 == t1 + 1))):
            h1 -= 1
        elif ((h2 == t2) & (h1 == t1 - 1)):
            h1 -= 1
            t1 -= 1
        else:
            t1, t2 = h1, h2
            h1 -= 1
    else:
        if (((h1 == t1) & (h2 == t2)) | ((h2 == t2) & (h1 == t1 - 1)) |
            (((h2 == t2 + 1) | (h2 == t2 - 1)) & (h1 == t1)) |
                (((h2 == t2 + 1) | (h2 == t2 - 1)) & (h1 == t1 - 1))):
            h1 += 1
        elif ((h2 == t2) & (h1 == t1 + 1)):
            h1 += 1
            t1 += 1
        else:
            t1, t2 = h1, h2
            h1 += 1
    #print(h1, h2, t1, t2)
    return h1, h2, t1, t2


for line in lines:
    s_ = line[0]
    # print(line)
    i = 1
    while i <= line[1]:
        hi, hj, ti, tj = tail_loc(hi, hj, ti, tj, s_)
        hgrid[hi, hj] = 1 if hgrid[hi, hj] == 0 else 1
        tgrid[ti, tj] = 1 if tgrid[ti, tj] == 0 else 1
        i += 1

# pd.DataFrame(hgrid).to_csv('./h.csv')
# pd.DataFrame(tgrid).to_csv('./t.csv')
print(sum(sum(tgrid)))
