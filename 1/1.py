import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else '7.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
