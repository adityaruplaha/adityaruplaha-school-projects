# Memecaseify: "how dare you" --> "hOw dArE YoU"

S = input("Enter a string: ")

N = ""

for i in range(len(S)):
    if i % 2:
        N += S[i].upper()
    else:
        N += S[i]

print("Required string is: ", N)
