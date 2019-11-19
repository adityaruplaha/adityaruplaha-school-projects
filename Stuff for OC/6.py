n = int(input("Enter no. of items: "))

if n < 10:
    cost = 120
elif n < 100:
    cost = 100
else:
    cost = 70

print("Total cost is:", n*cost)
