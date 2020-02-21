# Locate minimum element

L = eval(input("Enter a list: "))

indices = []
m = L[0]

for i in range(len(L)):
    e = L[i]
    if e < m:
        m = e
        indices.clear()
        indices.append(i)
    elif e == m:
        indices.append(i)

print("Minimum element is: {} @ {}".format(m, indices))
