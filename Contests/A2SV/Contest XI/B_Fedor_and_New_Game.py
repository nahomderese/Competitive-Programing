import sys
from collections import *
from itertools import *
from math import *

n,m,k = [int(i) for i in sys.stdin.readline().split()]
y = []
for i in range(m):
    y.append(int(sys.stdin.readline().strip()))
    
fedor = int(sys.stdin.readline().strip())
u = [1 for x in y if (x^fedor).bit_count() <= k]
print(len(u))