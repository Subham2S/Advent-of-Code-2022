import sys
infile = '2.txt'
data = open(infile).read().strip()
lines = [x.strip() for x in data.split('\n')]

# Part 1


def score(x):
    y = x.strip().split()
    s1 = 1 if y[1] == 'X' else 2 if y[1] == 'Y' else 3
    p, q = y[0], y[1]
    s2 = 6 if (((p == 'A') & (q == 'Y')) | ((p == 'B') & (q == 'Z')) |
               ((p == 'C') &
                (q == 'X'))) else 3 if (((p == 'A') & (q == 'X')) |
                                        ((p == 'B') & (q == 'Y')) |
                                        ((p == 'C') & (q == 'Z'))) else 0
    s = s1 + s2
    return s


total_score = 0
for line in lines:
    total_score += score(line)

print(total_score)

# Part 2


def score2(x):
    y = x.strip().split()
    s1 = 0 if y[1] == 'X' else 3 if y[1] == 'Y' else 6
    p, q = y[0], y[1]
    s2 = 3 if (((p == 'A') & (q == 'X')) | ((p == 'B') & (q == 'Z')) |
               ((p == 'C') &
                (q == 'Y'))) else 2 if (((p == 'A') & (q == 'Z')) |
                                        ((p == 'B') & (q == 'Y')) |
                                        ((p == 'C') & (q == 'X'))) else 1
    s = s1 + s2
    return s


total_score2 = 0
for line in lines:
    total_score2 += score2(line)
print(total_score2)
