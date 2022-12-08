import sys
from collections import defaultdict
infile = '1.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
