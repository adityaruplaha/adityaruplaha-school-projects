L = []

L.append(float(input("Enter a no.: ")))
L.append(float(input("Enter a no.: ")))
L.append(float(input("Enter a no.: ")))
L.append(float(input("Enter a no.: ")))
L.append(float(input("Enter a no.: ")))
# you can have as many as you like

for _ in range(len(L) - 1):
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]

print("Result:", L)