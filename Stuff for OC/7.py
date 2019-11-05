from math import fabs

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

D = fabs(a - b)

if D <= 0.001:
    print("Close.")
else:
    print("Not Close.")