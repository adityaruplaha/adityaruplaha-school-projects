#! /usr/bin/env python
 
from math import log, tan, fabs, ceil

# x-scaling factor
f = 0.05
# y-scaling factor
Q = 5

for i in range(1, 301):
    S = ceil(Q*fabs(tan(i*f) + log(i*f)))
    if S > 200:
        continue
    print(' '*S, '*')
