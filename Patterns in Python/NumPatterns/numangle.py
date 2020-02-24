n = int(input("Enter iterations: "))
print()

for i in range(1, 10):
    print(((' '.join([str(i)]*i).center(17)) + (' '.join([str(10 - i)]*(10 - i)).center(17)))*n)

print()
