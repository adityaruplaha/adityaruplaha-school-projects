#! /usr/bin/env python

from random import randint

def test(a : int, b : int) -> bool:
    p = (-a) // b
    q = a // (-b)
    S = p == q
    print("-{a}//{b} == {a}//-{b} : {S}".format(a=a, b=b, S=S))
    return S

I = True

N = 10000

for _ in range(N):
    A = randint(0, 1000000)
    B = randint(1, 1000000)
    I &= test(A, B)

print("Assertion: [(-a) // b] == [a // (-b)].")
print("Unit testing {n} elements: {i}".format(n=N, i=I))
