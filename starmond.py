#! /usr/bin/env python

n = int(input("Diamond seedval: "))

print(' '*n, '*', ' '*n)

for i in range(1, n):
    ps = n - i
    print(' '*ps, '*', ' '*(2*i - 3), '*', ' '*ps)

for i in range(n, 0, -1):
    ps = n - i
    print(' '*ps, '*', ' '*(2*i - 3), '*', ' '*ps)

print(' '*n, '*', ' '*n)