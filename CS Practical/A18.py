# Eligibility to vote. Senior citizen?

age = float(input("Enter age: "))

if age > 18:
    print("Eligible to vote.")
    if age > 60:
        print("Senior citizen.")
    else:
        print("Not a senior citizen.")
else:
    print("Not eligible to vote.")
