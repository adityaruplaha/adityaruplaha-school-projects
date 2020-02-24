#! /usr/bin/env python

def magic(n : int) -> str:
    if n % 4:
        return '*'
    else:
        return ' '

w = int(input("Enter max width: "))
W = 2*w - 1

for i in range (1, w):
    L = map(magic, range(1, i+1))
    S = ' '.join(L).center(W)
    print(S)

for i in range (w, 0, -1):
    L = map(magic, range(1, i+1))
    S = ' '.join(L).center(W)
    print(S)
