# From a list of strings, drop 1st char of each element

L = eval(input("Enter a list of strings: "))

N = []

for e in L:
    N.append(e[1:])

print("Required list is:", N)
