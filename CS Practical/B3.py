# Search for given element

L = eval(input("Enter a list: "))
E = (type(L[0]))(input("Enter element: "))

indices = []

for i in range(len(L)):
    if L[i] == E:
        indices.append(i)

print("Element {} is @ {}".format(E, indices))
