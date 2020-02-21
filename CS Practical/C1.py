# check if a string is a palindrome

S = input("Enter a string: ")

P = True
for i in range(len(S) // 2):
    P = (S[i] == S[-i-1])
    if not P:
        break

if P:
    print("Palindrome.")
else:
    print("Not a palindrome.")
