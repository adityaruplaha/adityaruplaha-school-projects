# Minimum of 3 numbers & check if they are all equal

print("Enter 3 no.s:")
a = float(input())
b = float(input())
c = float(input())

m = a
L = [a, b, c]
for e in L:
    if e < m:
        m = e

print("Minimum:", m)

if a == b == c:
    print("They are all equal.")
else:
    print("They are not all equal.")
