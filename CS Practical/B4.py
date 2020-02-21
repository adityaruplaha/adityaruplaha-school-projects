# Implement list.count()

L = eval(input("Enter a list: "))
E = (type(L[0]))(input("Enter element: "))

count = 0

for i in range(len(L)):
    if L[i] == E:
        count += 1

print("Element {} is present {} times".format(E, count))
