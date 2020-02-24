#! /usr/bin/env python

def magic(n : int) -> list:
    L = ['*']*n
    for j in range(n//2):
        if j % 2:
            L[j] = ' '
    for j in range(-1, -n//2 - 1, -1):
        if (-j) % 2 == 0:
            L[j] = ' '
    return L

w = int(input("Enter max width: "))
W = 2*w - 1

for i in range (1, w):
    L = magic(i)
    S = ' '.join(L).center(W)
    print(S)

for i in range (w, 0, -1):
    L = magic(i)
    S = ' '.join(L).center(W)
    print(S)
