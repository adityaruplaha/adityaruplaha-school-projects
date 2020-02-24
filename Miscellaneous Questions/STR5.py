#! /usr/bin/env python

'''
(This question is super complicated and artificial.)
(Refer Sumita Arora: Strings Q5)
'''

A = int(input("Enter the integer: "))
S = input("Enter the string: ")

# extract digits
D = int(''.join( e for e in S if e.isdigit() ))

R = A + D

print("{} + {} = {}".format(A, D, R))
