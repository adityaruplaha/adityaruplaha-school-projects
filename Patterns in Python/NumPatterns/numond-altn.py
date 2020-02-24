n = int(input("Enter iterations: "))
print()

for i in range(1, 10):
    print((' '.join([str(i)]*i).center(17).ljust(34) + '  ')*n)

for i in range(9, 0, -1):
    print(' ' + (' '.join([str(i)]*i).center(17).rjust(34) + '  ')*n)
