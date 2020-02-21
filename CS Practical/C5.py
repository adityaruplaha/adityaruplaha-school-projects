# Reverse a number

N = int(input("Enter a number: "))

R = 0

while N:
    R *= 10
    R += N % 10
    N //= 10

print("Reversed no. is:", R)
