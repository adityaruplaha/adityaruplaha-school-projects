# Reverse a list of ints

L = eval(input("Enter list to reverse: "))
N = []

for i in range(-1, -len(L)-1, -1):
    N.append(L[i])

print("Reversed list is:", N)
