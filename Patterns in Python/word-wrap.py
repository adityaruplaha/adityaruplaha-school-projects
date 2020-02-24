#| /usr/bin/env python

S = input("Enter string: ")

if len(S) % 2:
    S += " "
a = len(S)//2

for i in range(a):
    s = S[i] + ' '*(2*a - 1 - 2*i) + S[-i-1]
    print(s.center(2*a + 1))
