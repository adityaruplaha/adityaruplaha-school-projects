#! /usr/bin/env python

from randlist import randlist

L = randlist(-10000, 10000, 1000)
L.sort()

print("List is:", L)


def binary_search(L, e, low=0, high=len(L)-1):
    mid = (low + high) // 2

    if low == high:
        return low if L[low] == e else -1

    if e > L[mid]:
        return binary_search(L, e, mid+1, high)
    elif e < L[mid]:
        return binary_search(L, e, low, mid-1)
    elif e == L[mid]:
        return mid


e = int(input("Enter element to search: "))
print("Index at:", binary_search(L, e))
