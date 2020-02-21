# Check if angles for a triangle

print("Enter 3 angles:")
a = float(input())
b = float(input())
c = float(input())

if a+b+c == 180:
    print("They form a triangle.")
else:
    print("They don't form a triangle.")
