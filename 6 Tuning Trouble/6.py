infile = '6.txt'
data1 = open(infile).read().strip().split('\n')
data = data1[0]
# Part 1
c = 0
for i in range(4, len(data)):
    if (data[i-4:i][0] not in data[i-4:i][1:]) & (data[i-4:i][1] not in data[i-4:i][2:]) & (data[i-4:i][2] != data[i-4:i][3]):
        print(data[i-4:i])
        c = i
        break
print(c)

# Part 2
for d in data1:
    c1 = 0
    for i in range(14, len(d)):
        if (len(d[i-14:i]) == len(set(d[i-14:i]))):
            c1 = i
            print(d[:i])
            break
    print(c1)
