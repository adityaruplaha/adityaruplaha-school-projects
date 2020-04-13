#! /usr/bin/env python

from randlist import randlist

L = randlist(-10000, 10000, 100)
print("Sorting:\n{}".format(L))

for i in range(len(L) - 1):
    for j in range(len(L) - 1 - i):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

print("Result:\n{}".format(L))
