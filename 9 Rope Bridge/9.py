import pandas as pd
#import sys
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)
infile = '93.txt'
data = open(infile).read().strip()
lines = [[x.split()[0], int(x.split()[1])] for x in data.split('\n')]

n = sum([x[1] for x in lines])
hgrid = np.zeros([2*n+1, 2*n+1])
tgrid = np.zeros([2*n+1, 2*n+1])

# PART 1 [H T]
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

# PART 2 [H 1 2 3 4 5 6 7 8 9]
diff_dict = {
    (1, 1): ['D', 'R'],
    (1, -1): ['D', 'L'],
    (-1, 1): ['U', 'R'],
    (-1, -1): ['U', 'L'],
    (0, 1): ['R'],
    (1, 0): ['D'],
    (0, -1): ['L'],
    (-1, 0): ['U'],
    (0, 0): ['O']
}

hgrid = np.zeros([2 * n + 1, 2 * n + 1])
grid1 = np.zeros([2 * n + 1, 2 * n + 1])
grid2 = np.zeros([2 * n + 1, 2 * n + 1])
grid3 = np.zeros([2 * n + 1, 2 * n + 1])
grid4 = np.zeros([2 * n + 1, 2 * n + 1])
grid5 = np.zeros([2 * n + 1, 2 * n + 1])
grid6 = np.zeros([2 * n + 1, 2 * n + 1])
grid7 = np.zeros([2 * n + 1, 2 * n + 1])
grid8 = np.zeros([2 * n + 1, 2 * n + 1])
grid9 = np.zeros([2 * n + 1, 2 * n + 1])


hi, hj = n, n
i1, j1 = n, n
i2, j2 = n, n
i3, j3 = n, n
i4, j4 = n, n
i5, j5 = n, n
i6, j6 = n, n
i7, j7 = n, n
i8, j8 = n, n
i9, j9 = n, n

hgrid[hi, hj] = 1
grid1[i1, j1] = 1
grid2[i2, j2] = 1
grid3[i3, j3] = 1
grid4[i4, j4] = 1
grid5[i5, j5] = 1
grid6[i6, j6] = 1
grid7[i7, j7] = 1
grid8[i8, j8] = 1
grid9[i9, j9] = 1


def chk_shift(i_o, j_o, i_n, j_n):
    row_diff, col_diff = i_n - i_o, j_n - j_o
    # print(row_diff, col_diff)
    steps = abs(row_diff) + abs(col_diff)
    shift_type = diff_dict[(row_diff, col_diff)]
    return shift_type, steps


def next_knot(i_o, j_o, i_n, j_n, i_next, j_next, s_):
    # print(i_o, j_o, i_n, j_n, i_next, j_next, s_)
    st, steps = chk_shift(i_o, j_o, i_n, j_n)

    if steps == 1:
        i_o, j_o, i_next, j_next = tail_loc(i_o, j_o, i_next, j_next, st[0])
    elif steps == 2:
        s__ = s_ if s_ in st else st[0]
        i_o, j_o, i_next, j_next = tail_loc(i_o, j_o, i_next, j_next, s__)
        i_o, j_o, i_next, j_next = tail_loc(i_o, j_o, i_next, j_next,
                                            [x for x in st if x != s__][0])
    else:
        pass
    return i_next, j_next


for line in lines:
    s_ = line[0]
    # print(line)
    i = 1
    while i <= line[1]:
        # Recording past values:
        i1_, j1_ = i1, j1
        i2_, j2_ = i2, j2
        i3_, j3_ = i3, j3
        i4_, j4_ = i4, j4
        i5_, j5_ = i5, j5
        i6_, j6_ = i6, j6
        i7_, j7_ = i7, j7
        i8_, j8_ = i8, j8

        hi, hj, i1, j1 = tail_loc(hi, hj, i1, j1, s_)
        i2, j2 = next_knot(i1_, j1_, i1, j1, i2, j2, s_)
        i3, j3 = next_knot(i2_, j2_, i2, j2, i3, j3, s_)
        i4, j4 = next_knot(i3_, j3_, i3, j3, i4, j4, s_)
        i5, j5 = next_knot(i4_, j4_, i4, j4, i5, j5, s_)
        i6, j6 = next_knot(i5_, j5_, i5, j5, i6, j6, s_)
        i7, j7 = next_knot(i6_, j6_, i6, j6, i7, j7, s_)
        i8, j8 = next_knot(i7_, j7_, i7, j7, i8, j8, s_)
        i9, j9 = next_knot(i8_, j8_, i8, j8, i9, j9, s_)

        # print(hi, hj, i1, j1, i2, j2, i3, j3, i4, j4,
        #       i5, j5, i6, j6, i7, j7, i8, j8, i9, j9)
        # print("\n")
        hgrid[hi, hj] = 1
        grid1[i1, j1] = 1
        grid2[i2, j2] = 1
        grid3[i3, j3] = 1
        grid4[i4, j4] = 1
        grid5[i5, j5] = 1
        grid6[i6, j6] = 1
        grid7[i7, j7] = 1
        grid8[i8, j8] = 1
        grid9[i9, j9] = 1
        i += 1

# Save into CSV files:
save_array(hgrid, 'h')
save_array(grid1, 'tail_1')
save_array(grid2, 'tail_2')
save_array(grid3, 'tail_3')
save_array(grid4, 'tail_4')
save_array(grid5, 'tail_5')
save_array(grid6, 'tail_6')
save_array(grid7, 'tail_7')
save_array(grid8, 'tail_8')
save_array(grid9, 'tail_9')

print(f'Total Positions of 9: {np.sum(grid9)}')
