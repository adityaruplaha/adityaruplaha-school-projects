#! /usr/bin/env python

from randlist import randlist

L = randlist(-10000, 10000, 100)
print("Sorting:\n{}".format(L))

for i in range(1, len(L)):
    e = L[i]
    j = i - 1
    while L[j] > e and j >= 0:
        L[j+1] = L[j]
        j -= 1
    else:
        L[j+1] = e

print("Result:\n{}".format(L))
