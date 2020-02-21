# Concatenate 2 lists --> the hard way

L1 = eval(input("Enter a list: "))
L2 = eval(input("Enter another list: "))

N = []
for e in L1:
    N.append(e)
for e in L2:
    N.append(e)

print("Concatenated list is:", N)
