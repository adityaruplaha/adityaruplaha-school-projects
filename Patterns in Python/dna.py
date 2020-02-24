#! /usr/bin/env python 

from math import sin, cos, ceil
from random import choice

bases = [('A','T'), ('T','A'), ('G','C'), ('C','G')]

f = 0.1
Q = 20
ph = -0.08

for i in range(1000):
    p1 = ceil(Q*(1.03 + sin(i*f)))
    p2 = ceil(Q*(1.03 + cos(i*f + ph)))
    s1 = min(p1, p2)
    s2 = max(p1, p2) - s1 - 1
    b1, b2 = choice(bases)
    print(' '*s1 + b1 + '-'*s2 + b2)
