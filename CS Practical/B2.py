# Mean of a list of numbers.

L = eval(input("Enter a list: "))

S = 0
for e in L:
    S += e

print("Mean:", S/len(L))
