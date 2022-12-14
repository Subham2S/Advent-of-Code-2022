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

# PART 1

# Initializing the starting Position :
hi, hj, ti, tj = n, n, n, n
hgrid[hi, hj], tgrid[ti, tj] = 1, 1


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
                (((h1 == t1 + 1) | (h1 == t1 - 1)) & (h2 == t2 + 1))):
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
    #print(s, h1, h2, t1, t2)
    return h1, h2, t1, t2


def save_array(x, y):
    x = x[~np.all(x == 0, axis=1)]
    x = x[:, np.any(x, axis=0)]
    pd.DataFrame(x).to_csv(f'./{y}.csv')


for line in lines:
    s_ = line[0]
    # print(line)
    i = 1
    while i <= line[1]:
        hi, hj, ti, tj = tail_loc(hi, hj, ti, tj, s_)
        hgrid[hi, hj] = 1
        tgrid[ti, tj] = 1
        i += 1

# Save into CSV files:
save_array(hgrid, 'h')
save_array(tgrid, 't')
print(np.sum(tgrid))

# PART 2
