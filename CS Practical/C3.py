# Fibonacci Series

n = int(input("Enter no. of elements to print: "))

F = [0, 1]

for i in range(n-2):
    F.append(F[-2] + F[-1])

print("Series is:", F)
