#! /usr/bin/env python
 
N = int(input("Enter max hashes: "))
W = 2*N - 1

for i in range(N):
    print("#", end=' ')
print()

for w in range(W-2, 1, -2):
    print(' '*(w-1) + '#')

for i in range(N):
    print("#", end=' ')
print()
