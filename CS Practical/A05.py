#  Simple and compound interest

P = float(input("Enter principal: "))
R = float(input("Enter annual RoI (%): ")) / 100
T = float(input("Enter time (years): "))

C = int(input("Compounds per annum: "))

# Calculate simple interest

SI = P*R*T

# Calculate compound interest
R = R/C
T = int(T*C)
CI = (P*(1+R)**T) - P

# Print results
print("Simple Interest:", SI)
print("Compound Interest:", CI)
