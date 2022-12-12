import numpy as np
infile = '8.txt'
data = open(infile).read().strip()
lines = [[int(y) for y in str(x)] for x in data.split('\n')]
grid = np.array(lines)

# Part - 1
print(grid)
c = 2 * ((grid.shape[0]-1) + (grid.shape[1]-1))
for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        #print(f'{grid[i, j]}, up:{all(grid[i, j] > grid[:i, j])} down:{all(grid[i, j] > grid[i+1:, j])} left:{all(grid[i, j] > grid[i, :j])} right:{all(grid[i, j] > grid[i, j+1:])}')
        if ((all(grid[i, j] > grid[:i, j]) | all(grid[i, j] > grid[i+1:, j]) |
             all(grid[i, j] > grid[i, :j]) | all(grid[i, j] > grid[i, j+1:]))):
            c += 1
    # print('\n')
print(c)

# Part - 2
ss = np.ones_like(grid)
for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        s_ = 0
        for u in range(i-1, -1, -1):
            if grid[i, j] > grid[u, j]:
                s_ += 1
            else:
                s_ += 1
                break
        ss[i, j] *= s_
        s_ = 0
        for d in range(i+1, grid.shape[0], 1):
            if grid[i, j] > grid[d, j]:
                s_ += 1
            else:
                s_ += 1
                break
        ss[i, j] *= s_
        s_ = 0
        for l in range(j-1, -1, -1):
            if grid[i, j] > grid[i, l]:
                s_ += 1
            else:
                s_ += 1
                break
        ss[i, j] *= s_
        s_ = 0
        for r in range(j+1, grid.shape[1], 1):
            if grid[i, j] > grid[i, r]:
                s_ += 1
            else:
                s_ += 1
                break
        ss[i, j] *= s_

print(ss)
print(np.max(ss))
