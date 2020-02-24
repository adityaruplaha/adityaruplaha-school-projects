#! /usr/bin/env python

'''
To convert a given number to its Roman represenation.
'''

N = int(input("Enter number: "))

R = ""

# thousands
R += 'M'*(N // 1000)
N %= 1000

# hundreds
if N >= 900:
    R += "CM"
    N -= 900
elif 900 > N >= 500:
    R += 'D'
    N -= 500

R += 'C'*(N // 100)
N %= 100

# tens
if N >= 90:
    R += "XC"
    N -= 90
elif 90 > N >= 50:
    R += 'L'
    N -= 50

R += 'X'*(N // 10)
N %= 10

# ones
if N == 9:
    R += "IX"
elif 9 > N >= 5:
    R += 'V'
    N -= 5
    R += 'I'*N
elif N == 4:
    R += "IV"
elif 4 > N:
    R += 'I'*N

print("Roman equivalent:", R)
