# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = float(input("Enter no.: "))
i = int(n)
f = n - i

d =  ""

for t in range(4):
    f *= 2
    p = int(f)
    d += str(p)
    f -= p
    
print("{0}.{1}".format(bin(i), d))
