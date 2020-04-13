#! /usr/bin/env python

from randlist import randlist

L = randlist(-10000, 10000, 100)
print("Sorting:\n{}".format(L))

for i in range(len(L)):
    bj = 0
    for j in range(len(L) - i):
        if L[bj] > L[j]:
            bj = j
    L.append(L.pop(bj))

print("Result:\n{}".format(L))
