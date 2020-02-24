#! /usr/bin/env python

'''
To find the mean of elements of a nested tuple T, and to find the mean of means.
'''

T = eval(input("Enter a nested tuple of numbers: "))

S = 0

for i in range(len(T)):
    s = 0
    for e in T[i]:
        s += e
    
    s /= len(T[i])
    S += s

    print("Mean of element {}:".format(i), s)

S /= len(T)

print("Mean of means:", S)
