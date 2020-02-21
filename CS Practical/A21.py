# Maximum of 3 no.s & sum of no equal no.s

print("Enter 3 no.s:")
a = float(input())
b = float(input())
c = float(input())

m = a
S = 0
L = [a, b, c]
for e in L:
    if e > m:
        m = e
    if L.count(e) == 1:
        S += e

print("Maximum:", m)
print("Sum of non-equal numbers:", S)
